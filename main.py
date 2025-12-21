#!/usr/bin/env python3
"""
NaviDuck - Enhanced CLI Browser with REAL AI & Working Search
With Emoji/Icon toggle setting - CAPTCHA Fixed Version
With Ctrl+X support for immediate quit
"""

import os
import sys
import json
import re
import time
import random
from datetime import datetime
from urllib.parse import quote, urlparse, parse_qs, unquote
import subprocess
import tempfile
import shutil
import signal
import atexit
import webbrowser
import threading

# ==================== COLOR CODES ====================
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    GRAY = "\033[90m"
    UNDERLINE = "\033[4m"

    PROMPT = CYAN + BOLD
    SUCCESS = GREEN + BOLD
    ERROR = RED + BOLD
    WARNING = YELLOW + BOLD
    INFO = BLUE + BOLD
    HIGHLIGHT = MAGENTA + BOLD
    URL = CYAN + UNDERLINE
    TITLE = GREEN + BOLD
    SELECTED = "\033[48;5;236m"  # Gray background


# ==================== ICON SETS ====================
class Icons:
    # Nerd Font Icons
    NERD = {
        # Browser & Navigation
        "BROWSER": "󰇯",      # nf-md-web
        "SEARCH": "󰍉",       # nf-md-magnify
        "HOME": "󰋜",         # nf-md-home
        "BACK": "󰁍",         # nf-md-arrow_left
        "FORWARD": "󰁔",      # nf-md-arrow_right
        "REFRESH": "󰔄",      # nf-md-refresh
        "EXTERNAL": "󰋝",     # nf-md-open_in_new
        "DOWNLOAD": "󰉉",     # nf-md-download
        
        # Content
        "PAGE": "󰈙",         # nf-md-file_document
        "LINK": "󰄷",         # nf-md-link
        "IMAGE": "󰉨",        # nf-md-image
        "VIDEO": "󰕧",        # nf-md-video
        "AUDIO": "󰋋",        # nf-md-music
        
        # Bookmarks & History
        "BOOKMARK": "󰆿",     # nf-md-bookmark
        "BOOKMARK_ADD": "󰆾", # nf-md-bookmark_plus
        "HISTORY": "󰋚",      # nf-md-history
        "STAR": "󰃀",         # nf-md-star
        "STAR_OUTLINE": "󰃁", # nf-md-star_outline
        
        # Status
        "SUCCESS": "󰱢",      # nf-md-check_circle
        "ERROR": "󰀦",        # nf-md-close_circle
        "WARNING": "󰀪",      # nf-md-alert_circle
        "INFO": "󰋼",         # nf-md-information
        "LOADING": "󰔛",      # nf-md-loading
        "QUESTION": "󰞃",     # nf-md-help_circle
        
        # Actions
        "SETTINGS": "󰒓",     # nf-md-cog
        "MENU": "󰍜",         # nf-md-menu
        "EDIT": "󰏫",         # nf-md-pencil
        "DELETE": "󰩹",       # nf-md-trash_can_outline
        "SAVE": "󰆓",         # nf-md-content_save
        "COPY": "󰆐",         # nf-md-content_copy
        
        # Security & Features
        "LOCK": "󰌾",         # nf-md-lock
        "UNLOCK": "󰌿",       # nf-md-lock_open
        "SHIELD": "󰝆",       # nf-md-shield
        "TOR": "󰙭",          # nf-md-tor
        "AI": "󰚩",           # nf-md-robot
        
        # Search Engines (Brand Icons)
        "DDG": "󰙯",          # Duck icon
        "GOOGLE": "󰡷",       # Google icon
        "WIKI": "󰗕",         # Wikipedia icon
        "BRAVE": "󰚥",        # Brave icon
        "BING": "󰊫",         # Bing icon
        "YAHOO": "󰇸",        # Yahoo icon
        "STARTPAGE": "󰋜",    # Home icon
        "GITHUB": "󰊤",       # GitHub icon
        
        # UI Elements
        "BULLET": "󰝥",       # nf-md-circle_small
        "DOT": "󰝥",          # nf-md-circle_small
        "CHECK": "󰄲",        # nf-md-check
        "PLUS": "󰐕",         # nf-md-plus
        "MINUS": "󰐖",        # nf-md-minus
        "CLOSE": "󰅖",        # nf-md-close
        "ARROW_RIGHT": "󰅂",  # nf-md-chevron_right
        "ARROW_DOWN": "󰅀",   # nf-md-chevron_down
        
        # Categories
        "CODE": "󰨞",         # nf-md-code_tags
        "FILE": "󰈔",         # nf-md-file
        "FOLDER": "󰉓",       # nf-md-folder
        "USER": "󰀉",         # nf-md-account
        "TIME": "󰔟",         # nf-md-clock
        
        # Communication
        "MAIL": "󰇮",         # nf-md-email
        "CHAT": "󰭻",         # nf-md-message
        "NOTIFICATION": "󱅫", # nf-md-bell
    }
    
    # Simple Emoji Icons
    EMOJI = {
        "BROWSER": "🌐",
        "SEARCH": "🔍",
        "HOME": "🏠",
        "BACK": "⬅",
        "FORWARD": "➡",
        "REFRESH": "🔄",
        "EXTERNAL": "📤",
        "DOWNLOAD": "💾",
        "PAGE": "📄",
        "LINK": "🔗",
        "IMAGE": "🖼️",
        "VIDEO": "🎥",
        "AUDIO": "🎵",
        "BOOKMARK": "📑",
        "BOOKMARK_ADD": "➕",
        "HISTORY": "🕰️",
        "STAR": "⭐",
        "STAR_OUTLINE": "☆",
        "SUCCESS": "✅",
        "ERROR": "❌",
        "WARNING": "⚠️",
        "INFO": "ℹ️",
        "LOADING": "🌀",
        "QUESTION": "❓",
        "SETTINGS": "⚙️",
        "MENU": "☰",
        "EDIT": "✏️",
        "DELETE": "🗑️",
        "SAVE": "💾",
        "COPY": "📋",
        "LOCK": "🔒",
        "UNLOCK": "🔓",
        "SHIELD": "🛡️",
        "TOR": "🧅",
        "AI": "🤖",
        "DDG": "🦆",
        "GOOGLE": "G",
        "WIKI": "📚",
        "BRAVE": "🦁",
        "BING": "B",
        "YAHOO": "Y!",
        "STARTPAGE": "🏠",
        "GITHUB": "🐙",
        "BULLET": "•",
        "DOT": "⚫",
        "CHECK": "✓",
        "PLUS": "➕",
        "MINUS": "➖",
        "CLOSE": "✕",
        "ARROW_RIGHT": "→",
        "ARROW_DOWN": "↓",
        "CODE": "</>",
        "FILE": "📁",
        "FOLDER": "📂",
        "USER": "👤",
        "TIME": "🕒",
        "MAIL": "📧",
        "CHAT": "💬",
        "NOTIFICATION": "🔔",
    }

# ==================== WORKING SEARCH ENGINES (NO BS4 REQUIRED) ====================
SEARCH_ENGINES = {
    "ddg": {
        "name": "DuckDuckGo",
        "url": "https://html.duckduckgo.com/html/",  # Changed from lite to html version
        "params": {"q": "{query}", "kl": "wt-wt"},
        "icon": "DDG",
        "requires_tor": False,
        "enabled": True,
        "type": "html"
    },
    "ddg_api": {
        "name": "DuckDuckGo API",
        "url": "https://api.duckduckgo.com/",
        "params": {"q": "{query}", "format": "json", "no_html": "1"},
        "icon": "DDG",
        "requires_tor": False,
        "enabled": True,
        "type": "api"
    },
    "google": {
        "name": "Google",
        "url": "https://www.google.com/search",
        "params": {"q": "{query}", "num": "10"},
        "icon": "GOOGLE",
        "requires_tor": False,
        "enabled": True,
        "type": "html"
    },
    "wikipedia": {
        "name": "Wikipedia",
        "url": "https://en.wikipedia.org/w/api.php",
        "params": {"action": "opensearch", "search": "{query}", "limit": "10", "format": "json"},
        "icon": "WIKI",
        "requires_tor": False,
        "enabled": True,
        "type": "api"
    },
    "brave": {
        "name": "Brave Search",
        "url": "https://search.brave.com/search",
        "params": {"q": "{query}", "source": "web"},
        "icon": "BRAVE",
        "requires_tor": False,
        "enabled": True,
        "type": "html"
    }
}

