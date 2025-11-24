"""
RefiX - AI-Powered Text Enhancement Tool
Main application entry point.

Version: 2.0.0
Author: MrTG1B
License: MIT
"""

import os
import sys
import shutil
import subprocess
import time
import logging
from typing import Optional
from pathlib import Path

try:
    import pyperclip
    import keyboard
    from dotenv import load_dotenv
except ImportError as e:
    print(f"Error: Required package not installed: {e}")
    print("Please run: pip install -r requirements.txt")
    sys.exit(1)

# Application metadata
__version__ = "2.0.0"
__author__ = "MrTG1B"

# Configure logging
log_level = os.environ.get("LOG_LEVEL", "INFO")
log_file = os.environ.get("LOG_FILE", "refix.log")

logging.basicConfig(
    level=getattr(logging, log_level, logging.INFO),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

logger.info(f"Starting RefiX v{__version__}")


def is_windows() -> bool:
    """Check if running on Windows."""
    return sys.platform.startswith('win')


def get_script_dir() -> Path:
    """Get the directory where the script is located."""
    return Path(__file__).parent.absolute()


def add_to_startup() -> None:
    """
    Attempt to add the application to Windows startup (optional feature).
    Only works on Windows. Fails gracefully on other platforms.
    """
    if not is_windows():
        logger.info("Startup installation skipped (not on Windows)")
        return
    
    try:
        startup_folder = os.path.join(
            os.environ["APPDATA"],
            "Microsoft",
            "Windows",
            "Start Menu",
            "Programs",
            "Startup"
        )
        
        if not os.path.exists(startup_folder):
            logger.warning(f"Startup folder not found: {startup_folder}")
            return
        
        exe_path = os.path.abspath(__file__)
        exe_name = os.path.basename(exe_path)
        destination_path = os.path.join(startup_folder, exe_name)
        
        if os.path.exists(destination_path):
            logger.info(f"Already in startup: {exe_name}")
            return
        
        shutil.copy(exe_path, startup_folder)
        logger.info(f"✅ Added {exe_name} to Startup folder")
        print(f"✅ Added {exe_name} to Startup folder.")
        
    except KeyError:
        logger.warning("APPDATA environment variable not found")
    except PermissionError:
        logger.warning("Insufficient permissions to add to startup")
    except Exception as e:
        logger.warning(f"Failed to add to Startup: {e}")
        print(f"⚠️ Failed to add to Startup: {e}")


def setup_environment() -> Optional[str]:
    """
    Set up the application environment and validate configuration.
    
    Returns:
        Optional[str]: API key if successfully loaded, None otherwise.
    """
    script_dir = get_script_dir()
    dotenv_path = script_dir / '.env'
    
    # Check if .env file exists
    if not dotenv_path.is_file():
        logger.warning(f".env file not found at {dotenv_path}")
        print(f".env file not found at {dotenv_path}. Creating .env file...")
        
        try:
            with open(dotenv_path, 'w') as f:
                f.write('GEMINI_API_KEY=""\n')
            logger.info("Created .env file")
            print("Created .env file. Please add your GEMINI_API_KEY.")
        except Exception as e:
            logger.error(f"Failed to create .env file: {e}")
            print(f"Error creating .env file: {e}")
            return None
        
        # Launch GUI for API key input
        launch_setup_gui(script_dir)
        return None
    
    # Load environment variables from .env file
    try:
        load_dotenv(dotenv_path=str(dotenv_path))
        logger.info("Loaded environment variables from .env")
    except Exception as e:
        logger.error(f"Failed to load .env file: {e}")
        print(f"Error loading .env file: {e}")
        return None
    
    # Check if GEMINI_API_KEY is present and valid
    api_key = os.environ.get("GEMINI_API_KEY", "").strip().strip('"').strip("'")
    
    if not api_key:
        logger.warning("GEMINI_API_KEY not found or empty in .env file")
        print("GEMINI_API_KEY not found in .env file. Launching GUI to enter API key...")
        launch_setup_gui(script_dir)
        return None
    
    logger.info("API key loaded successfully")
    return api_key


def launch_setup_gui(script_dir: Path) -> None:
    """
    Launch the GUI for API key setup.
    
    Args:
        script_dir (Path): Path to the script directory.
    """
    gui_path = script_dir / "gui" / "gui.py"
    
    if not gui_path.exists():
        logger.error(f"GUI script not found at {gui_path}")
        print(f"Error: GUI script not found at {gui_path}")
        return
    
    try:
        logger.info("Launching setup GUI")
        subprocess.run([sys.executable, str(gui_path)], check=False)
    except Exception as e:
        logger.error(f"Failed to launch setup GUI: {e}")
        print(f"Error launching setup GUI: {e}")


def launch_help_gui(script_dir: Path) -> None:
    """
    Launch the help GUI.
    
    Args:
        script_dir (Path): Path to the script directory.
    """
    help_gui_path = script_dir / "gui" / "help_gui.py"
    
    if not help_gui_path.exists():
        logger.error(f"Help GUI script not found at {help_gui_path}")
        print(f"Error: Help GUI script not found at {help_gui_path}")
        return
    
    try:
        logger.info("Launching help GUI")
        subprocess.run([sys.executable, str(help_gui_path)], check=False)
    except Exception as e:
        logger.error(f"Failed to launch help GUI: {e}")
        print(f"Error launching help GUI: {e}")



def call_ai(prompt: str, process_type: str) -> None:
    """
    Call the AI with the given prompt and type, then copy/write the response.
    
    Args:
        prompt (str): The text to process.
        process_type (str): Type of processing (p/g/f/l).
    """
    try:
        logger.info(f"Processing AI request of type '{process_type}'")
        response = ai.ai_prompt(prompt, process_type)
        
        if response.startswith("Error:"):
            logger.error(f"AI processing error: {response}")
            print(f"❌ {response}")
            return
        
        # Copy to clipboard
        try:
            pyperclip.copy(response)
            logger.debug("Response copied to clipboard")
        except Exception as e:
            logger.warning(f"Failed to copy to clipboard: {e}")
        
        # Write the response (replace selected text)
        try:
            keyboard.write(response)
            logger.debug("Response written via keyboard")
        except Exception as e:
            logger.warning(f"Failed to write response: {e}")
            print(f"⚠️ Could not write response: {e}")
        
        print("✅ AI Response processed successfully!")
        logger.info("AI request completed successfully")
        
    except Exception as e:
        logger.error(f"Unexpected error in call_ai: {e}", exc_info=True)
        print(f"❌ An error occurred: {e}")


def copy_selection(process_type: str) -> None:
    """
    Copy the current selection and process it with AI.
    
    Args:
        process_type (str): Type of AI processing to perform.
    """
    try:
        logger.debug(f"Copying selection for type '{process_type}'")
        
        # Wait for user to release the hotkey
        time.sleep(0.3)
        
        # Copy selected text to clipboard
        keyboard.press_and_release("ctrl+c")
        time.sleep(0.5)
        
        # Get clipboard content
        text = pyperclip.paste()
        logger.debug(f"Clipboard content length: {len(text) if text else 0}")
        
        if not text or not text.strip():
            logger.warning("No text captured from clipboard")
            print("⚠️ No text selected! Please select some text and try again.")
            return
        
        # Process with AI
        call_ai(text, process_type)
        
    except Exception as e:
        logger.error(f"Error in copy_selection: {e}", exc_info=True)
        print(f"❌ Error processing selection: {e}")


def setup_hotkeys(script_dir: Path) -> None:
    """
    Set up global hotkeys for the application.
    
    Args:
        script_dir (Path): Path to the script directory.
    """
    try:
        logger.info("Setting up hotkeys")
        
        # Text processing hotkeys
        keyboard.add_hotkey("alt+p", lambda: copy_selection("p"))
        keyboard.add_hotkey("alt+g", lambda: copy_selection("g"))
        keyboard.add_hotkey("alt+f", lambda: copy_selection("f"))
        keyboard.add_hotkey("alt+l", lambda: copy_selection("l"))
        
        # Help hotkey
        keyboard.add_hotkey("alt+h", lambda: launch_help_gui(script_dir))
        
        logger.info("Hotkeys registered successfully")
        print("✅ Hotkeys active:")
        print("   Alt+P - Professionalize text")
        print("   Alt+G - Correct grammar")
        print("   Alt+F - Format code")
        print("   Alt+L - Lengthen text")
        print("   Alt+H - Show help")
        print("   Alt+ESC - Exit application")
        
    except Exception as e:
        logger.error(f"Failed to setup hotkeys: {e}", exc_info=True)
        raise


def main() -> int:
    """
    Main application entry point.
    
    Returns:
        int: Exit code (0 for success, 1 for error).
    """
    try:
        # Optionally add to startup (Windows only)
        add_to_startup()
        
        # Set up environment and check API key
        api_key = setup_environment()
        if not api_key:
            logger.info("Setup incomplete - exiting")
            return 1
        
        # Import AI module (after environment is set up)
        try:
            import gemini.ai as ai_module
            global ai
            ai = ai_module
            logger.info("AI module imported successfully")
        except Exception as e:
            logger.error(f"Failed to import AI module: {e}", exc_info=True)
            print(f"❌ Failed to initialize AI module: {e}")
            print("Please check your API key and internet connection.")
            return 1
        
        # Set up hotkeys
        script_dir = get_script_dir()
        setup_hotkeys(script_dir)
        
        print("\n" + "="*50)
        print("RefiX is running! Select text and press a hotkey.")
        print("Press Alt+ESC to quit.")
        print("="*50 + "\n")
        
        # Wait for exit hotkey
        logger.info("Application ready - waiting for user input")
        keyboard.wait("alt+esc")
        
        logger.info("User requested exit")
        print("\n👋 Goodbye!")
        return 0
        
    except KeyboardInterrupt:
        logger.info("Application interrupted by user")
        print("\n\n👋 Goodbye!")
        return 0
    except Exception as e:
        logger.error(f"Fatal error in main: {e}", exc_info=True)
        print(f"\n❌ Fatal error: {e}")
        print("Please check the log file for details.")
        return 1


if __name__ == "__main__":
    sys.exit(main())