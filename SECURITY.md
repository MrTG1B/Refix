# Security Policy

## Supported Versions

The following versions of RefiX are currently supported with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 2.0.x   | :white_check_mark: |
| < 2.0   | :x:                |

## Reporting a Vulnerability

We take the security of RefiX seriously. If you have discovered a security vulnerability, please report it privately.

### How to Report

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please send an email to the repository owner or use GitHub's private vulnerability reporting feature.

Include the following information:
- Type of vulnerability
- Full paths of source file(s) related to the vulnerability
- Location of the affected source code (tag/branch/commit or direct URL)
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it

### What to Expect

- You should receive an acknowledgment within 48 hours
- We will investigate and keep you informed of the progress
- Once the vulnerability is confirmed, we will:
  - Work on a fix
  - Prepare a security advisory
  - Release a patch as soon as possible
  - Credit you for the discovery (unless you prefer to remain anonymous)

## Security Best Practices

When using RefiX, please follow these security guidelines:

### API Key Protection

1. **Never commit your `.env` file** to version control
2. **Never share your API key** publicly or in screenshots
3. **Rotate your API key** periodically
4. **Use environment-specific keys** for development vs. production
5. **Revoke compromised keys** immediately at https://aistudio.google.com/app/apikey

### Installation Security

1. **Download only from official sources** (GitHub releases)
2. **Verify checksums** when available
3. **Use virtual environments** to isolate dependencies
4. **Keep dependencies updated** regularly
5. **Review permissions** requested by the application

### Runtime Security

1. **Run with minimal privileges** - don't use administrator/root unless necessary
2. **Monitor log files** for unusual activity
3. **Validate input text** before processing
4. **Be cautious with sensitive data** - the AI processes your text on Google's servers
5. **Use secure networks** - avoid public WiFi for sensitive operations

### Data Privacy

RefiX processes text using Google's Gemini AI:
- **Your text is sent to Google's servers** for processing
- **Review Google's privacy policy** at https://policies.google.com/privacy
- **Don't process highly sensitive or confidential information** without understanding the implications
- **The application does not store your text locally** beyond temporary clipboard operations

## Known Security Considerations

### Third-Party Dependencies

RefiX relies on several third-party libraries:
- `google-generativeai` - Official Google Gemini SDK
- `pyperclip` - Clipboard operations
- `keyboard` - Global hotkey capture (requires elevated privileges on some systems)
- `python-dotenv` - Environment variable management
- `customtkinter` - GUI framework

We regularly update these dependencies to address known vulnerabilities.

### Permissions Required

RefiX requires the following permissions:
- **File system access** - To read/write `.env` configuration file
- **Network access** - To communicate with Google's Gemini API
- **Keyboard access** - To register global hotkeys and simulate keyboard input
- **Clipboard access** - To copy/paste text

On Windows, **administrator privileges may be required** for global hotkey functionality.

## Security Measures Implemented

### Input Validation
- All user inputs are sanitized before processing
- Text length is limited to prevent resource exhaustion
- Special characters and control codes are filtered

### Error Handling
- Error messages are sanitized to prevent information leakage
- Sensitive data is not logged
- Stack traces are limited in production mode

### API Communication
- Secure HTTPS connections to Google's API
- API key validation before use
- Retry logic with exponential backoff to prevent abuse
- Request timeouts to prevent hanging

### Code Quality
- Regular security audits
- Dependency vulnerability scanning
- Following OWASP secure coding practices
- Type checking and validation throughout

## Vulnerability Disclosure Timeline

We aim to handle vulnerability reports according to the following timeline:
- **Day 0**: Vulnerability reported
- **Day 1-2**: Initial acknowledgment and assessment
- **Day 3-7**: Validation and investigation
- **Day 7-30**: Development and testing of fix
- **Day 30-45**: Release of security patch
- **Day 45+**: Public disclosure (coordinated with reporter)

## Security Updates

Security updates will be released as:
- **Patch releases** (e.g., 2.0.1) for minor security fixes
- **Minor releases** (e.g., 2.1.0) for moderate security improvements
- **Major releases** (e.g., 3.0.0) for significant security overhauls

Users are strongly encouraged to update to the latest version promptly.

## Contact

For security-related questions or concerns:
- Review our [Security Policy](https://github.com/MrTG1B/Refix/security/policy)
- Check [Security Advisories](https://github.com/MrTG1B/Refix/security/advisories)
- Report vulnerabilities privately through GitHub

---

**Last Updated**: 2024-11-24
**Version**: 2.0.0