# ==================== GLOBAL FLAGS ====================
EXIT_FLAG = False
EXIT_LOCK = threading.Lock()

def set_exit_flag():
    """Set global exit flag"""
    global EXIT_FLAG
    with EXIT_LOCK:
        EXIT_FLAG = True

def get_exit_flag():
    """Get global exit flag"""
    global EXIT_FLAG
    with EXIT_LOCK:
        return EXIT_FLAG

def check_exit_flag():
    """Check and exit if flag is set"""
    if get_exit_flag():
        raise KeyboardInterrupt("Ctrl+X pressed")

# ==================== NAVAI - REAL AI ====================
class NavAI:
    """REAL AI that searches the web for answers"""
    
    def __init__(self, icons):
        import requests
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        self.conversation = []
        self.icons = icons
        
    def ask(self, question: str) -> str:
        """Get real answers by searching the web"""
        try:
            question = question.strip()
            
            # Check exit flag
            check_exit_flag()
            
            # Handle simple queries
            simple_response = self._handle_simple_queries(question)
            if simple_response:
                return simple_response
            
            # Check exit flag
            check_exit_flag()
            
            # Try DuckDuckGo Instant Answer API first
            ddg_answer = self._get_duckduckgo_answer(question)
            if ddg_answer and ddg_answer != "No answer found.":
                return ddg_answer
            
            # If no instant answer, suggest search
            return f"{self.icons['INFO']} I couldn't find a direct answer. Try: 'search {question}'"
            
        except KeyboardInterrupt:
            raise
        except Exception as e:
            return f"{self.icons['ERROR']} AI Error: {str(e)[:50]}"
    
    def _handle_simple_queries(self, query: str) -> str:
        """Handle greetings and simple queries"""
        query_lower = query.lower()
        
        responses = {
            "hello": f"{self.icons['CHAT']} Hello! I'm NavAI. How can I help you?",
            "hi": f"{self.icons['CHAT']} Hi there! What would you like to know?",
            "how are you": f"{self.icons['CHAT']} I'm functioning perfectly! Ready to help you search the web.",
            "what is your name": f"{self.icons['AI']} I'm NavAI, the AI assistant for NaviDuck browser!",
            "help": f"{self.icons['QUESTION']} I can help you search the web and answer questions. Try asking me anything!",
            "thank you": f"{self.icons['SUCCESS']} You're welcome! Happy to help.",
            "bye": f"{self.icons['SUCCESS']} Goodbye! Come back anytime.",
            "time": f"{self.icons['TIME']} Current time: {datetime.now().strftime('%H:%M:%S')}",
            "date": f"{self.icons['TIME']} Today is: {datetime.now().strftime('%Y-%m-%d')}",
            "who created you": f"{self.icons['AI']} I was created by DAPOWER99 on Github (Also Known As Dragon). Check out NaviDuck Here (https://github.com/DAPOWER99/NaviDuck)!",
            "who is your creator": f"{self.icons['AI']} I was created by DAPOWER99 on Github (Also Known As Dragon). Check out NaviDuck Here (https://github.com/DAPOWER99/NaviDuck)!",
            "what can you do": f"{self.icons['AI']} I can help you search the web, answer questions, and provide information using real-time data.",
            "what is naviduck": f"{self.icons['BROWSER']} NaviDuck is an enhanced CLI browser with working search engines and AI capabilities.",
            "what is your purpose": f"{self.icons['AI']} My purpose is to assist users in finding information quickly and efficiently using web searches and instant answers.",
            "who are you": f"{self.icons['AI']} I'm NavAI, your AI assistant integrated into the NaviDuck CLI browser.",
            "roll a dice": f"{self.icons['INFO']} You rolled a {random.randint(1, 6)}!",
            "flip a coin": f"{self.icons['INFO']} You got {'Heads' if random.randint(0, 1) == 0 else 'Tails'}!",
            "What's the weather": f"{self.icons['INFO']} I can't provide real-time weather updates yet. Try searching for 'weather in [your city]'.",
            "good morning": f"{self.icons['CHAT']} Good morning! How can I assist you today?"
        }
        
        for key, response in responses.items():
            if key in query_lower:
                return response
        
        return ""
    
    def _get_duckduckgo_answer(self, query: str) -> str:
        """Get answer from DuckDuckGo Instant Answer API"""
        try:
            url = "https://api.duckduckgo.com/"
            params = {
                "q": query,
                "format": "json",
                "no_html": "1",
                "skip_disambig": "1"
            }
            
            response = self.session.get(url, params=params, timeout=5)
            data = response.json()
            
            # Check exit flag
            check_exit_flag()
            
            # Check Abstract (direct answer)
            abstract = data.get("AbstractText", "").strip()
            if abstract and len(abstract) > 15:
                return f"{self.icons['INFO']} {abstract}"
            
            # Check Definition
            definition = data.get("Definition", "").strip()
            if definition and len(definition) > 15:
                return f"{self.icons['INFO']} Definition: {definition}"
            
            # Check Answer (for calculations, conversions)
            answer = data.get("Answer", "").strip()
            if answer and len(answer) > 5:
                return f"{self.icons['INFO']} {answer}"
            
            return "No answer found."
            
        except KeyboardInterrupt:
            raise
        except:
            return "No answer found."

# ==================== UTILITIES ====================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(text, color=Colors.TITLE, width=80):
    print(f"\n{color}{'━' * width}{Colors.RESET}")
    print(f"{color}{text.center(width)}{Colors.RESET}")
    print(f"{color}{'━' * width}{Colors.RESET}")

def print_box(text, title="", color=Colors.INFO):
    width = 70
    print(f"\n{color}╔{'═' * (width-2)}╗{Colors.RESET}")
    if title:
        print(f"{color}║ {title.center(width-4)} ║{Colors.RESET}")
        print(f"{color}╟{'─' * (width-2)}╢{Colors.RESET}")
    
    # Check exit flag
    check_exit_flag()
    
    # Wrap text
    lines = []
    words = text.split()
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= width - 4:
            current_line += " " + word if current_line else word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    
    for line in lines:
        print(f"{color}║ {line.ljust(width-4)} ║{Colors.RESET}")
    
    print(f"{color}╚{'═' * (width-2)}╝{Colors.RESET}")

def get_input(prompt="", default=""):
    if default:
        prompt_text = f"{Colors.PROMPT}{prompt} [{default}]: {Colors.RESET}"
    else:
        prompt_text = f"{Colors.PROMPT}{prompt}: {Colors.RESET}"
    
    try:
        result = input(prompt_text)
        # Check for Ctrl+X
        if result and result.strip() == "^X":
            set_exit_flag()
            raise KeyboardInterrupt("Ctrl+X pressed")
        return result if result else default
    except (KeyboardInterrupt, EOFError):
        set_exit_flag()
        raise

