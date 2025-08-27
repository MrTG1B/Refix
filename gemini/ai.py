import google.generativeai as genai
import os
from dotenv import load_dotenv

#AIzaSyDeayjI6wr935aJW-8kSEqeOvVDyQ1QV4w
# Load environment variables from .env file located in the parent directory
# This assumes the .env file is one level up from the current script's directory.
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

# Get the API key from the environment variable.
# It's crucial to set the GEMINI_API_KEY environment variable for this script to run.
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

# Configure the genai library with the obtained API key.
genai.configure(api_key=api_key)

# Initialize the GenerativeModel with the specified model name.
# 'gemini-2.5-flash' is chosen for its speed and efficiency.
model = genai.GenerativeModel('gemini-2.5-flash')

# Prompts for different AI functionalities.
# These are designed to guide the AI's response format (just the text, no extra conversation).
P_PROMPT = "Please rewrite the passage in a more professional tone keeping the same meaning and more human-like tone and don't use any fancy words. The output should exclusively comprise the refined text, devoid of any additional commentary.\n\nThe Text: \n\n"
G_PROMPT = "Please correct any grammatical errors in the passage keeping the same meaning. The response must solely comprise the corrected text, without additional commentary.\n\nThe Text: \n\n"
F_PROMPT = "The provided source code necessitates comprehensive formatting and error correction. The resulting output must exclusively comprise the refined code. All supplementary information and specific instructions shall be embedded as inline comments within the code structure, eliminating any external narrative or explanatory text from the final output.\n\nThe Source Code:\n\n"
L_PROMPT = "Please make the passage long and detailed in content and structure maintaining a professional tone. The output should exclusively comprise the , devoid of any additional commentary.\n\nThe Text: \n\n"


def ai_prompt(prompt: str, type: str) -> str:
    """
    Interacts with the Gemini AI model based on the specified type of prompt.

    Args:
        prompt (str): The text content to be processed by the AI.
        type (str): The type of processing to perform.
                    'p' for professionalizing the passage.
                    'g' for grammatical correction.
                    'f' for code formatting.

    Returns:
        str: The processed text from the Gemini AI.

    Raises:
        ValueError: If an unsupported 'type' is provided, indicating an invalid request.
        Exception: Catches and prints any other exceptions that occur during AI interaction,
                   returning an error message.
    """
    try:
        add_prompt = ""
        if type == "p":
            add_prompt = P_PROMPT
        elif type == "g":
            add_prompt = G_PROMPT
        elif type == "f":
            add_prompt = F_PROMPT
        elif type == "l":
            add_prompt = L_PROMPT
        else:
            raise ValueError(f"Unsupported prompt type: {type}. Expected 'p', 'g', or 'f'.")

        response = model.generate_content(add_prompt + prompt)

        # Clean markdown formatting (remove ``` and language names)
        fixed_response = response.text
        import re
        fixed_response = re.sub(r"```[a-zA-Z0-9]*\n?", "", fixed_response)  # remove opening fences
        fixed_response = fixed_response.replace("```", "")  # remove closing fences
        fixed_response = fixed_response.strip()  # clean whitespace

        return fixed_response
    except Exception as e:
        print(f"An error occurred during AI interaction: {e}")
        return f"Error: {e}"
