# NaviDuck 🦆

**A feature-packed CLI browser with built-in AI, privacy features, and real web search - all without BeautifulSoup!**

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![CLI](https://img.shields.io/badge/Interface-CLI-black.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

Tired of bloated browsers? NaviDuck brings web browsing to your terminal with style. Search the web, get AI answers, manage bookmarks, and browse privately - all from a clean, keyboard-first interface.
# Note From Developer:
**Right Now This Project Mostly Works on Windows**
---

## 📋 Table of Contents
- [✨ Features](#-features)
- [🚀 Quick Start](#-quick-start)
- [📖 Complete Usage Guide](#-complete-usage-guide)
- [🔧 Configuration](#-configuration)
- [🔍 Search Engines](#-search-engines)
- [🤖 NavAI Assistant](#-navai-assistant)
- [🛡️ Privacy & Tor](#️-privacy--tor)
- [🎨 Customization](#-customization)
- [🏗️ Architecture](#️-architecture)
- [🧪 Testing](#-testing)
- [🤝 Contributing](#-contributing)
- [📝 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)
- [📞 Contact](#-contact)

---

## ✨ Features

### 🔍 **Advanced Web Search**
- **Multiple Search Engines**: DuckDuckGo (HTML & API), Google, Wikipedia, Brave Search
- **Smart CAPTCHA Handling**: Automatic detection and engine switching
- **Real-time Parsing**: No mock data - actual live web results
- **Regex-Powered**: Zero dependencies on BeautifulSoup or heavy parsers
- **Fallback System**: If one engine fails, automatically tries alternatives

### 🤖 **Intelligent AI Assistant**
- **NavAI Integration**: Real web search for accurate answers
- **Conversational Interface**: Natural language processing for queries
- **Instant Answers**: Direct responses from DuckDuckGo API
- **Contextual Suggestions**: Smart follow-up recommendations
- **Query Understanding**: Identifies question types automatically

### 🛡️ **Privacy & Security Suite**
- **Built-in Tor Support**: One-click Tor activation
- **Proxy Configuration**: SOCKS5 proxy support
- **Privacy-Respecting**: No telemetry or data collection
- **Onion Routing**: Native `.onion` site support
- **Custom User-Agent**: Configurable browser fingerprint

### 🎨 **Beautiful Terminal Experience**
- **Dual Icon Themes**: Switch between Nerd Font icons and Emoji
- **Full ANSI Support**: Rich color schemes and text formatting
- **Responsive Layout**: Adapts to terminal window size
- **Keyboard-First Design**: Optimized for power users
- **Visual Feedback**: Loading indicators and progress bars

### 📚 **Smart Browser Features**
- **Bookmark Management**: Save, organize, and tag favorites
- **Browsing History**: Timeline-based history with search
- **Session Management**: Save and restore browsing sessions
- **Content Extraction**: Clean text extraction from web pages
- **Quick Navigation**: Shortcuts for common actions

### ⚡ **Performance & Reliability**
- **Lightweight**: Minimal memory footprint
- **Fast Startup**: Instant initialization
- **Robust Error Handling**: Graceful degradation
- **Connection Pooling**: Efficient network usage
- **Caching System**: Optional result caching

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+**
- `requests` library
- (Recommended) Nerd Font for optimal icon display
- (Optional) Tor for privacy features

### Installation

#### Method 1: Direct Download
```bash
# Clone the repository
git clone https://github.com/DAPOWER99/naviduck.git
cd naviduck

# Install required package
pip install requests

# Or Install Like This 
pip install -r requirements.txt

# Run NaviDuck
python main.py
```
# **For Users More Familiar To The Terminal Or Cmd(Command Prompt)**
```bash
# You Can Use A One Line Install 
git clone https://github.com/DAPOWER99/NaviDuck.git && cd NaviDuck && pip install -r requirements.txt && python naviduck.py
```
#### Method 2: Using pip (Coming Soon)
```bash
# Once published
pip install naviduck
naviduck
```

#### Method 3: Development Setup
```bash
# Clone and setup development environment
git clone https://github.com/DAPOWER99/naviduck.git
cd naviduck

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run in development mode
python main.py --debug
```

### System Requirements
- **RAM**: 128MB minimum, 256MB recommended
- **Storage**: 10MB for installation
- **Network**: Internet connection for web access
- **Terminal**: 80x24 minimum size

---

## 📖 Complete Usage Guide

### Basic Navigation

#### Starting the Browser
```bash
# Basic start
python main.py

# Start with specific search engine
python main.py --engine brave

# Start with Tor enabled
python main.py --tor

# Start in read-only mode
python main.py --readonly
```

#### Interactive Commands
```
┌─────────────────────────────────────────────────────────────┐
│                     NaviDuck Command Guide                   │
├─────────────────────────────────────────────────────────────┤
│ s [query]           Quick search with default engine        │
│ search [engine] [query] Search with specific engine         │
│ ai [question]       Ask NavAI a question                    │
│ go [url]            Open URL in NaviDuck                    │
│ open [url/#]        Open URL in system browser              │
│ history             View browsing history                   │
│ bookmarks           Manage bookmarks                        │
│ tor [start/stop]    Control Tor connection                  │
│ settings            Open settings menu                      │
│ engines             Manage search engines                   │
│ clear               Clear screen                            │
│ help                Show this help                          │
│ quit/exit/q         Exit NaviDuck                           │
└─────────────────────────────────────────────────────────────┘
```

### Search Examples

```bash
# Quick search (uses default engine)
s python programming tutorials

# Search with specific engine
search google machine learning algorithms
search wikipedia ancient rome
search ddg privacy tools
search brave open source projects

# Complex searches with operators
search google "python flask" site:github.com
```

### AI Interaction Examples

```bash
# General knowledge questions
ai what is quantum computing?
ai explain blockchain technology
ai who invented the world wide web?

# Technical questions
ai how to implement binary search in python?
ai what are REST API best practices?
ai difference between TCP and UDP

# Practical queries
ai current time in Tokyo
ai weather forecast for London
ai convert 100 USD to EUR
```

### URL Navigation

```bash
# Open websites
go https://github.com
go https://news.ycombinator.com
go https://en.wikipedia.org/wiki/Unix

# Open from search results
# After searching, type number (1-10) to open result
```

### Bookmark Management

```bash
# View bookmarks
bookmarks

# Bookmark current page
# While viewing a page, press 'b'

# Bookmark search result
# After search results, type 'b' to bookmark first result
```

### History Management

```bash
# View full history
history

# Search history
# Use arrow keys or type numbers to navigate

# Clear history (from settings)
settings -> Clear history
```

---

## 🔧 Configuration

### Configuration Files

NaviDuck stores configuration in `~/.naviduck_config.json`:
```json
{
  "default_engine": "brave",
  "use_emoji": false,
  "engines": {
    "ddg": true,
    "ddg_api": true,
    "google": true,
    "wikipedia": true,
    "brave": true
  },
  "tor_enabled": false,
  "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64 x64)...",
  "timeout": 10,
  "max_results": 10
}
```

### Data Storage

User data is stored in `~/.naviduck_data.json`:
```json
{
  "history": [...],
  "bookmarks": [...],
  "sessions": [...]
}
```

### Command-Line Arguments

```bash
# Full list of command-line options
python main.py --help

Options:
  --engine ENGINE    Set default search engine
  --tor              Start with Tor enabled
  --emoji            Use emoji icons instead of Nerd Font
  --config FILE      Use alternative config file
  --data FILE        Use alternative data file
  --timeout SECONDS  Set network timeout
  --debug            Enable debug mode
  --version          Show version information
```

### Environment Variables

```bash
# Set in shell profile (.bashrc, .zshrc, etc.)
export NAVIDUCK_ENGINE="google"
export NAVIDUCK_TOR="true"
export NAVIDUCK_TIMEOUT="15"
export NAVIDUCK_USER_AGENT="Custom Agent"
```

---

## 🔍 Search Engines

### Available Engines

| Engine | Type | Features | Privacy |
|--------|------|----------|---------|
| **Brave Search** | HTML | Fast, privacy-focused, no CAPTCHA | Excellent |
| **DuckDuckGo (HTML)** | HTML | No tracking, !bang commands | Excellent |
| **DuckDuckGo API** | JSON | Instant answers, structured data | Excellent |
| **Google** | HTML | Comprehensive results, advanced operators | Poor |
| **Wikipedia** | API | Encyclopedia articles, references | Good |

### Engine Configuration

Enable/disable engines from settings:
```bash
# In NaviDuck, type:
engines

# Then use:
enable 1    # Enable engine 1
disable 2   # Disable engine 2
set 3       # Set as default engine
```

### Custom Search Engines

Add custom engines by editing the `SEARCH_ENGINES` dictionary in the code:

```python
"custom_engine": {
    "name": "My Search",
    "url": "https://api.example.com/search",
    "params": {"q": "{query}", "format": "json"},
    "icon": "SEARCH",
    "requires_tor": False,
    "enabled": True,
    "type": "api"  # or "html"
}
```

---

## 🤖 NavAI Assistant

### How It Works

NavAI combines multiple techniques for intelligent responses:

1. **Instant Answer API**: Queries DuckDuckGo's Instant Answer API
2. **Web Search Integration**: Falls back to web search when needed
3. **Local Knowledge Base**: Common queries and greetings
4. **Context Awareness**: Remembers conversation context

### API Integration

```python
# Example of NavAI's internal workflow
def get_answer(question):
    # 1. Check local knowledge base
    if is_greeting(question):
        return get_greeting_response(question)
    
    # 2. Query DuckDuckGo Instant Answer
    ddg_answer = query_ddg_api(question)
    if ddg_answer:
        return format_answer(ddg_answer)
    
    # 3. Suggest web search
    return suggest_search(question)
```

### Extending NavAI

Add custom responses by modifying the `_handle_simple_queries` method:

```python
responses = {
    "hello": f"{self.icons['CHAT']} Hello! I'm NavAI...",
    "time": f"{self.icons['TIME']} Current time: {datetime.now()}",
    "joke": f"{self.icons['CHAT']} Why don't scientists trust atoms?...",
    # Add your own responses here
}
```

---

## 🛡️ Privacy & Tor

### Tor Integration

#### Setting Up Tor

```bash
# Windows (using Tor Browser)
# Tor should be at: D:\APPS&DATA\Tor Browser\Browser\TorBrowser\Tor\tor.exe **(this is a development path and will be changed in the future)**

# Linux
sudo apt install tor

# macOS
brew install tor
```

#### Using Tor in NaviDuck

```bash
# Start Tor from within NaviDuck
tor start

# Verify Tor status
tor

# Stop Tor
tor stop

# Browse with Tor
go http://example.onion
```

#### Manual Tor Configuration

```python
# Custom Tor settings in code
self.tor_dir = "/path/to/tor"
self.tor_exe = os.path.join(self.tor_dir, "tor")
self.tor_port = 9050
self.tor_data_dir = tempfile.mkdtemp()
```

### Privacy Features

1. **No Tracking**: NaviDuck doesn't track your searches or browsing
2. **Local Storage**: All data stays on your machine
3. **Configurable User-Agent**: Change how you appear to websites
4. **Proxy Support**: Route through custom proxies
5. **Data Encryption**: (Planned) Encrypted local storage

---

## 🎨 Customization

### Theme Configuration

#### Icon Themes
Toggle between Nerd Font and Emoji:
```bash
# In settings menu, option 3
settings -> Toggle icons
```

#### Color Schemes
Modify the `Colors` class for custom colors:
```python
class CustomColors:
    PROMPT = "\033[1;36m"  # Bright Cyan
    SUCCESS = "\033[1;32m" # Bright Green
    ERROR = "\033[1;31m"   # Bright Red
    # Add your own color codes
```

#### Layout Customization
Adjust display parameters:
```python
# In print_header function
width = 80  # Change header width
border_char = "━"  # Change border character
```

### Keyboard Shortcuts

| Key | Action | Context |
|-----|--------|---------|
| `Ctrl+C` | Cancel/Interrupt | Anywhere |
| `Enter` | Confirm/Select | Prompts |
| `q` | Back/Quit | Pages |
| `b` | Bookmark | Page view |
| `o` | Open in browser | Page view |
| `s` | Search related | Page view |
| `h` | History | Page view |

### Advanced Customization

#### Custom Parsers
Add parsing logic for new sites:
```python
def parse_custom_site(html):
    # Your parsing logic here
    return results
```

#### Plugin System
(Planned) Extend functionality with plugins:
```python
# Example plugin structure
class NaviDuckPlugin:
    def on_search(self, query, results):
        # Modify search results
        return enhanced_results
    
    def on_page_load(self, url, content):
        # Process page content
        return processed_content
```

---

## 🏗️ Architecture
👉 **[Click Here for More Information On The Architecture Of NaviDuck!](https://github.com/DAPOWER99/NaviDuck/wiki/Architecture)**
### Component Overview

```
┌─────────────────────────────────────────────────────────────┐
│                      NaviDuck Architecture                   │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │   UI     │  │  Search  │  │   Page   │  │    AI    │   │
│  │ Manager  │◄─┤ Manager  │◄─┤ Loader   │◄─┤ Assistant│   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│        │             │             │             │         │
│  ┌─────▼─────┐ ┌─────▼─────┐ ┌─────▼─────┐ ┌─────▼─────┐   │
│  │ Browser   │ │ Network   │ │   Tor     │ │   Data    │   │
│  │  State    │ │ Manager   │ │ Manager   │ │  Storage  │   │
│  └───────────┘ └───────────┘ └───────────┘ └───────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Core Components

1. **BrowserState**: Manages session data, settings, and state
2. **NetworkManager**: Handles HTTP requests with proxy support
3. **SearchManager**: Parses and processes search results
4. **PageLoader**: Loads and displays web pages
5. **UIManager**: Handles user interface and interaction
6. **NavAI**: Provides intelligent assistant functionality
7. **TorManager**: Manages Tor connection and routing

### Data Flow

```
User Input → UIManager → Command Routing
                            ↓
                    Search/Page Load/AI
                            ↓
                Network Requests (with Tor)
                            ↓
                Parsing/Processing
                            ↓
                Display/Response
```

### Error Handling

```python
try:
    # Main execution flow
    result = perform_action()
except ConnectionError:
    show_network_error()
except ParsingError:
    show_parsing_error()
except KeyboardInterrupt:
    handle_interrupt()
except Exception as e:
    log_error(e)
    show_fallback_ui()
```

---

## 🧪 Testing

### Running Tests

```bash
# Basic functionality tests
python -m pytest tests/

# Specific test categories
python -m pytest tests/test_search.py
python -m pytest tests/test_ai.py
python -m pytest tests/test_network.py

# With coverage report
python -m pytest --cov=naviduck tests/
```

### Test Categories

1. **Unit Tests**: Individual component testing
2. **Integration Tests**: Component interaction testing
3. **Network Tests**: Web request and parsing testing
4. **UI Tests**: User interface and interaction testing
5. **Performance Tests**: Speed and memory usage testing

### Manual Testing Checklist

- [ ] Search functionality with all engines
- [ ] AI question answering
- [ ] URL navigation
- [ ] Bookmark management
- [ ] History tracking
- [ ] Tor integration
- [ ] Settings configuration
- [ ] Error handling
- [ ] Keyboard shortcuts

---

## 🤝 Contributing

We love contributions! Here's how you can help:

### Ways to Contribute

1. **Report Bugs**: Open an issue with detailed bug reports
2. **Suggest Features**: Propose new features or improvements
3. **Write Code**: Submit pull requests with fixes or features
4. **Improve Documentation**: Help make docs better
5. **Test**: Try new versions and report issues

### Development Setup

```bash
# Fork and clone
git clone https://github.com/DAPOWER99/naviduck.git
cd naviduck

# Create feature branch
git checkout -b feature/amazing-feature

# Make changes and commit
git commit -m "Add amazing feature"

# Push and create PR
git push origin feature/amazing-feature
```

### Coding Standards

- Follow PEP 8 for Python code
- Use descriptive variable and function names
- Add docstrings to all functions
- Include tests for new features
- Update documentation when needed

### Pull Request Process

1. Update the README.md with details of changes if needed
2. Update the CHANGELOG.md with your changes
3. The PR will be merged once you have approval

### Feature Requests

Open an issue with:
- Use case description
- Expected behavior
- Proposed implementation (if any)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
### Third-Party Licenses

- **requests**: Apache License 2.0
- **Nerd Fonts**: MIT License
- **Tor Project**: BSD 3-Clause License

---

## 🙏 Acknowledgments

### Credits

- **Icon Design**: Nerd Fonts community for amazing icons
- **Search APIs**: DuckDuckGo, Google, Wikipedia, Brave
- **Inspiration**: Lynx browser, w3m, and other CLI tools
- **Testing**: All beta testers and contributors

### Special Thanks

- The open-source community for endless inspiration
- Everyone who reported bugs and suggested features
- Terminal enthusiasts who keep text-based interfaces alive

### Related Projects

- [Lynx](https://lynx.browser.org/) - Text web browser
- [w3m](https://w3m.sourceforge.net/) - Pager/text browser
- [Browsh](https://www.brow.sh/) - Modern text browser
- [Elinks](http://elinks.or.cz/) - Advanced text browser

---

## 📞 Contact

### Project Links

- **GitHub Repository**: [github.com/DAPOWER99/naviduck](https://github.com/DAPOWER99/naviduck)
- **Issue Tracker**: [github.com/DAPOWER99/naviduck/issues](https://github.com/DAPOWER99/naviduck/issues)
- **Discussion Forum**: [GitHub Discussions](https://github.com/DAPOWER99/naviduck/discussions)

### Support

- **Documentation**: This README and code comments
- **Community Help**: GitHub Discussions
- **Bug Reports**: GitHub Issues
- **Security Issues**: Please email directly (see GitHub profile)

### Stay Updated

- Star the repository on GitHub
- Watch for releases
- Join the discussion forum
- Follow updates on social media

---

## 🚀 What's Next?

### Planned Features
- [ ] Tabbed browsing support
- [ ] Download manager
- [ ] Plugin system
- [ ] Custom CSS for page styling
- [ ] JavaScript execution (limited)
- [ ] Password manager integration
- [ ] Sync across devices
- [ ] Voice control interface

### Version Roadmap

#### v1.0 (Current)
- Core browsing functionality
- Basic AI assistant
- Privacy features
- Multiple search engines

#### v2.0 (Planned)
- Plugin architecture
- Enhanced AI capabilities
- Better JavaScript support
- Performance optimizations

#### v3.0 (Future)
- Full extension support
- Advanced privacy tools
- Cloud sync
- Mobile terminal support

---

<div align="center">

**Made with ❤️ for the terminal community**

[![Star History Chart](https://api.star-history.com/svg?repos=DAPOWER99/naviduck&type=Date)](https://star-history.com/#DAPOWER99/naviduck&Date)

*If you enjoy NaviDuck, please consider giving it a ⭐ on GitHub!*


</div>