# ==================== BROWSER STATE ====================
class BrowserState:
    def __init__(self):
        self.use_emoji = False  # Default to Nerd Font icons
        self.icons = Icons.NERD
        self.history = []
        self.bookmarks = []
        self.current_results = []
        self.current_page = ""
        self.current_url = ""
        self.current_title = ""
        self.current_engine = "brave"  # Changed default to Brave to avoid CAPTCHA
        self.tor_enabled = False
        self.tor_process = None
        self.data_file = os.path.expanduser("~/.naviduck_data.json")
        self.config_file = os.path.expanduser("~/.naviduck_config.json")
        
        self.load_data()
        self.load_config()
        atexit.register(self.cleanup)
    
    def get_icon(self, icon_name):
        """Get icon based on current setting (emoji or nerd)"""
        if self.use_emoji:
            return Icons.EMOJI.get(icon_name, "?")
        else:
            return Icons.NERD.get(icon_name, "?")
    
    def load_config(self):
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    self.current_engine = config.get('default_engine', 'brave')
                    self.use_emoji = config.get('use_emoji', False)
                    
                    engine_states = config.get('engines', {})
                    for engine, enabled in engine_states.items():
                        if engine in SEARCH_ENGINES:
                            SEARCH_ENGINES[engine]['enabled'] = enabled
            except:
                pass
    
    def save_config(self):
        config = {
            'default_engine': self.state.current_engine,
            'use_emoji': self.state.use_emoji,
            'engines': {engine: SEARCH_ENGINES[engine]['enabled'] 
                       for engine in SEARCH_ENGINES}
        }
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
        except:
            pass
    
    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.history = data.get('history', [])
                    self.bookmarks = data.get('bookmarks', [])
            except:
                pass
    
    def save_data(self):
        data = {
            'history': self.history[-100:],
            'bookmarks': self.bookmarks,
        }
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except:
            pass
    
    def add_bookmark(self, title, url):
        """Add bookmark to list"""
        self.bookmarks.append({
            'title': title[:80],
            'url': url,
            'added': datetime.now().isoformat()
        })
        self.save_data()
        return True
    
    def cleanup(self):
        if self.tor_process:
            try:
                self.tor_process.terminate()
            except:
                pass

# ==================== NETWORK MANAGER ====================
class NetworkManager:
    def __init__(self, state):
        self.state = state
        try:
            import requests
            self.session = requests.Session()
            self.session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            })
        except ImportError:
            print(f"{Colors.ERROR}❌ requests library not installed!{Colors.RESET}")
            print(f"{Colors.INFO}Install with: pip install requests{Colors.RESET}")
            sys.exit(1)
    
    def get(self, url, use_tor=False, timeout=10):
        try:
            # Add random delay to avoid CAPTCHA
            time.sleep(random.uniform(0.5, 2.0))
            
            # Check exit flag
            check_exit_flag()
            
            proxies = self.get_tor_proxies() if use_tor else None
            response = self.session.get(url, proxies=proxies, timeout=timeout)
            response.raise_for_status()
            
            # Check exit flag
            check_exit_flag()
            
            return response
        except KeyboardInterrupt:
            raise
        except Exception as e:
            raise Exception(f"Failed to fetch {url}: {e}")
    
    def get_tor_proxies(self):
        if self.state.tor_enabled:
            return {
                'http': 'socks5h://127.0.0.1:9050',
                'https': 'socks5h://127.0.0.1:9050'
            }
        return None

# ==================== SIMPLE SEARCH MANAGER (NO BS4 REQUIRED) ====================
class SearchManager:
    def __init__(self, state, network):
        self.state = state
        self.network = network
    
    def search(self, query, engine=None):
        engine = engine or self.state.current_engine
        engine_config = SEARCH_ENGINES.get(engine, SEARCH_ENGINES["brave"])
        
        if not engine_config['enabled']:
            print(f"{Colors.ERROR}{self.state.get_icon('ERROR')} Search engine '{engine_config['name']}' is disabled{Colors.RESET}")
            print(f"{Colors.INFO}Enable it in settings (engines command){Colors.RESET}")
            return []
        
        print(f"{Colors.INFO}{self.state.get_icon('INFO')} Searching {engine_config['name']} for: {query}{Colors.RESET}")
        
        try:
            # Check exit flag
            check_exit_flag()
            
            params = {}
            for key, value in engine_config["params"].items():
                params[key] = value.format(query=quote(query))
            
            use_tor = engine_config["requires_tor"] and self.state.tor_enabled
            
            # Build URL with parameters
            url = engine_config["url"]
            if params:
                url += '?' + '&'.join([f"{k}={v}" for k, v in params.items()])
            
            response = self.network.get(url, use_tor=use_tor)
            
            # Check exit flag
            check_exit_flag()
            
            # Check for CAPTCHA
            if self._check_captcha(response.text):
                print(f"{Colors.WARNING}{self.state.get_icon('WARNING')} CAPTCHA detected! Switching to alternative engine...{Colors.RESET}")
                return self._fallback_search(query, engine)
            
            results = self.parse_results(response, engine, query)
            
            self.state.history.append({
                'type': 'search',
                'query': query,
                'engine': engine,
                'timestamp': datetime.now().isoformat(),
                'results': len(results)
            })
            
            self.state.save_data()
            self.state.current_results = results
            return results
            
        except KeyboardInterrupt:
            raise
        except Exception as e:
            print(f"{Colors.ERROR}{self.state.get_icon('ERROR')} Search failed: {e}{Colors.RESET}")
            return self._fallback_search(query, engine)
    
    def _check_captcha(self, html):
        """Check if the response contains CAPTCHA"""
        captcha_indicators = [
            "captcha", "CAPTCHA", "challenge", "duck", "squares",
            "Please complete", "confirm you are human", "bot detection"
        ]
        
        for indicator in captcha_indicators:
            if indicator.lower() in html.lower():
                return True
        return False
    
    def _fallback_search(self, query, failed_engine):
        """Try alternative search engines when one fails"""
        alternatives = {
            'ddg': ['brave', 'google', 'ddg_api'],
            'google': ['brave', 'ddg_api', 'wikipedia'],
            'brave': ['google', 'ddg_api', 'wikipedia'],
            'ddg_api': ['brave', 'google', 'wikipedia'],
            'wikipedia': ['brave', 'google', 'ddg_api']
        }
        
        if failed_engine in alternatives:
            for alt_engine in alternatives[failed_engine]:
                if SEARCH_ENGINES[alt_engine]['enabled']:
                    print(f"{Colors.INFO}{self.state.get_icon('INFO')} Trying {SEARCH_ENGINES[alt_engine]['name']}...{Colors.RESET}")
                    try:
                        return self.search(query, alt_engine)
                    except KeyboardInterrupt:
                        raise
                    except:
                        continue
        
        # Last resort: return empty results with suggestion
        print(f"{Colors.WARNING}{self.state.get_icon('WARNING')} All search engines failed. Try enabling Tor or use a different network.{Colors.RESET}")
        return []
    
    def parse_results(self, response, engine, query):
        """Simple parsing without BeautifulSoup"""
        results = []
        
        try:
            # Check exit flag
            check_exit_flag()
            
            if engine == "ddg":
                # Parse DuckDuckGo HTML version
                html = response.text
                
                # Extract results from DDG HTML
                # DDG HTML has results in <a class="result__url" ...> format
                pattern = r'<a[^>]*class="[^"]*result__url[^"]*"[^>]*href="([^"]+)"[^>]*>.*?<a[^>]*class="[^"]*result__title[^"]*"[^>]*>([^<]+)</a>'
                matches = re.findall(pattern, html, re.DOTALL)
                
                for url, title in matches[:10]:
                    if 'duckduckgo.com' not in url:
                        # Clean title
                        title = re.sub(r'<[^>]+>', '', title).strip()
                        results.append({
                            'title': title[:80],
                            'url': url,
                            'snippet': f"Result from DuckDuckGo for: {query}",
                            'engine': 'DuckDuckGo'
                        })
                
                # If no results found with first pattern, try alternative
                if not results:
                    # Try to find all links with snippets
                    links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>([^<]+)</a>', html)
                    for url, title in links[:15]:
                        if 'duckduckgo.com' not in url and len(title) > 10:
                            results.append({
                                'title': re.sub(r'<[^>]+>', '', title).strip()[:80],
                                'url': url if url.startswith('http') else f"https:{url}" if url.startswith('//') else f"https://{url}",
                                'snippet': f"Search result for: {query}",
                                'engine': 'DuckDuckGo'
                            })
            
            elif engine == "ddg_api":
                # Parse DuckDuckGo JSON API
                data = response.json()
                
                # Check exit flag
                check_exit_flag()
                
                # Get abstract/answer
                if data.get("AbstractText"):
                    results.append({
                        'title': data.get("Heading", "Answer"),
                        'url': data.get("AbstractURL", f"https://duckduckgo.com/?q={quote(query)}"),
                        'snippet': data["AbstractText"][:150],
                        'engine': 'DuckDuckGo API'
                    })
                
                # Get related topics
                for topic in data.get("RelatedTopics", []):
                    if "Text" in topic and "FirstURL" in topic:
                        results.append({
                            'title': topic["Text"].split(" - ")[0][:80],
                            'url': topic["FirstURL"],
                            'snippet': topic["Text"][:120],
                            'engine': 'DuckDuckGo API'
                        })
                
                # Get external links
                for result in data.get("Results", []):
                    results.append({
                        'title': result.get("Text", "Result")[:80],
                        'url': result.get("FirstURL", ""),
                        'snippet': result.get("Text", "")[:120],
                        'engine': 'DuckDuckGo API'
                    })
            
            elif engine == "wikipedia":
                try:
                    data = response.json()
                    if isinstance(data, list) and len(data) >= 4:
                        for i in range(min(len(data[1]), len(data[2]), len(data[3]))):
                            results.append({
                                'title': data[1][i],
                                'url': data[3][i],
                                'snippet': data[2][i][:120],
                                'engine': 'Wikipedia'
                            })
                except:
                    results.append({
                        'title': "View Wikipedia Search",
                        'url': f"https://en.wikipedia.org/wiki/Special:Search?search={quote(query)}",
                        'snippet': "Open Wikipedia search results",
                        'engine': 'Wikipedia'
                    })
            
            elif engine == "google":
                # Simple Google parsing
                html = response.text
                
                # Extract Google results (simplified)
                pattern = r'<div[^>]*class="[^"]*g[^"]*"[^>]*>.*?<a[^>]+href="([^"]+)"[^>]*>([^<]+)</a>'
                matches = re.findall(pattern, html, re.DOTALL)
                
                for url, title in matches[:10]:
                    # Clean Google redirect URLs
                    if url.startswith('/url?'):
                        url_match = re.search(r'q=([^&]+)', url)
                        if url_match:
                            url = unquote(url_match.group(1))
                    
                    if url and title and 'google.com' not in url:
                        # Try to get snippet
                        snippet_pattern = f'{re.escape(title)}.*?<div[^>]*class="[^"]*VwiC3b[^"]*"[^>]*>([^<]+)'
                        snippet_match = re.search(snippet_pattern, html, re.DOTALL)
                        snippet = snippet_match.group(1)[:120] if snippet_match else ""
                        
                        results.append({
                            'title': re.sub(r'<[^>]+>', '', title).strip()[:80],
                            'url': url,
                            'snippet': re.sub(r'<[^>]+>', '', snippet).strip(),
                            'engine': 'Google'
                        })
            
            elif engine == "brave":
                # Parse Brave Search
                html = response.text
                
                # Brave search results pattern
                pattern = r'<a[^>]+data-testid="[^"]*result-title[^"]*"[^>]+href="([^"]+)"[^>]*>(.*?)</a>'
                matches = re.findall(pattern, html, re.DOTALL)
                
                for url, title in matches[:10]:
                    if 'brave.com' not in url:
                        title = re.sub(r'<[^>]+>', '', title).strip()
                        if title:
                            results.append({
                                'title': title[:80],
                                'url': url,
                                'snippet': f"Result from Brave Search for: {query}",
                                'engine': 'Brave'
                            })
        
        except KeyboardInterrupt:
            raise
        except Exception as e:
            print(f"{Colors.ERROR}{self.state.get_icon('ERROR')} Parse error: {e}{Colors.RESET}")
        
        # If no results found, show search page
        if not results:
            results.append({
                'title': f"View {SEARCH_ENGINES[engine]['name']} Search Results",
                'url': response.url,
                'snippet': f"Search results for '{query}'",
                'engine': SEARCH_ENGINES[engine]['name']
            })
        
        return results[:10]

