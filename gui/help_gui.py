"""
RefiX Help GUI
Displays hotkey reference guide and usage instructions.
"""

import sys
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


def get_icon_path() -> Path:
    """Get the path to the logo icon."""
    return Path(__file__).parent.parent / 'logo.ico'


def create_help_gui() -> None:
    """Create and display the help GUI."""
    # Create the main window
    app = ctk.CTk()
    app.title("RefiX - Hotkey Help")
    app.geometry("750x550")
    app.resizable(False, False)
    
    # Set icon if available
    icon_path = get_icon_path()
    if icon_path.exists():
        try:
            app.iconbitmap(str(icon_path))
        except Exception as e:
            logger.warning(f"Could not set icon: {e}")
    
    # Create a main frame with padding
    frame = ctk.CTkScrollableFrame(app, corner_radius=15)
    frame.pack(expand=True, fill='both', padx=40, pady=30)
    
    # Title with modern styling
    title = ctk.CTkLabel(
        frame,
        text="🚀 RefiX Hotkey Reference Guide",
        font=ctk.CTkFont(family="Segoe UI", size=26, weight="bold"),
        text_color=("gray10", "gray90")
    )
    title.pack(pady=(20, 5))
    
    # Subtitle
    subtitle = ctk.CTkLabel(
        frame,
        text="Below is a detailed explanation of each available hotkey and its function.\nPress the hotkeys after selecting text:",
        font=ctk.CTkFont(family="Segoe UI", size=13),
        text_color=("gray50", "gray80"),
        justify="center"
    )
    subtitle.pack(pady=(0, 20))
    
    # Hotkey descriptions
    hotkeys = [
        ("Alt + P",
         "Professional Rewrite – Enhances the selected text by making it more polished, formal, and professional. "
         "Useful for emails, reports, or any communication that requires a refined tone. The improved version is also copied to your clipboard."),
        
        ("Alt + G",
         "Grammar Correction – Corrects grammatical mistakes, punctuation errors, and awkward phrasing in the selected text. "
         "This ensures that your writing is clear, accurate, and stylistically consistent."),
        
        ("Alt + F",
         "Fix Code – Automatically formats and improves selected programming code. "
         "This includes fixing syntax issues, improving readability, and ensuring consistency across your script."),
        
        ("Alt + L",
         "Lengthen & Elaborate – Expands the selected text into a longer and more detailed explanation. "
         "Ideal when you want to provide additional context, clarification, or in-depth descriptions."),
        
        ("Alt + H",
         "Help – Opens this Help window, providing a complete overview of all available hotkeys and their functionalities."),
        
        ("Alt + ESC",
         "Exit Application – Closes the entire app immediately. Use this shortcut when you want to quickly quit the program."),
    ]
    
    for key, desc in hotkeys:
        # Container for each hotkey entry
        entry_frame = ctk.CTkFrame(frame, fg_color="transparent")
        entry_frame.pack(pady=(10, 5), fill="x")
        
        # Shortcut Key (centered and bold)
        key_label = ctk.CTkLabel(
            entry_frame,
            text=key,
            font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
            text_color=("#5BA3FF", "#5BA3FF"),
            justify="center"
        )
        key_label.pack(pady=(5, 0))
        
        # Description (left aligned)
        desc_label = ctk.CTkLabel(
            entry_frame,
            text=desc,
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color=("gray70", "gray80"),
            wraplength=580,
            justify="left"
        )
        desc_label.pack(anchor="center", pady=(2, 8))
    
    # Separator
    separator = ctk.CTkFrame(frame, height=2, fg_color=("gray70", "gray30"))
    separator.pack(fill="x", padx=50, pady=(15, 10))
    
    # Footer tips
    footer = ctk.CTkLabel(
        frame,
        text="💡 Tip: First select the text, then press the hotkey.\n"
             "For rewriting and corrections, keep the text selected to enable automatic replacement.\n"
             "All processed text is automatically copied to your clipboard.",
        font=ctk.CTkFont(family="Segoe UI", size=12, slant="italic"),
        text_color=("gray40", "gray70"),
        wraplength=580,
        justify="center"
    )
    footer.pack(pady=(10, 10))
    
    # Version info
    version_label = ctk.CTkLabel(
        frame,
        text="RefiX v2.0.0 | Made with ❤️ by MrTG1B",
        font=ctk.CTkFont(family="Segoe UI", size=9),
        text_color=("gray40", "gray60")
    )
    version_label.pack(side="bottom", pady=(10, 20))
    
    logger.info("Help GUI initialized")
    # Run the main event loop
    app.mainloop()


if __name__ == "__main__":
    create_help_gui()
