# RefiX - AI-Powered Text Enhancement Tool

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/MrTG1B/Refix)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

RefiX is a professional, enterprise-grade AI-powered text enhancement tool that helps you improve your writing with simple keyboard shortcuts. Using Google's Gemini AI, it can professionalize text, correct grammar, format code, and expand content - all accessible via intuitive hotkeys.

## ✨ Features

- **Professional Rewriting** (`Alt+P`): Transform casual text into polished, professional content
- **Grammar Correction** (`Alt+G`): Fix grammatical errors and improve sentence structure
- **Code Formatting** (`Alt+F`): Automatically format and improve source code
- **Content Expansion** (`Alt+L`): Elaborate and extend text with detailed explanations
- **Quick Help** (`Alt+H`): Access hotkey reference guide
- **Easy Exit** (`Alt+Esc`): Quickly close the application

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MrTG1B/Refix.git
   cd Refix
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key:**
   - Copy `.env.example` to `.env`
   - Add your Gemini API key to the `.env` file:
     ```
     GEMINI_API_KEY="your-api-key-here"
     ```

4. **Run the application:**
   ```bash
   python APP.py
   ```

## 📖 Usage

1. **Start the application** - Run `python APP.py`
2. **Select text** in any application
3. **Press the hotkey** for the desired function:
   - `Alt+P` - Professionalize text
   - `Alt+G` - Correct grammar
   - `Alt+F` - Format code
   - `Alt+L` - Lengthen and elaborate
   - `Alt+H` - Open help guide
   - `Alt+Esc` - Exit application

The enhanced text will automatically replace your selection and be copied to your clipboard.

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
GEMINI_API_KEY="your-api-key-here"
LOG_LEVEL=INFO                    # Optional: DEBUG, INFO, WARNING, ERROR
LOG_FILE=refix.log                # Optional: Log file path
```

### First-Time Setup

If you run the application without a configured API key, a GUI will guide you through the setup process.

## 🏗️ Project Structure

```
Refix/
├── APP.py                 # Main application entry point
├── gemini/
│   ├── __init__.py       # Package initialization
│   └── ai.py             # AI interaction module
├── gui/
│   ├── __init__.py       # Package initialization
│   ├── gui.py            # API key setup GUI
│   └── help_gui.py       # Help reference GUI
├── .env.example          # Environment template
├── .gitignore            # Git ignore rules
├── requirements.txt      # Python dependencies
├── README.md             # This file
├── LICENSE               # License information
└── logo.ico              # Application icon
```

## 🔒 Security

- **Never commit your `.env` file** - It contains sensitive API keys
- The `.gitignore` file is configured to exclude `.env` files
- API keys are loaded securely from environment variables
- Input validation prevents injection attacks
- Error messages sanitized to prevent information leakage

## 🐛 Troubleshooting

### Common Issues

**API Key Not Found:**
- Ensure `.env` file exists in the root directory
- Verify `GEMINI_API_KEY` is set correctly (no spaces, proper quotes)
- Check that `.env` file is not in `.gitignore` locally

**Hotkeys Not Working:**
- Run the application with administrator privileges (required for global hotkeys)
- Check for conflicting hotkey assignments from other applications
- Ensure keyboard module has proper permissions

**GUI Not Showing:**
- Verify customtkinter is installed: `pip install customtkinter`
- Check Python version is 3.8 or higher
- Ensure icon file `logo.ico` exists in the root directory

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Google Gemini AI](https://deepmind.google/technologies/gemini/)
- UI powered by [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on [GitHub](https://github.com/MrTG1B/Refix/issues)
- Visit the [project website](https://mrtg1b.vercel.app/projects/refix)

## 🗺️ Roadmap

- [ ] Cross-platform support improvements
- [ ] Additional AI models support
- [ ] Custom prompt templates
- [ ] Command-line interface
- [ ] Plugin system for extensibility
- [ ] Multi-language support

---

**Made with ❤️ by MrTG1B**