# ==================== PAGE LOADER ====================
class PageLoader:
    def __init__(self, state, network):
        self.state = state
        self.network = network
    
    def load_page(self, url, display=True):
        print(f"{Colors.INFO}{self.state.get_icon('INFO')} Loading: {url}{Colors.RESET}")
        
        try:
            # Check exit flag
            check_exit_flag()
            
            use_tor = url.endswith(".onion") or self.state.tor_enabled
            
            if display:
                # For display mode, get full content
                response = self.network.get(url, use_tor=use_tor)
                
                # Check exit flag
                check_exit_flag()
                
                content_type = response.headers.get('content-type', '').lower()
                
                if 'text/html' in content_type:
                    # Simple HTML parsing without BS4
                    html = response.text
                    
                    # Extract title
                    title_match = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE)
                    title = title_match.group(1) if title_match else url
                    
                    # Remove scripts and styles
                    content = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
                    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)
                    content = re.sub(r'<[^>]+>', ' ', content)
                    content = re.sub(r'\s+', ' ', content)[:2000]
                    
                else:
                    content = response.text[:2000]
                    title = url
                
                self.state.current_url = url
                self.state.current_title = title[:80]
                self.state.current_page = content
                
                self.state.history.append({
                    'type': 'visit',
                    'url': url,
                    'title': title[:80],
                    'timestamp': datetime.now().isoformat(),
                    'tor': use_tor
                })
                
                self.state.save_data()
                return {
                    'success': True,
                    'title': title,
                    'content': content,
                    'tor': use_tor
                }
            else:
                # Just open in browser
                self.state.current_url = url
                webbrowser.open(url)
                return {'success': True, 'opened_in_browser': True}
                
        except KeyboardInterrupt:
            raise
        except Exception as e:
            error_msg = f"Failed to load page: {e}"
            self.state.current_page = error_msg
            return {
                'error': error_msg,
                'content': error_msg
            }

