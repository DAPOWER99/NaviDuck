# Contributing to NaviDuck 🦆

Thank you for considering contributing to NaviDuck! This document provides guidelines and instructions for contributing to this CLI browser project.

## 🚀 Quick Start

1. **Fork** the repository
2. **Clone** your fork:
```bash
git clone https://github.com/YOUR_USERNAME/NaviDuck.git
cd NaviDuck
```
3. **Create a branch**:
```bash
git checkout -b feature/your-feature-name
```

## 📁 Project Structure

```
NaviDuck/
├── naviduck.py          # Main application file
├── README.md           # Project documentation
├── CODE_OF_CONDUCT.md  # Community guidelines
├── requirements.txt    # Python dependencies (if any)
└── .github/           # GitHub workflows and templates
```

## 🛠️ Development Setup

### Prerequisites
- Python 3.8+
- Git

### Installation
```bash
# Clone and navigate to project
git clone https://github.com/DAPOWER99/NaviDuck.git
cd NaviDuck

# Install dependencies (if any)
# Currently no external dependencies beyond Python stdlib
# Optional: Install requests for better networking
pip install requests
```

## 🔧 Architecture Overview

### Core Components
1. **BrowserState** - Manages application state, history, bookmarks
2. **NetworkManager** - Handles HTTP requests
3. **SearchManager** - Manages search engines and parsing
4. **PageLoader** - Fetches and displays web pages
5. **TorManager** - Optional Tor integration
6. **NavAI** - AI assistant using web APIs
7. **UIManager** - CLI interface and user interaction

### Key Design Principles
- **No BeautifulSoup** - We use regex parsing instead
- **Modularity** - Each component is independent
- **Fallback support** - Multiple search engines with automatic fallback
- **Responsive CLI** - Clean, intuitive interface

## 📝 Coding Standards

### Python Style
- Follow **PEP 8** guidelines
- Use **descriptive variable names**
- Add **docstrings** for functions and classes
- Keep functions focused and single-purpose

### Code Organization
```python
# File structure example
class ComponentName:
    """Brief description of the component."""
    
    def __init__(self, dependencies):
        """Initialize with necessary dependencies."""
        pass
    
    def method_name(self, param):
        """
        Detailed description of method.
        
        Args:
            param: Description of parameter
            
        Returns:
            Description of return value
        """
        pass
```

### Error Handling
- Use **try-except** blocks for network operations
- Provide **user-friendly error messages**
- Log errors appropriately
- Use custom exceptions where needed

## 🧪 Testing

### Manual Testing Checklist
Before submitting changes, test:
- [ ] Search functionality with different engines
- [ ] Page loading and display
- [ ] AI query responses
- [ ] History and bookmark operations
- [ ] Tor integration (if applicable)
- [ ] Error handling and edge cases

### Running Tests
```bash
# Currently manual testing, but you can:
python naviduck.py
# Test various commands and features
```

## 🌟 Feature Development

### Adding a New Search Engine
1. Add to `SEARCH_ENGINES` dictionary:
```python
"new_engine": {
    "name": "Engine Name",
    "url": "https://search.endpoint.com/",
    "params": {"q": "{query}", "other": "param"},
    "icon": "ENGINE_ICON",
    "requires_tor": False,
    "enabled": True,
    "type": "html"  # or "api"
}
```

2. Add parsing logic in `SearchManager.parse_results()`:
```python
elif engine == "new_engine":
    # Add regex patterns for parsing
    pattern = r'your-regex-pattern'
```

3. Add icon to `Icons` class if needed

### Adding New Commands
1. Add command handler in `UIManager.handle_command()`:
```python
elif cmd == "newcommand":
    if not args:
        self.print_error("Usage: newcommand [args]")
        return True
    # Command logic here
```

2. Update help text in `UIManager.show_help()`

### UI/UX Improvements
- Keep **80-character width** for terminal display
- Use **color coding** consistently (see `Colors` class)
- Provide **clear prompts and feedback**
- Support **both emoji and nerd font icons**

## 📤 Pull Request Process

### Before Submitting
1. **Test your changes** thoroughly
2. **Update documentation** if needed
3. **Ensure no regression** in existing features
4. **Follow the coding standards**

### PR Description Template
```markdown
## Description
Brief description of the changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing Performed
- [ ] Tested search functionality
- [ ] Tested page loading
- [ ] Tested AI features
- [ ] Tested on [OS: e.g., Windows/Linux]

## Screenshots (if applicable)

## Related Issues
Closes #issue_number
```

### Review Process
1. **Automated checks** (if any) must pass
2. **Code review** by maintainers
3. **Discussion** of any requested changes
4. **Merge** after approval

## 🐛 Reporting Bugs

### Bug Report Template
```markdown
**Description:**
Clear description of the bug

**Steps to Reproduce:**
1. Command: `...`
2. Action: `...`
3. Result: `...`

**Expected Behavior:**
What should have happened

**Environment:**
- OS: [e.g., Windows 11]
- Python Version: [e.g., 3.9.0]
- NaviDuck Version: [commit hash or version]

**Additional Context:**
Screenshots, logs, etc.
```

## 💡 Feature Requests

### Feature Request Template
```markdown
**Feature Description:**
Clear description of the requested feature

**Use Case:**
Why this feature would be useful

**Proposed Implementation:**
Optional: Suggestions for how to implement

**Alternatives Considered:**
Other ways to achieve the same goal
```

## 🏆 Recognition

Contributors will be:
- Listed in the README.md (if significant contribution)
- Thanked in release notes
- Acknowledged in the project

## ❓ Need Help?

- **Open an issue** for bug reports or feature requests
- **Check existing issues** before creating new ones
- **Be specific** about problems or questions
- **Provide context** (OS, Python version, error messages)

## 📜 License

By contributing, you agree that your contributions will be licensed under the project's MIT License.

---

## 🎯 First-Time Contributors

Looking for your first contribution? Try these:

### Good First Issues
1. **Add a new search engine** (like StartPage, Ecosia)
2. **Improve error messages** for better user experience
3. **Add more emoji icons** for different content types
4. **Create installation script** for easier setup
5. **Add command aliases** (shortcuts for common commands)

### Getting Started Example
```python
# Example: Adding a simple command
def handle_command(self, cmd_line):
    parts = cmd_line.strip().split()
    if not parts:
        return False
    
    cmd = parts[0].lower()
    
    # Add your new command here
    if cmd == "ping":
        self.print_success("Pong! 🏓")
        return True
```

## 🤝 Code of Conduct

Please read and adhere to our [Code of Conduct](CODE_OF_CONDUCT.md). We're committed to providing a welcoming and respectful environment for all contributors.

---

Thank you for helping make NaviDuck better! Your contributions are valued and appreciated. 🦆💻

*Maintained by DAPOWER99*
