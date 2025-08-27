import customtkinter as ctk

# Set theme and color scheme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create the main window
app = ctk.CTk()
app.title("Hotkey Help")
app.geometry("750x500")
app.resizable(False, False)
app.iconbitmap('logo.ico')

# Create a main frame with padding
frame = ctk.CTkScrollableFrame(app, corner_radius=15)
frame.pack(expand=True, fill='both', padx=40, pady=30)

# Title with modern styling
title = ctk.CTkLabel(
    frame, 
    text="🚀 Hotkey Reference Guide",
    font=ctk.CTkFont(family="Segoe UI", size=26, weight="bold"),
    text_color=("gray10", "gray90")
)
title.pack(pady=(20, 5))

# Subtitle
subtitle = ctk.CTkLabel(
    frame,
    text="Below is a detailed explanation of each available hotkey and its function. Press the hotkeys after selecting text:",
    font=ctk.CTkFont(family="Segoe UI", size=13),
    text_color=("gray50", "gray80")
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
    # Center + Bold Shortcut Key
    key_label = ctk.CTkLabel(
        frame,
        text=key,
        font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
        text_color=("gray90", "white"),
        justify="center"
    )
    key_label.pack(pady=(10, 0))

    # Left aligned Description
    desc_label = ctk.CTkLabel(
        frame,
        text=desc,
        font=ctk.CTkFont(family="Segoe UI", size=12),
        text_color=("gray70", "gray80"),
        wraplength=550,
        justify="left"
    )
    desc_label.pack(anchor="center", pady=(2, 8))

# Footer
footer = ctk.CTkLabel(
    frame,
    text="💡 Tip: First select the text, then press the hotkey. "
         "For rewriting and corrections, keep the text selected to enable automatic replacement.",
    font=ctk.CTkFont(family="Segoe UI", size=12, slant="italic"),
    text_color=("gray40", "gray70"),
    wraplength=550,
    justify="center"
)
footer.pack(side="bottom", pady=(20, 10))

# Run the main event loop
app.mainloop()
