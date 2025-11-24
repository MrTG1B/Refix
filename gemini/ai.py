"""
AI Module for RefiX
Handles interaction with Google's Gemini AI for text enhancement.
"""

import google.generativeai as genai
import os
import logging
import time
from typing import Optional
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables from .env file located in the parent directory
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

# Get the API key from the environment variable
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key or not api_key.strip():
    logger.error("GEMINI_API_KEY environment variable not set or empty")
    raise ValueError("GEMINI_API_KEY environment variable not set. Please configure it in the .env file.")

# Validate API key format (basic check)
if len(api_key.strip()) < 20:
    logger.warning("API key seems too short, please verify it's correct")

# Configure the genai library with the obtained API key
try:
    genai.configure(api_key=api_key.strip())
    logger.info("Gemini AI configured successfully")
except Exception as e:
    logger.error(f"Failed to configure Gemini AI: {e}")
    raise

# Initialize the GenerativeModel with the specified model name
# 'gemini-2.0-flash-exp' is chosen for its speed and efficiency
try:
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    logger.info("Gemini model initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize Gemini model: {e}")
    raise

# Prompts for different AI functionalities
# These are designed to guide the AI's response format (just the text, no extra conversation)
P_PROMPT = """Please rewrite the passage in a more professional tone keeping the same meaning and more human-like tone. 
Avoid using overly complex or fancy words. The output should exclusively comprise the refined text, 
devoid of any additional commentary, explanations, or meta-discussion.

The Text:

"""

G_PROMPT = """Please correct any grammatical errors in the passage while keeping the same meaning. 
The response must solely comprise the corrected text, without additional commentary, explanations, or meta-discussion.

The Text:

"""

F_PROMPT = """The provided source code requires comprehensive formatting and error correction. 
The resulting output must exclusively comprise the refined code. All supplementary information and 
specific instructions shall be embedded as inline comments within the code structure, eliminating 
any external narrative or explanatory text from the final output.

The Source Code:

"""

L_PROMPT = """Please make the passage longer and more detailed in both content and structure while 
maintaining a professional tone. The output should exclusively comprise the expanded text, 
devoid of any additional commentary, explanations, or meta-discussion.

The Text:

"""

# Configuration constants
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds
REQUEST_TIMEOUT = 30  # seconds


def _sanitize_input(text: str) -> str:
    """
    Sanitize user input to prevent injection attacks and ensure valid input.
    
    Args:
        text (str): The input text to sanitize.
        
    Returns:
        str: Sanitized text.
        
    Raises:
        ValueError: If input is invalid or too long.
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    # Remove null bytes and other control characters (except newlines and tabs)
    sanitized = ''.join(char for char in text if char.isprintable() or char in '\n\t\r')
    
    # Limit input length (100KB max)
    max_length = 100000
    if len(sanitized) > max_length:
        logger.warning(f"Input text truncated from {len(sanitized)} to {max_length} characters")
        sanitized = sanitized[:max_length]
    
    return sanitized


def _clean_response(response_text: str) -> str:
    """
    Clean markdown formatting from AI response.
    
    Args:
        response_text (str): Raw response from AI.
        
    Returns:
        str: Cleaned response text.
    """
    import re
    
    # Remove code block markers (``` with optional language specifiers)
    cleaned = re.sub(r"```[a-zA-Z0-9]*\n?", "", response_text)
    cleaned = cleaned.replace("```", "")
    
    # Clean whitespace
    cleaned = cleaned.strip()
    
    return cleaned


def ai_prompt(prompt: str, prompt_type: str) -> str:
    """
    Interact with the Gemini AI model based on the specified type of prompt.
    Includes retry logic, timeout handling, and comprehensive error management.
    
    Args:
        prompt (str): The text content to be processed by the AI.
        prompt_type (str): The type of processing to perform.
                          'p' for professionalizing the passage.
                          'g' for grammatical correction.
                          'f' for code formatting.
                          'l' for lengthening and elaborating.
    
    Returns:
        str: The processed text from the Gemini AI.
    
    Raises:
        ValueError: If an unsupported 'prompt_type' is provided or input is invalid.
        RuntimeError: If AI interaction fails after all retries.
    """
    # Validate and sanitize input
    try:
        sanitized_prompt = _sanitize_input(prompt)
    except ValueError as e:
        logger.error(f"Input validation failed: {e}")
        return f"Error: Invalid input - {e}"
    
    if not sanitized_prompt.strip():
        logger.warning("Empty prompt provided")
        return "Error: Please provide some text to process"
    
    # Select the appropriate prompt template
    prompt_templates = {
        "p": P_PROMPT,
        "g": G_PROMPT,
        "f": F_PROMPT,
        "l": L_PROMPT
    }
    
    if prompt_type not in prompt_templates:
        error_msg = f"Unsupported prompt type: {prompt_type}. Expected 'p', 'g', 'f', or 'l'."
        logger.error(error_msg)
        raise ValueError(error_msg)
    
    add_prompt = prompt_templates[prompt_type]
    full_prompt = add_prompt + sanitized_prompt
    
    # Attempt API call with retry logic
    last_exception = None
    for attempt in range(MAX_RETRIES):
        try:
            logger.info(f"Attempting AI request (attempt {attempt + 1}/{MAX_RETRIES}) for type '{prompt_type}'")
            
            # Generate content with timeout consideration
            response = model.generate_content(full_prompt)
            
            if not response or not hasattr(response, 'text'):
                raise RuntimeError("Invalid response from AI model")
            
            # Clean and return the response
            cleaned_response = _clean_response(response.text)
            logger.info(f"AI request successful on attempt {attempt + 1}")
            return cleaned_response
            
        except Exception as e:
            last_exception = e
            logger.warning(f"AI request failed on attempt {attempt + 1}/{MAX_RETRIES}: {e}")
            
            # Don't retry on certain errors
            if "API key" in str(e) or "authentication" in str(e).lower():
                logger.error("Authentication error - not retrying")
                return "Error: Invalid API key. Please check your configuration."
            
            # Wait before retrying (exponential backoff)
            if attempt < MAX_RETRIES - 1:
                wait_time = RETRY_DELAY * (2 ** attempt)
                logger.info(f"Waiting {wait_time} seconds before retry...")
                time.sleep(wait_time)
    
    # All retries exhausted
    error_msg = f"AI request failed after {MAX_RETRIES} attempts"
    logger.error(f"{error_msg}: {last_exception}")
    return f"Error: Unable to process request. Please try again later."
