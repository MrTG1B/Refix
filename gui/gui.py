"""
RefiX API Key Setup GUI
Provides a graphical interface for configuring the Gemini API key.
"""

import os
import sys
import webbrowser
import logging
from pathlib import Path

try:
    import customtkinter as ctk
except ImportError:
    print("Error: customtkinter not installed. Run: pip install customtkinter")
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Set theme and color scheme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def get_env_path() -> Path:
    """Get the path to the .env file."""
    return Path(__file__).parent.parent / '.env'


def get_icon_path() -> Path:
    """Get the path to the logo icon."""
    return Path(__file__).parent.parent / 'logo.ico'


def open_link() -> None:
    """Open the API key help link in the default browser."""
    try:
        webbrowser.open('https://aistudio.google.com/app/apikey')
        logger.info("Opened API key help link")
    except Exception as e:
        logger.error(f"Failed to open link: {e}")


def save_api_key(api_entry, status_label, app) -> None:
    """
    Save the API key to the .env file.
    
    Args:
        api_entry: The entry widget containing the API key.
        status_label: The label widget to show status messages.
        app: The main application window.
    """
    api_key = api_entry.get().strip()
    
    if not api_key:
        status_label.configure(
            text="⚠ Please enter a valid API key",
            text_color=("red", "red")
        )
        logger.warning("Empty API key provided")
        return
    
    # Basic validation
    if len(api_key) < 20:
        status_label.configure(
            text="⚠ API key seems too short. Please verify.",
            text_color=("orange", "orange")
        )
        logger.warning(f"Potentially invalid API key (length: {len(api_key)})")
        return
    
    try:
        dotenv_path = get_env_path()
        with open(dotenv_path, 'w') as f:
            f.write(f'GEMINI_API_KEY="{api_key}"\n')
        
        status_label.configure(
            text="✓ API Key saved successfully!",
            text_color=("lime", "lime")
        )
        logger.info("API key saved successfully")
        
        # Close window after 1.5 seconds
        app.after(1500, app.destroy)
        
    except Exception as e:
        status_label.configure(
            text=f"⚠ Error saving API key: {e}",
            text_color=("red", "red")
        )
        logger.error(f"Failed to save API key: {e}")


def create_gui() -> None:
    """Create and display the setup GUI."""
    # Create the main window
    app = ctk.CTk()
    app.title("RefiX Setup")
    app.geometry("500x400")
    app.resizable(False, False)
    
    # Set icon if available
    icon_path = get_icon_path()
    if icon_path.exists():
        try:
            app.iconbitmap(str(icon_path))
        except Exception as e:
            logger.warning(f"Could not set icon: {e}")
    
    # Create a main frame with padding
    frame = ctk.CTkFrame(app, corner_radius=15)
    frame.pack(expand=True, fill='both', padx=40, pady=30)
    
    # Title with modern styling
    title = ctk.CTkLabel(
        frame,
        text="Welcome to RefiX",
        font=ctk.CTkFont(family="Segoe UI", size=24, weight="bold"),
        text_color=("gray10", "gray90")
    )
    title.pack(pady=(20, 5))
    
    # Subtitle
    subtitle = ctk.CTkLabel(
        frame,
        text="Please enter your Gemini API key to get started",
        font=ctk.CTkFont(family="Segoe UI", size=12),
        text_color=("gray20", "gray80")
    )
    subtitle.pack(pady=(0, 20))
    
    # API Entry field with modern look
    api_entry = ctk.CTkEntry(
        frame,
        font=ctk.CTkFont(family="Segoe UI", size=12),
        width=350,
        height=40,
        corner_radius=8,
        placeholder_text="Enter your API key here"
    )
    api_entry.pack(pady=(0, 15))
    
    # Status label (initially empty)
    status_label = ctk.CTkLabel(
        frame,
        text="",
        font=ctk.CTkFont(family="Segoe UI", size=11),
    )
    status_label.pack(pady=(10, 10))
    
    # Save button with modern styling
    save_btn = ctk.CTkButton(
        frame,
        text="Save API Key",
        command=lambda: save_api_key(api_entry, status_label, app),
        width=200,
        height=40,
        corner_radius=8,
        font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold")
    )
    save_btn.pack(pady=(5, 20))
    
    # Help link with modern styling
    link_label = ctk.CTkLabel(
        frame,
        text="Don't know how to get one? Click here",
        font=ctk.CTkFont(family="Segoe UI", size=10, underline=True),
        text_color=("#4A9EFF", "#4A9EFF"),
        cursor="hand2"
    )
    link_label.pack(pady=(0, 10))
    link_label.bind("<Button-1>", lambda e: open_link())
    
    # Footer
    footer = ctk.CTkLabel(
        frame,
        text="RefiX v2.0.0 | Made with ❤️ by MrTG1B",
        font=ctk.CTkFont(family="Segoe UI", size=9),
        text_color=("gray40", "gray60")
    )
    footer.pack(side="bottom", pady=(10, 0))
    
    logger.info("Setup GUI initialized")
    app.mainloop()


if __name__ == "__main__":
    create_gui()
