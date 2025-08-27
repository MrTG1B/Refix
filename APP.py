import os
import shutil
import subprocess
import time
import pyperclip
import keyboard
from dotenv import load_dotenv


# -----------------------------
# Auto-add to Windows Startup
# -----------------------------
try:
    startup_folder = os.path.join(
        os.environ["APPDATA"],
        "Microsoft",
        "Windows",
        "Start Menu",
        "Programs",
        "Startup"
    )
    exe_path = os.path.abspath(__file__)  # Path to this running exe/script
    exe_name = os.path.basename(exe_path)
    destination_path = os.path.join(startup_folder, exe_name)

    if not os.path.exists(destination_path):
        shutil.copy(exe_path, startup_folder)
        print(f"✅ Added {exe_name} to Startup folder.")
except Exception as e:
    print(f"⚠️ Failed to add to Startup: {e}")

# -----------------------------
# Main Application Logic
# -----------------------------
# Path to .env file (in current directory)
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

# Check if .env file exists
if not os.path.isfile(dotenv_path):
    print(f".env file not found at {dotenv_path}. Creating .env file...")
    with open(dotenv_path, 'w') as f:
        f.write('GEMINI_API_KEY=""\n')
    print("Created .env file. Please add your GEMINI_API_KEY.")
    subprocess.run(["python", os.path.join(os.path.dirname(__file__), "gui", "gui.py")])
    exit()

# Load environment variables from .env file
load_dotenv(dotenv_path=dotenv_path)

# Check if GEMINI_API_KEY is present in .env
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key or api_key.strip() == "":
    print("GEMINI_API_KEY not found in .env file. Launching GUI to enter API key...")
    subprocess.run(["python", os.path.join(os.path.dirname(__file__), "gui", "gui.py")])
    exit()

import gemini.ai as ai

def call_AI(prompt: str, type: str):
    response = ai.ai_prompt(prompt, type)
    pyperclip.copy(response)
    keyboard.write(response)
    print("✅ AI Response copied to clipboard!")

def copy_selection(process_type: str):
    time.sleep(1)
    keyboard.press_and_release("ctrl+c")
    time.sleep(0.5)
    text = pyperclip.paste()
    print("DEBUG - Raw clipboard content:", repr(text))

    if text.strip():
        call_AI(text, process_type)
    else:
        print("⚠️ No text captured!")

print(".env file and GEMINI_API_KEY found!")
print("Press ALT+P after selecting text (ESC to quit)...")

keyboard.add_hotkey("alt+p", lambda: copy_selection("p"))
keyboard.add_hotkey("alt+g", lambda: copy_selection("g"))
keyboard.add_hotkey("alt+f", lambda: copy_selection("f"))
keyboard.add_hotkey("alt+l", lambda: copy_selection("l"))
keyboard.add_hotkey("alt+h", subprocess.run(["python", os.path.join(os.path.dirname(__file__), "gui", "help_gui.py")]))

keyboard.wait("alt+esc")

print("Goodbye!")