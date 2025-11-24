# Contributing to RefiX

Thank you for your interest in contributing to RefiX! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue on GitHub with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Screenshots (if applicable)
- Your environment (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please create an issue with:
- A clear, descriptive title
- Detailed description of the proposed feature
- Use cases and benefits
- Any potential drawbacks or challenges

### Pull Requests

1. **Fork the repository** and create a new branch from `main`
2. **Make your changes** following the coding standards below
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Commit with clear messages** describing what and why
6. **Submit a pull request** with a comprehensive description

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/MrTG1B/Refix.git
   cd Refix
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your `.env` file:
   ```bash
   cp .env.example .env
   # Edit .env and add your API key
   ```

## Coding Standards

### Python Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use meaningful variable and function names
- Maximum line length: 100 characters
- Use type hints where applicable
- Write docstrings for all functions, classes, and modules

### Documentation

- Keep README.md up to date
- Update CHANGELOG.md for notable changes
- Add inline comments for complex logic
- Update API documentation if adding new features

### Testing

- Write tests for new features
- Ensure existing tests pass
- Aim for high code coverage
- Test on multiple platforms if possible

### Commit Messages

Use clear and descriptive commit messages:
- Use the imperative mood ("Add feature" not "Added feature")
- First line should be 50 characters or less
- Add detailed description if needed
- Reference issues and pull requests where applicable

Example:
```
Add rate limiting for API calls

- Implement exponential backoff
- Add configuration options
- Update documentation

Fixes #123
```

## Project Structure

```
Refix/
├── APP.py              # Main entry point
├── gemini/             # AI module
│   ├── __init__.py
│   └── ai.py
├── gui/                # GUI modules
│   ├── __init__.py
│   ├── gui.py
│   └── help_gui.py
├── tests/              # Test files
├── docs/               # Documentation
└── requirements.txt    # Dependencies
```

## Security

- Never commit sensitive data (API keys, passwords, etc.)
- Follow secure coding practices
- Report security vulnerabilities privately to the maintainers
- Validate all user inputs
- Sanitize error messages

## Questions?

If you have questions or need help, feel free to:
- Open an issue on GitHub
- Reach out to the maintainers
- Check existing documentation

## License

By contributing to RefiX, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to RefiX! 🚀