# ==================== TOR MANAGER ====================
class TorManager:
    def __init__(self, state):
        self.state = state
        self.tor_process = None
        self.tor_data_dir = None
        self.tor_dir = r"D:\APPS&DATA\Tor Browser\Browser\TorBrowser\Tor"
        self.tor_exe = os.path.join(self.tor_dir, "tor.exe")
        
        self.ensure_tor_in_path()
    
    def ensure_tor_in_path(self):
        current_path = os.environ.get('PATH', '')
        if self.tor_dir not in current_path:
            os.environ['PATH'] = current_path + ';' + self.tor_dir
    
    def check_tor(self):
        if not os.path.exists(self.tor_exe):
            return False
        
        try:
            original_cwd = os.getcwd()
            os.chdir(self.tor_dir)
            
            result = subprocess.run(
                [self.tor_exe, "--version"],
                capture_output=True,
                text=True,
                timeout=5,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
            
            os.chdir(original_cwd)
            return result.returncode == 0
        except:
            return False
    
    def start_tor(self):
        if self.state.tor_enabled:
            print(f"{Colors.INFO}{self.state.get_icon('INFO')} Tor is already running{Colors.RESET}")
            return True
        
        if not self.check_tor():
            print(f"{Colors.ERROR}{self.state.get_icon('ERROR')} Tor is not installed or not in PATH{Colors.RESET}")
            print(f"{Colors.INFO}Expected at: {self.tor_exe}{Colors.RESET}")
            return False
        
        try:
            self.tor_data_dir = tempfile.mkdtemp(prefix="naviduck_tor_")
            
            original_cwd = os.getcwd()
            os.chdir(self.tor_dir)
            
            self.tor_process = subprocess.Popen(
                [self.tor_exe,
                 "--SocksPort", "9050",
                 "--DataDirectory", self.tor_data_dir,
                 "--Log", "notice stdout"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
            
            os.chdir(original_cwd)
            
            time.sleep(3)
            self.state.tor_enabled = True
            print(f"{Colors.SUCCESS}{self.state.get_icon('SUCCESS')} Tor started successfully{Colors.RESET}")
            return True
            
        except Exception as e:
            print(f"{Colors.ERROR}{self.state.get_icon('ERROR')} Failed to start Tor: {e}{Colors.RESET}")
            return False
    
    def stop_tor(self):
        if not self.state.tor_enabled:
            print(f"{Colors.INFO}{self.state.get_icon('INFO')} Tor is not running{Colors.RESET}")
            return True
        
        try:
            if self.tor_process:
                self.tor_process.terminate()
                self.tor_process.wait()
                self.tor_process = None
            
            if self.tor_data_dir and os.path.exists(self.tor_data_dir):
                shutil.rmtree(self.tor_data_dir)
            
            self.state.tor_enabled = False
            print(f"{Colors.SUCCESS}{self.state.get_icon('SUCCESS')} Tor stopped{Colors.RESET}")
            return True
            
        except Exception as e:
            print(f"{Colors.ERROR}{self.state.get_icon('ERROR')} Failed to stop Tor: {e}{Colors.RESET}")
            return False

# ==================== ENHANCED UI MANAGER ====================
class UIManager:
    def __init__(self, state, search_mgr, page_loader, tor_mgr):
        self.state = state
        self.search_mgr = search_mgr
        self.page_loader = page_loader
        self.tor_mgr = tor_mgr
        self.ai = NavAI(state.icons if state.use_emoji else Icons.NERD)
        self.last_results = []
        
        # Set up signal handlers
        signal.signal(signal.SIGINT, self.signal_handler)
        if hasattr(signal, 'SIGBREAK'):
            signal.signal(signal.SIGBREAK, self.signal_handler)
        
        # On Windows, also catch CTRL_C_EVENT and CTRL_BREAK_EVENT
        if os.name == 'nt':
            try:
                import win32api
                win32api.SetConsoleCtrlHandler(self.windows_ctrl_handler, True)
            except ImportError:
                pass
    
    def windows_ctrl_handler(self, event):
        """Handle Windows control events"""
        if event in [0, 1, 2]:  # CTRL_C_EVENT, CTRL_BREAK_EVENT, CTRL_CLOSE_EVENT
            set_exit_flag()
            return True  # Don't let default handler run
        return False
    
    def signal_handler(self, signum, frame):
        """Handle Unix signals"""
        set_exit_flag()
        print(f"\n{Colors.WARNING}Ctrl+X detected. Exiting...{Colors.RESET}")
    
    def print_error(self, message):
        print(f"{Colors.ERROR}{self.state.get_icon('ERROR')} {message}{Colors.RESET}")
    
    def print_success(self, message):
        print(f"{Colors.SUCCESS}{self.state.get_icon('SUCCESS')} {message}{Colors.RESET}")
    
    def print_warning(self, message):
        print(f"{Colors.WARNING}{self.state.get_icon('WARNING')} {message}{Colors.RESET}")
    
    def print_info(self, message):
        print(f"{Colors.INFO}{self.state.get_icon('INFO')} {message}{Colors.RESET}")
    
    def print_ai(self, message):
        print(f"{Colors.MAGENTA}{self.state.get_icon('AI')} {message}{Colors.RESET}")
    
    def show_banner(self):
        clear_screen()
        
        # Check exit flag
        check_exit_flag()
        
        icon_type = "Emoji" if self.state.use_emoji else "Nerd Font"
        
        banner = f"""
{Colors.TITLE}{'━' * 70}{Colors.RESET}
{Colors.HIGHLIGHT}{self.state.get_icon('BROWSER')}  NaviDuck Browser - Enhanced Version{Colors.RESET}
{Colors.INFO}  Smart CLI Browser with NavAI & Working Search{Colors.RESET}
{Colors.TITLE}{'━' * 70}{Colors.RESET}


{Colors.INFO}{self.state.get_icon('SEARCH')}  Default Engine: {Colors.HIGHLIGHT}{SEARCH_ENGINES[self.state.current_engine]['name']}{Colors.RESET}
{Colors.INFO}{self.state.get_icon('TOR')}  Tor: {Colors.HIGHLIGHT}{'ON' if self.state.tor_enabled else 'OFF'}{Colors.RESET}
{Colors.INFO}{self.state.get_icon('HISTORY')}  History: {Colors.HIGHLIGHT}{len(self.state.history)} entries{Colors.RESET}
{Colors.INFO}{self.state.get_icon('BOOKMARK')}  Bookmarks: {Colors.HIGHLIGHT}{len(self.state.bookmarks)} saved{Colors.RESET}
{Colors.INFO}{self.state.get_icon('AI')}  NavAI: {Colors.HIGHLIGHT}Ready{Colors.RESET}
{Colors.INFO}{self.state.get_icon('SETTINGS')}  Icons: {Colors.HIGHLIGHT}{icon_type}{Colors.RESET}
{Colors.INFO}{self.state.get_icon('WARNING')}  Press Ctrl+X or type ^X to quit immediately{Colors.RESET}
"""
        print(banner)
    
    def show_main_menu(self):
        self.show_banner()
        
        print(f"{Colors.INFO}╞{'═' * 70}╡{Colors.RESET}")
        print(f"{Colors.INFO} Quick Actions:{Colors.RESET}")
        print(f"{Colors.INFO}╞{'═' * 70}╡{Colors.RESET}")
        
        actions = [
            (f"{self.state.get_icon('SEARCH')}  Search", "search [query] or s [query]"),
            (f"{self.state.get_icon('AI')}  Ask NavAI", "ai [question]"),
            (f"{self.state.get_icon('PAGE')}  Open URL", "go [url]"),
            (f"{self.state.get_icon('EXTERNAL')}  Open Browser", "open [url or #]"),
            (f"{self.state.get_icon('HISTORY')}  History", "history"),
            (f"{self.state.get_icon('BOOKMARK')}  Bookmarks", "bookmarks"),
            (f"{self.state.get_icon('SETTINGS')}  Settings", "settings"),
            (f"{self.state.get_icon('TOR')}  Tor Control", "tor [start|stop]"),
            (f"{self.state.get_icon('QUESTION')}  Help", "help"),
            (f"{self.state.get_icon('CLOSE')}  Exit", "quit or ^X")
        ]
        
        for icon_text, command in actions:
            print(f"  {Colors.CYAN}{command:25}{Colors.RESET} {icon_text}")
        
        # Show recent searches
        recent = [h for h in self.state.history if h['type'] == 'search'][-3:]
        if recent:
            print(f"\n{Colors.INFO}{self.state.get_icon('HISTORY')}  Recent Searches:{Colors.RESET}")
            for entry in recent:
                engine_icon = self.state.get_icon(SEARCH_ENGINES[entry.get('engine', 'brave')]['icon'])
                print(f"  {engine_icon} {entry.get('query', '')[:40]}")
        
        print(f"\n{Colors.PROMPT}Type a command (try 'ai hello' or 's python'):{Colors.RESET}")
        print(f"{Colors.GRAY}Press Ctrl+X or type ^X to quit immediately{Colors.RESET}")
    
    def show_help(self):
        print_header("Help & Commands")
        
        commands = [
            ("s [query]", "Quick search", "Uses default engine"),
            ("search [engine] [query]", "Search with engine", "e.g., 'search google cats'"),
            ("ai [question]", "Ask NavAI", "Real AI using web search"),
            ("go [url]", "View page in NaviDuck", "Displays content here"),
            ("open [url or #]", "Open in system browser", "# opens from last results"),
            ("history", "Show browsing history", ""),
            ("bookmarks", "Manage bookmarks", "[add|delete|list]"),
            ("tor [start|stop]", "Control Tor connection", ""),
            ("settings", "Open settings menu", ""),
            ("engines", "Manage search engines", ""),
            ("clear", "Clear screen", ""),
            ("quit", "Exit NaviDuck", ""),
            ("^X or Ctrl+X", "Exit immediately", "Quits even during operations")
        ]
        
        print(f"\n{Colors.INFO}{self.state.get_icon('INFO')}  Available Commands:{Colors.RESET}")
        for cmd, desc, extra in commands:
            print(f"  {Colors.CYAN}{cmd:25}{Colors.RESET} {desc}")
            if extra:
                print(f"    {Colors.GRAY}{extra}{Colors.RESET}")
        
        print(f"\n{Colors.INFO}{self.state.get_icon('SEARCH')}  Search Examples:{Colors.RESET}")
        print(f"  {Colors.CYAN}s python tutorials{Colors.RESET}")
        print(f"  {Colors.CYAN}search wikipedia machine learning{Colors.RESET}")
        print(f"  {Colors.CYAN}ai what is python{Colors.RESET}")
        print(f"  {Colors.CYAN}go https://example.com{Colors.RESET}")
        print(f"  {Colors.CYAN}open https://github.com{Colors.RESET}")
        print(f"  {Colors.CYAN}open 1 (opens 1st result from last search){Colors.RESET}")
        print(f"\n{Colors.WARNING}{self.state.get_icon('WARNING')}  Quick Exit:{Colors.RESET}")
        print(f"  {Colors.CYAN}Press Ctrl+X{Colors.RESET} or {Colors.CYAN}type ^X{Colors.RESET} to quit immediately, even during searches or page loads")
    
    def show_results(self, results):
        """Show search results and allow selection"""
        if not results:
            self.print_warning("No results found")
            return None
        
        # Store results for later use
        self.last_results = results
        
        print_header(f"{self.state.get_icon('SEARCH')}  Search Results ({len(results)} found)")
        
        for i, result in enumerate(results[:10], 1):
            # Check exit flag
            check_exit_flag()
            
            engine_icon = self.state.get_icon(result.get('engine', 'SEARCH'))
            title = result['title']
            url_display = result['url'][:60] + ("..." if len(result['url']) > 60 else "")
            
            print(f"{Colors.CYAN}{i:2d}.{Colors.RESET} {engine_icon} {title}")
            print(f"     {Colors.URL}{url_display}{Colors.RESET}")
            if result.get('snippet'):
                print(f"     {Colors.GRAY}{result['snippet']}{Colors.RESET}")
            
            if i < min(10, len(results)):
                print(f"     {Colors.GRAY}{'─' * 60}{Colors.RESET}")
        
        # Interactive selection
        while True:
            # Check exit flag
            check_exit_flag()
            
            print(f"\n{Colors.INFO}{self.state.get_icon('LINK')}  Select an option:{Colors.RESET}")
            print(f"  {Colors.CYAN}1-{min(10, len(results))}{Colors.RESET} - Open result in NaviDuck")
            print(f"  {Colors.CYAN}o1-o{min(10, len(results))}{Colors.RESET} - Open result in browser")
            print(f"  {Colors.CYAN}b{Colors.RESET} - Bookmark first result")
            print(f"  {Colors.CYAN}Enter{Colors.RESET} - Return to search")
            print(f"  {Colors.CYAN}^X{Colors.RESET} - Quit immediately")
            
            choice = get_input("Your choice")
            
            if choice is None:  # Ctrl+X was pressed
                raise KeyboardInterrupt("Ctrl+X pressed")
            
            if not choice:
                return None
            
            choice = choice.lower().strip()
            
            if choice == 'b':
                # Bookmark first result
                if results:
                    self.state.add_bookmark(results[0]['title'], results[0]['url'])
                    self.print_success(f"Bookmarked: {results[0]['title'][:40]}")
                return None
            
            elif choice.startswith('o') and len(choice) > 1:
                # Open specific result in browser (e.g., o1, o2, etc.)
                try:
                    idx_str = choice[1:]
                    idx = int(idx_str) - 1
                    if 0 <= idx < len(results):
                        url = results[idx]['url']
                        webbrowser.open(url)
                        self.print_success(f"Opening in browser: {url[:50]}")
                        return None
                    else:
                        self.print_error(f"Please enter o1-o{min(10, len(results))}")
                except ValueError:
                    self.print_error(f"Please enter o1-o{min(10, len(results))}")
            
            else:
                # Regular number selection (open in NaviDuck)
                try:
                    idx = int(choice) - 1
                    if 0 <= idx < len(results):
                        return results[idx]
                    else:
                        self.print_error(f"Please enter 1-{min(10, len(results))}")
                except ValueError:
                    self.print_error("Please enter a valid number or command")
    
    def show_page(self, page_data):
        """Show webpage content in a nice format"""
        if 'error' in page_data:
            self.print_error(page_data['error'])
            return
        
        print_header(f"{self.state.get_icon('PAGE')}  {page_data.get('title', 'Page Content')}")
        
        print(f"{Colors.INFO}{self.state.get_icon('LINK')}  URL: {Colors.URL}{self.state.current_url}{Colors.RESET}")
        if page_data.get('tor'):
            print(f"{Colors.INFO}{self.state.get_icon('TOR')}  Loaded via Tor{Colors.RESET}")
        
        print_box(
            page_data.get('content', 'No content available'),
            title="Page Content",
            color=Colors.INFO
        )
        
        # Actions menu
        print(f"\n{Colors.INFO}{self.state.get_icon('MENU')}  Page Actions:{Colors.RESET}")
        actions = [
            ("b", "Bookmark this page"),
            ("o", "Open in browser"),
            ("s", "Search related"),
            ("h", "Back to history"),
            ("q", "Return to main"),
            ("^X", "Quit immediately")
        ]
        
        for key, desc in actions:
            print(f"  {Colors.CYAN}{key}{Colors.RESET} - {desc}")
        
        while True:
            # Check exit flag
            check_exit_flag()
            
            choice = get_input("Action")
            
            if choice is None:  # Ctrl+X was pressed
                raise KeyboardInterrupt("Ctrl+X pressed")
            
            if not choice:
                break
                
            choice = choice.lower()
            
            if choice == 'b':
                title = get_input("Bookmark title", page_data.get('title', 'Untitled'))
                if title:
                    self.state.add_bookmark(title, self.state.current_url)
                    self.print_success("Bookmarked!")
                break
            
            elif choice == 'o':
                webbrowser.open(self.state.current_url)
                self.print_success("Opened in browser")
                break
            
            elif choice == 's':
                related = get_input("Search for related content")
                if related:
                    results = self.search_mgr.search(related, self.state.current_engine)
                    selected = self.show_results(results)
                    if selected:
                        page_data = self.page_loader.load_page(selected['url'], display=True)
                        if page_data and 'success' in page_data:
                            self.show_page(page_data)
                break
            
            elif choice == 'h':
                self.show_history()
                break
            
            elif choice in ['q', '']:
                break
            
            else:
                self.print_error("Invalid choice")
    
    def show_history(self):
        if not self.state.history:
            self.print_info("No browsing history")
            return
        
        print_header(f"{self.state.get_icon('HISTORY')}  Browsing History")
        
        items = []
        for i, entry in enumerate(reversed(self.state.history[-15:]), 1):
            # Check exit flag
            check_exit_flag()
            
            time_str = entry['timestamp'][11:16]
            date_str = entry['timestamp'][:10]
            
            if entry['type'] == 'search':
                icon = self.state.get_icon('SEARCH')
                engine_icon = self.state.get_icon(SEARCH_ENGINES[entry.get('engine', 'brave')]['icon'])
                text = f"{entry.get('query', '')[:40]}"
                items.append(f"{icon} {engine_icon} {text}")
                print(f"{Colors.CYAN}{i:2d}.{Colors.RESET} {icon} {engine_icon} {text}")
            else:
                icon = self.state.get_icon('PAGE')
                text = entry.get('title', entry.get('url', '')[:40])
                items.append(f"{icon} {text}")
                print(f"{Colors.CYAN}{i:2d}.{Colors.RESET} {icon} {text}")
            
            print(f"     {Colors.GRAY}{date_str} {time_str}{Colors.RESET}")
            
            if i < min(15, len(self.state.history)):
                print(f"     {Colors.GRAY}{'─' * 50}{Colors.RESET}")
        
        # Allow selection
        choice = get_input(f"Open item (1-{min(15, len(self.state.history))}) or Enter to return")
        if choice is None:  # Ctrl+X was pressed
            raise KeyboardInterrupt("Ctrl+X pressed")
        
        if choice:
            try:
                idx = int(choice) - 1
                history_idx = len(self.state.history) - 1 - idx
                if 0 <= history_idx < len(self.state.history):
                    entry = self.state.history[history_idx]
                    if entry['type'] == 'search':
                        results = self.search_mgr.search(entry.get('query', ''), entry.get('engine', 'brave'))
                        selected = self.show_results(results)
                        if selected:
                            page_data = self.page_loader.load_page(selected['url'], display=True)
                            if page_data and 'success' in page_data:
                                self.show_page(page_data)
                    elif entry['type'] == 'visit':
                        page_data = self.page_loader.load_page(entry['url'], display=True)
                        if page_data and 'success' in page_data:
                            self.show_page(page_data)
            except:
                self.print_error("Invalid selection")
    
    def handle_ai_query(self, query):
        """Handle AI queries"""
        print_header(f"{self.state.get_icon('AI')}  NavAI")
        
        response = self.ai.ask(query)
        print_box(response, title="NavAI Response", color=Colors.MAGENTA)
        
        # Suggest follow-up
        print(f"\n{Colors.INFO}{self.state.get_icon('SEARCH')}  Try searching for more information:{Colors.RESET}")
        print(f"  {Colors.CYAN}search {query}{Colors.RESET}")
        
        choice = get_input("Search for this? (y/N)", "n")
        
        if choice is None:  # Ctrl+X was pressed
            raise KeyboardInterrupt("Ctrl+X pressed")
            
        choice = choice.lower()
        
        if choice == 'y':
            results = self.search_mgr.search(query, self.state.current_engine)
            selected = self.show_results(results)
            if selected:
                page_data = self.page_loader.load_page(selected['url'], display=True)
                if page_data and 'success' in page_data:
                    self.show_page(page_data)
    
    def show_settings(self):
        """Show settings menu with icon toggle option"""
        print_header(f"{self.state.get_icon('SETTINGS')}  Settings")
        
        print(f"\n{Colors.INFO}Current Configuration:{Colors.RESET}")
        print(f"  {self.state.get_icon('SEARCH')}  Default Engine: {Colors.HIGHLIGHT}{SEARCH_ENGINES[self.state.current_engine]['name']}{Colors.RESET}")
        print(f"  {self.state.get_icon('TOR')}  Tor: {Colors.HIGHLIGHT}{'ON' if self.state.tor_enabled else 'OFF'}{Colors.RESET}")
        print(f"  {self.state.get_icon('SETTINGS')}  Icons: {Colors.HIGHLIGHT}{'Emoji' if self.state.use_emoji else 'Nerd Font'}{Colors.RESET}")
        
        print(f"\n{Colors.INFO}Options:{Colors.RESET}")
        print(f"  1. Change default search engine")
        print(f"  2. Manage search engines")
        print(f"  3. Toggle icons (Emoji/Nerd Font)")
        print(f"  4. Clear history")
        print(f"  5. Clear bookmarks")
        print(f"  6. Back to main")
        
        choice = get_input("Select option")
        
        if choice is None:  # Ctrl+X was pressed
            raise KeyboardInterrupt("Ctrl+X pressed")
        
        if choice == '1':
            self.change_default_engine()
        elif choice == '2':
            self.show_engines()
        elif choice == '3':
            self.toggle_icons()
        elif choice == '4':
            confirm = get_input("Clear all history? (y/N)", "n")
            if confirm and confirm.lower() == 'y':
                self.state.history = []
                self.state.save_data()
                self.print_success("History cleared")
        elif choice == '5':
            confirm = get_input("Clear all bookmarks? (y/N)", "n")
            if confirm and confirm.lower() == 'y':
                self.state.bookmarks = []
                self.state.save_data()
                self.print_success("Bookmarks cleared")
        elif choice == '6':
            return
    
    def toggle_icons(self):
        """Toggle between emoji and nerd font icons"""
        current = "Emoji" if self.state.use_emoji else "Nerd Font"
        new = "Nerd Font" if self.state.use_emoji else "Emoji"
        
        print(f"\n{Colors.INFO}Current icon style: {Colors.HIGHLIGHT}{current}{Colors.RESET}")
        print(f"{Colors.INFO}New icon style: {Colors.HIGHLIGHT}{new}{Colors.RESET}")
        
        choice = get_input(f"Switch to {new} icons? (y/N)", "n")
        if choice and choice.lower() == 'y':
            self.state.use_emoji = not self.state.use_emoji
            self.ai.icons = Icons.EMOJI if self.state.use_emoji else Icons.NERD
            self.state.save_config()
            self.print_success(f"Switched to {new} icons")
            self.show_banner()
    
    def handle_command(self, cmd_line):
        parts = cmd_line.strip().split()
        if not parts:
            return False
        
        cmd = parts[0].lower()
        args = parts[1:]
        
        # Check for Ctrl/X command
        if cmd == "^x" or cmd_line.strip() == "^X":
            print(f"\n{Colors.WARNING}Exiting immediately...{Colors.RESET}")
            return False
        
        # Handle AI queries
        if cmd == "ai":
            if not args:
                self.print_error("Usage: ai [question]")
                self.print_info("Example: ai what is python?")
                return True
            
            query = " ".join(args)
            self.handle_ai_query(query)
            return True
        
        # Handle quick search
        elif cmd == "s":
            if not args:
                self.print_error("Usage: s [query]")
                return True
            
            query = " ".join(args)
            results = self.search_mgr.search(query, self.state.current_engine)
            selected = self.show_results(results)
            if selected:
                page_data = self.page_loader.load_page(selected['url'], display=True)
                if page_data and 'success' in page_data:
                    self.show_page(page_data)
            return True
        
        elif cmd == "search":
            if not args:
                self.print_error("Usage: search [engine] query")
                return True
            
            engine = self.state.current_engine
            query_parts = args
            
            if args[0] in SEARCH_ENGINES:
                engine = args[0]
                query_parts = args[1:]
            
            if not query_parts:
                self.print_error("Please enter a search query")
                return True
            
            query = " ".join(query_parts)
            results = self.search_mgr.search(query, engine)
            selected = self.show_results(results)
            if selected:
                page_data = self.page_loader.load_page(selected['url'], display=True)
                if page_data and 'success' in page_data:
                    self.show_page(page_data)
            return True
        
        elif cmd == "go":
            if not args:
                self.print_error("Usage: go [url]")
                return True
            
            url = args[0]
            if not url.startswith(("http://", "https://")):
                url = "https://" + url
            
            page_data = self.page_loader.load_page(url, display=True)
            if 'error' in page_data:
                self.print_error(page_data['error'])
            else:
                self.show_page(page_data)
            return True
        
        elif cmd == "open":
            if not args:
                self.print_error("Usage: open [url or number]")
                self.print_info("Examples: open https://example.com")
                self.print_info("          open 1 (opens first result from last search)")
                return True
            
            target = args[0]
            
            # Check if it's a number (to open from last results)
            if target.isdigit():
                idx = int(target) - 1
                if 0 <= idx < len(self.last_results):
                    url = self.last_results[idx]['url']
                    webbrowser.open(url)
                    self.print_success(f"Opening in browser: {url[:50]}")
                else:
                    self.print_error(f"No result #{target} found from last search")
                    if self.last_results:
                        self.print_info(f"Last search had {len(self.last_results)} results")
            else:
                # It's a URL
                url = target
                if not url.startswith(("http://", "https://")):
                    url = "https://" + url
                
                webbrowser.open(url)
                self.print_success(f"Opening in browser: {url[:50]}")
            return True
        
        elif cmd == "history":
            self.show_history()
            return True
        
        elif cmd == "bookmarks":
            if not self.state.bookmarks:
                self.print_info("No bookmarks saved")
                return True
            
            print_header(f"{self.state.get_icon('BOOKMARK')}  Bookmarks")
            for i, bm in enumerate(self.state.bookmarks, 1):
                print(f"{Colors.CYAN}{i:2d}.{Colors.RESET} {self.state.get_icon('BOOKMARK')} {bm['title']}")
                print(f"     {Colors.GRAY}{bm['url']}{Colors.RESET}")
            
            choice = get_input(f"Open bookmark (1-{len(self.state.bookmarks)}) or Enter to return")
            if choice is None:  # Ctrl+X was pressed
                raise KeyboardInterrupt("Ctrl+X pressed")
            
            if choice:
                try:
                    idx = int(choice) - 1
                    if 0 <= idx < len(self.state.bookmarks):
                        page_data = self.page_loader.load_page(self.state.bookmarks[idx]['url'], display=True)
                        if 'error' in page_data:
                            self.print_error(page_data['error'])
                        else:
                            self.show_page(page_data)
                except:
                    self.print_error("Invalid selection")
            return True
        
        elif cmd == "tor":
            if not args:
                print(f"{Colors.INFO}Tor is {'ON' if self.state.tor_enabled else 'OFF'}{Colors.RESET}")
                return True
            
            subcmd = args[0].lower()
            if subcmd == "start":
                self.tor_mgr.start_tor()
            elif subcmd == "stop":
                self.tor_mgr.stop_tor()
            else:
                self.print_error("Usage: tor [start|stop]")
            return True
        
        elif cmd == "settings":
            self.show_settings()
            return True
        
        elif cmd == "engines":
            self.show_engines()
            return True
        
        elif cmd == "clear":
            clear_screen()
            self.show_main_menu()
            return True
        
        elif cmd == "help":
            self.show_help()
            return True
        
        elif cmd in ["quit", "exit", "q", ":q", "^x", "^X"]:
            print(f"\n{Colors.SUCCESS}{self.state.get_icon('SUCCESS')}  Goodbye!{Colors.RESET}")
            self.state.save_data()
            self.state.save_config()
            return False
        
        else:
            # Try as a direct query (search or AI)
            query = cmd_line.strip()
            if query:
                # Check for Ctrl/X
                if query == "^X" or query == "^x":
                    print(f"\n{Colors.WARNING}Exiting immediately...{Colors.RESET}")
                    return False
                
                # Check if it's likely an AI question
                ai_indicators = ["what", "how", "why", "when", "where", "who", "explain", "tell me", "?"]
                if any(indicator in query.lower() for indicator in ai_indicators):
                    self.handle_ai_query(query)
                else:
                    # Default to search
                    results = self.search_mgr.search(query, self.state.current_engine)
                    selected = self.show_results(results)
                    if selected:
                        page_data = self.page_loader.load_page(selected['url'], display=True)
                        if page_data and 'success' in page_data:
                            self.show_page(page_data)
                return True
            else:
                self.print_error(f"Unknown command: {cmd}")
                self.print_info("Type 'help' for available commands")
                return True
    
    def change_default_engine(self):
        print_header("Change Default Search Engine")
        
        enabled_engines = [(e, config) for e, config in SEARCH_ENGINES.items() if config['enabled']]
        for i, (engine, config) in enumerate(enabled_engines, 1):
            icon = self.state.get_icon(config['icon'])
            current = " (current)" if engine == self.state.current_engine else ""
            print(f"{i}. {icon} {config['name']}{current}")
        
        try:
            idx = int(get_input(f"Select engine (1-{len(enabled_engines)})")) - 1
            if 0 <= idx < len(enabled_engines):
                engine, config = enabled_engines[idx]
                self.state.current_engine = engine
                self.state.save_config()
                self.print_success(f"Default engine set to: {config['name']}")
        except:
            self.print_error("Invalid selection")
    
    def show_engines(self):
        print_header(f"{self.state.get_icon('SEARCH')}  Search Engine Management")
        
        engines = list(SEARCH_ENGINES.keys())
        
        print(f"\n{Colors.INFO}Enabled engines marked with {self.state.get_icon('SUCCESS')}{Colors.RESET}")
        for i, engine in enumerate(engines, 1):
            config = SEARCH_ENGINES[engine]
            icon = self.state.get_icon(config['icon'])
            enabled = self.state.get_icon('SUCCESS') if config['enabled'] else " "
            default = " (default)" if engine == self.state.current_engine else ""
            
            print(f"  {Colors.CYAN}{i:2d}.{Colors.RESET} {enabled} {icon} {config['name']}{default}")
        
        print(f"\n{Colors.INFO}Commands:{Colors.RESET}")
        print(f"  {Colors.CYAN}enable [num]{Colors.RESET} - Enable engine")
        print(f"  {Colors.CYAN}disable [num]{Colors.RESET} - Disable engine")
        print(f"  {Colors.CYAN}set [num]{Colors.RESET} - Set as default")
        print(f"  {Colors.CYAN}back{Colors.RESET} - Return")
        
        while True:
            # Check exit flag
            check_exit_flag()
            
            cmd = get_input("\nengines>")
            if cmd is None:  # Ctrl+X was pressed
                raise KeyboardInterrupt("Ctrl+X pressed")
            
            if not cmd:
                continue
            
            parts = cmd.split()
            if not parts:
                continue
            
            action = parts[0].lower()
            
            if action == "back":
                break
            
            elif action == "enable" and len(parts) > 1:
                try:
                    idx = int(parts[1]) - 1
                    if 0 <= idx < len(engines):
                        engine = engines[idx]
                        SEARCH_ENGINES[engine]['enabled'] = True
                        self.state.save_config()
                        self.print_success(f"{SEARCH_ENGINES[engine]['name']} enabled")
                        self.show_engines()
                        break
                except:
                    self.print_error("Invalid number")
            
            elif action == "disable" and len(parts) > 1:
                try:
                    idx = int(parts[1]) - 1
                    if 0 <= idx < len(engines):
                        engine = engines[idx]
                        if engine == self.state.current_engine:
                            self.print_error("Cannot disable default engine")
                        else:
                            SEARCH_ENGINES[engine]['enabled'] = False
                            self.state.save_config()
                            self.print_success(f"{SEARCH_ENGINES[engine]['name']} disabled")
                            self.show_engines()
                            break
                except:
                    self.print_error("Invalid number")
            
            elif action == "set" and len(parts) > 1:
                try:
                    idx = int(parts[1]) - 1
                    if 0 <= idx < len(engines):
                        engine = engines[idx]
                        if not SEARCH_ENGINES[engine]['enabled']:
                            self.print_error("Engine must be enabled first")
                        else:
                            self.state.current_engine = engine
                            self.state.save_config()
                            self.print_success(f"Default engine set to: {SEARCH_ENGINES[engine]['name']}")
                            self.show_engines()
                            break
                except:
                    self.print_error("Invalid number")
            
            else:
                self.print_error("Unknown command")
    
    def run(self):
        self.show_main_menu()
        
        while True:
            try:
                # Check exit flag
                if get_exit_flag():
                    print(f"\n{Colors.WARNING}Exiting...{Colors.RESET}")
                    break
                
                cmd = get_input(f"{Colors.PROMPT}{self.state.get_icon('BROWSER')} naviduck>{Colors.RESET}")
                if cmd is None:  # Ctrl+X was pressed
                    print(f"\n{Colors.WARNING}Exiting...{Colors.RESET}")
                    break
                
                if not self.handle_command(cmd):
                    break
                
                print(f"\n{Colors.GRAY}{'─' * 70}{Colors.RESET}")
                
            except KeyboardInterrupt:
                if get_exit_flag():
                    print(f"\n{Colors.WARNING}Exiting immediately...{Colors.RESET}")
                    break
                else:
                    print(f"\n{Colors.WARNING}Use 'quit' or Ctrl+X to exit.{Colors.RESET}")
            except Exception as e:
                self.print_error(f"Unexpected error: {e}")

# ==================== MAIN ====================
def main():
    print(f"{Colors.INFO}🌐  Starting NaviDuck Enhanced...{Colors.RESET}")
    print(f"{Colors.WARNING}⚠️  Press Ctrl+X at any time to quit immediately{Colors.RESET}")
    
    # Check for required packages
    try:
        import requests
    except ImportError:
        print(f"{Colors.ERROR}❌ requests library not installed!{Colors.RESET}")
        print(f"{Colors.INFO}Install with: pip install requests{Colors.RESET}")
        sys.exit(1)
    
    # Create browser components
    state = BrowserState()
    network = NetworkManager(state)
    search_mgr = SearchManager(state, network)
    page_loader = PageLoader(state, network)
    tor_mgr = TorManager(state)
    ui = UIManager(state, search_mgr, page_loader, tor_mgr)
    
    # Run the application
    try:
        ui.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}Exiting immediately...{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.ERROR}❌ Fatal error: {e}{Colors.RESET}")
        sys.exit(1)
    
    # Cleanup
    try:
        state.save_data()
        state.save_config()
        print(f"{Colors.SUCCESS}✅  Goodbye!{Colors.RESET}")
    except:
        pass

if __name__ == "__main__":
    main()