import os
import webbrowser
import customtkinter as ctk
import subprocess

# Set theme and color scheme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def open_link():
    webbrowser.open('https://aistudio.google.com/app/apikey')

def save_api_key():
    api_key = api_entry.get().strip()
    if api_key:
        dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
        with open(dotenv_path, 'w') as f:
            f.write(f'GEMINI_API_KEY="{api_key}"\n')
        status_label.configure(text="✓ API Key saved successfully!", text_color=("lime", "lime"))
        app.after(1500, app.destroy)  # Close window after 1.5 seconds
    else:
        status_label.configure(text="⚠ Please enter a valid API key", text_color=("red", "red"))

# Create the main window
app = ctk.CTk()
app.title("RefiX Setup")
app.geometry("500x380")
app.resizable(False, False)
app.iconbitmap('logo.ico')

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
    text="Please enter your API key to get started",
    font=ctk.CTkFont(family="Segoe UI", size=12),
    text_color=("gray20", "gray80")
)
subtitle.pack(pady=(0, 20))

# API Entry field with modern look
api_entry = ctk.CTkEntry(
    frame,
    font=ctk.CTkFont(family="Segoe UI", size=12),
    width=300,
    height=40,
    corner_radius=8,
    placeholder_text="Enter your API key here"
)
api_entry.pack(pady=(0, 15))

# Save button with modern styling
save_btn = ctk.CTkButton(
    frame,
    text="Save API Key",
    command=save_api_key,
    width=200,
    height=40,
    corner_radius=8,
    font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold")
)
save_btn.pack(pady=(0, 20))

# Help link with modern styling
link_label = ctk.CTkLabel(
    frame,
    text="Need an API key? Click here to get one",
    font=ctk.CTkFont(family="Segoe UI", size=10, underline=True),
    text_color=("#4A9EFF", "#4A9EFF"),
    cursor="hand2"
)
link_label.pack(pady=(0, 10))
link_label.bind("<Button-1>", lambda e: open_link())

# Status label with modern styling
status_label = ctk.CTkLabel(
    frame,
    text="",
    font=ctk.CTkFont(family="Segoe UI", size=11),
)
status_label.pack(pady=(10, 0))

app.mainloop()
subprocess.run(["python","gui/help_gui.py"])