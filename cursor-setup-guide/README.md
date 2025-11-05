# Cursor IDE Setup Guide

Complete setup guide for Cursor IDE with all necessary dependencies, extensions, and ready-to-use code examples.

## Table of Contents

1. [Cursor IDE Installation](#cursor-ide-installation)
2. [Essential Dependencies](#essential-dependencies)
3. [Git and GitHub Setup](#git-and-github-setup)
4. [Required Extensions](#required-extensions)
5. [Useful Tools and Packages](#useful-tools-and-packages)
6. [Premade Packages](./premade-packages/README.md)
7. [Docker Container Setup](#docker-container-setup)
8. [Quick Setup Checklist](#quick-setup-checklist)

---

## Cursor IDE Installation

### Download Cursor

- **Official Website**: [https://cursor.sh](https://cursor.sh)
- **Direct Download**: [https://cursor.sh/download](https://cursor.sh/download)
- **GitHub Releases**: [https://github.com/getcursor/cursor/releases](https://github.com/getcursor/cursor/releases)

### Installation by Platform

#### 1. Windows
1. Download the `.exe` installer from the official website
2. Run the installer and follow the setup wizard
3. Launch Cursor from the Start menu

#### 2. macOS
1. Download the `.dmg` file from the official website
2. Open the downloaded file and drag Cursor to Applications
3. Launch Cursor from Applications or Spotlight

#### 3. Linux
1. Download the `.AppImage` or `.deb` package
2. For `.deb`: `sudo dpkg -i cursor_*.deb`
3. For `.AppImage`: `chmod +x cursor_*.AppImage && ./cursor_*.AppImage`

---

## Essential Dependencies

### 1. Git

Git is essential for version control and Cursor's AI features.

**Installation:**

**1. Windows**
- Download from: [https://git-scm.com/download/win](https://git-scm.com/download/win)
- Or use PowerShell (run as Administrator): `winget install Git.Git`
- During installation, choose "Git from the command line and also from 3rd-party software"

**2. macOS**
```bash
# Using Homebrew (recommended)
brew install git

# Or download from: https://git-scm.com/download/mac
```

**3. Linux**
```bash
# Ubuntu/Debian
sudo apt-get update && sudo apt-get install git

# Fedora
sudo dnf install git

# Arch
sudo pacman -S git
```

**Verify Installation:**
```bash
git --version
```

---

### 2. Python 3.13

Python is required for Python development and many extensions.

**Installation:**

**1. Windows**
- Download from: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- **Important**: Check "Add Python to PATH" during installation
- Or use PowerShell (run as Administrator): `winget install Python.Python.3.13`

**2. macOS**
```bash
# Using Homebrew (recommended)
brew install python@3.13

# Or download from: https://www.python.org/downloads/
```

**3. Linux**
```bash
# Ubuntu/Debian (may need to add deadsnakes PPA)
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.13 python3.13-venv python3.13-pip

# Fedora
sudo dnf install python3.13

# Arch
sudo pacman -S python
```

**Verify Installation:**
```bash
python3.13 --version
# or
python3 --version
```

**Install pip (if not included):**
```bash
python3.13 -m ensurepip --upgrade
```

---

### 3. Node.js

Required for JavaScript/TypeScript development and many extensions.

**Installation:**

**1. Windows**
- Download LTS version from: [https://nodejs.org/](https://nodejs.org/)
- Or use PowerShell (run as Administrator): `winget install OpenJS.NodeJS.LTS`

**2. macOS**
```bash
# Using Homebrew (recommended)
brew install node

# Or download from: https://nodejs.org/
```

**3. Linux**
```bash
# Ubuntu/Debian (using NodeSource)
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# Or using snap
sudo snap install node --classic

# Fedora
sudo dnf install nodejs npm

# Arch
sudo pacman -S nodejs npm
```

**Alternative: Using nvm (Node Version Manager)**
```bash
# Install nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# Install and use Node.js
nvm install --lts
nvm use --lts
```

**Verify Installation:**
```bash
node --version
npm --version
```

---

### 4. Docker

Docker is required for containerized development environments.

**Installation:**

**1. Windows**
- Download Docker Desktop from: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
- Requires WSL 2 (Windows Subsystem for Linux)
- Install WSL 2 first if needed (run PowerShell as Administrator):
  ```powershell
  wsl --install
  ```
- After installing WSL 2, restart your computer
- Then install Docker Desktop and enable WSL 2 integration in Docker Desktop settings

**2. macOS**
- Download Docker Desktop from: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
- Or using Homebrew: `brew install --cask docker`
- Launch Docker Desktop after installation

**3. Linux**
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install docker.io docker-compose
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
# Log out and back in for group changes to take effect

# Fedora
sudo dnf install docker docker-compose
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

# Arch
sudo pacman -S docker docker-compose
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
```

**Verify Installation:**
```bash
docker --version
docker-compose --version
```

**Test Docker:**
```bash
docker run hello-world
```

---

## Git and GitHub Setup

### Initial Git Configuration

After installing Git, configure it with your name and email:

**Windows/macOS/Linux:**
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Set default branch name to main
git config --global init.defaultBranch main

# Set default editor (optional)
git config --global core.editor "cursor --wait"  # For Cursor
# or
git config --global core.editor "code --wait"     # For VS Code
```

### GitHub Authentication

There are two main methods to authenticate with GitHub:

#### Method 1: Personal Access Token (Recommended)

1. **Create a Personal Access Token:**
   - Go to GitHub: [https://github.com/settings/tokens](https://github.com/settings/tokens)
   - Click "Generate new token" → "Generate new token (classic)"
   - Give it a name (e.g., "Cursor Development")
   - Select expiration (recommend 90 days or custom)
   - Select scopes:
     - `repo` (full control of private repositories)
     - `workflow` (if using GitHub Actions)
     - `read:org` (if accessing organization repos)
   - Click "Generate token"
   - **Copy the token immediately** (you won't see it again)

2. **Authenticate Git with the token:**
   ```bash
   # When Git prompts for password, use your token as the password
   git clone https://github.com/username/repo.git
   # Username: your-github-username
   # Password: your-personal-access-token
   ```

3. **Store credentials (Windows):**
   ```bash
   # Git will use Windows Credential Manager
   git config --global credential.helper wincred
   ```

4. **Store credentials (macOS):**
   ```bash
   # Git will use Keychain to store credentials
   git config --global credential.helper osxkeychain
   ```

5. **Store credentials (Linux):**
   ```bash
   # Git will use credential store
   git config --global credential.helper store
   ```

#### Method 2: SSH Keys (More Secure)

1. **Generate SSH Key:**
   
   **Windows (Git Bash):**
   ```bash
   # Open Git Bash (installed with Git)
   ssh-keygen -t ed25519 -C "your.email@example.com"
   # Press Enter to accept default location
   # Enter a passphrase (optional but recommended)
   ```

   **macOS:**
   ```bash
   ssh-keygen -t ed25519 -C "your.email@example.com"
   # Press Enter to accept default location
   # Enter a passphrase (optional but recommended)
   ```

   **Linux:**
   ```bash
   ssh-keygen -t ed25519 -C "your.email@example.com"
   # Press Enter to accept default location
   # Enter a passphrase (optional but recommended)
   ```

2. **Add SSH Key to SSH Agent:**
   
   **Windows (Git Bash):**
   ```bash
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519
   ```

   **macOS:**
   ```bash
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519
   ```

   **Linux:**
   ```bash
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519
   ```

3. **Copy Public Key:**
   
   **Windows (PowerShell):**
   ```powershell
   Get-Content ~/.ssh/id_ed25519.pub | Set-Clipboard
   ```

   **macOS:**
   ```bash
   pbcopy < ~/.ssh/id_ed25519.pub
   ```

   **Linux:**
   ```bash
   cat ~/.ssh/id_ed25519.pub | xclip -selection clipboard
   # or if xclip is not installed:
   cat ~/.ssh/id_ed25519.pub
   # Then manually copy the output
   ```

4. **Add SSH Key to GitHub:**
   - Go to: [https://github.com/settings/keys](https://github.com/settings/keys)
   - Click "New SSH key"
   - Title: "Cursor Development" (or your computer name)
   - Key: Paste your public key
   - Click "Add SSH key"

5. **Test SSH Connection:**
   ```bash
   ssh -T git@github.com
   # You should see: "Hi username! You've successfully authenticated..."
   ```

6. **Use SSH URLs for Cloning:**
   ```bash
   # Use SSH instead of HTTPS
   git clone git@github.com:username/repo.git
   ```

### GitHub Extensions for Cursor

Install these extensions for better GitHub integration:

1. **GitLens**
   - Extension ID: `eamodio.gitlens`
   - Features: Enhanced Git capabilities, blame annotations, commit history

2. **GitHub Pull Requests and Issues**
   - Extension ID: `GitHub.vscode-pull-request-github`
   - Features: Create and review PRs directly from Cursor

3. **GitHub Copilot** (Optional - requires subscription)
   - Extension ID: `GitHub.copilot`
   - Features: AI-powered code suggestions

**Install via Command Line:**
```bash
cursor --install-extension eamodio.gitlens
cursor --install-extension GitHub.vscode-pull-request-github
```

### Linking GitHub with Cursor

1. **Open Cursor**
2. **Sign in to GitHub:**
   - Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows)
   - Type "GitHub: Sign in"
   - Select "GitHub: Sign in with GitHub"
   - Browser will open for authentication
   - Authorize Cursor

3. **Verify Connection:**
   - Open Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`)
   - Type "GitHub: Show GitHub Account"
   - You should see your GitHub username

4. **Clone a Repository:**
   - Press `Cmd+Shift+P` / `Ctrl+Shift+P`
   - Type "Git: Clone"
   - Enter repository URL or GitHub username/repo
   - Select folder to clone into

### Common Git Commands

```bash
# Initialize a new repository
git init

# Clone a repository
git clone https://github.com/username/repo.git
# or with SSH
git clone git@github.com:username/repo.git

# Check status
git status

# Add files
git add .                    # Add all files
git add filename.py          # Add specific file

# Commit changes
git commit -m "Your commit message"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main

# Create and switch to new branch
git checkout -b new-branch-name

# Switch branches
git checkout branch-name

# View commit history
git log

# View differences
git diff
```

---

## Required Extensions

Install these extensions in Cursor for optimal functionality:

### Core Extensions

1. **Python**
   - Extension ID: `ms-python.python`
   - Publisher: Microsoft
   - Essential for Python development, debugging, and IntelliSense

2. **Python Debugger**
   - Extension ID: `ms-python.debugpy`
   - Publisher: Microsoft
   - Required for debugging Python code

3. **Pylance**
   - Extension ID: `ms-python.vscode-pylance`
   - Publisher: Microsoft
   - Advanced Python language support (usually installed with Python extension)

### PowerShell (Windows)

4. **PowerShell**
   - Extension ID: `ms-vscode.PowerShell`
   - Publisher: Microsoft
   - Required for PowerShell script support and execution

### Data & CSV Tools

5. **Rainbow CSV**
   - Extension ID: `mechatroner.rainbow-csv`
   - Publisher: mechatroner
   - Colorizes CSV files and provides SQL-like query capabilities

### Additional Recommended Extensions

6. **GitLens**
   - Extension ID: `eamodio.gitlens`
   - Publisher: GitKraken
   - Enhanced Git capabilities

7. **GitHub Pull Requests and Issues**
   - Extension ID: `GitHub.vscode-pull-request-github`
   - Publisher: GitHub
   - Create and review pull requests directly in Cursor

8. **Prettier**
   - Extension ID: `esbenp.prettier-vscode`
   - Publisher: Prettier
   - Code formatter

9. **ESLint**
   - Extension ID: `dbaeumer.vscode-eslint`
   - Publisher: Microsoft
   - JavaScript/TypeScript linting

10. **Error Lens**
    - Extension ID: `usernamehw.errorlens`
    - Publisher: usernamehw
    - Inline error highlighting

11. **Path Intellisense**
    - Extension ID: `christian-kohler.path-intellisense`
    - Publisher: Christian Kohler
    - Autocomplete for file paths

---

## How to Install Extensions

### Method 1: Using Cursor UI
1. Open Cursor
2. Click the Extensions icon in the sidebar (or press `Cmd+Shift+X` / `Ctrl+Shift+X`)
3. Search for the extension by name or ID
4. Click "Install"

### Method 2: Using Command Palette
1. Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)
2. Type "Extensions: Install Extensions"
3. Search and install

### Method 3: Using Command Line
```bash
# Install extension by ID
cursor --install-extension ms-python.python
cursor --install-extension ms-python.debugpy
cursor --install-extension ms-python.vscode-pylance
cursor --install-extension ms-vscode.PowerShell
cursor --install-extension mechatroner.rainbow-csv
cursor --install-extension eamodio.gitlens
cursor --install-extension GitHub.vscode-pull-request-github
```

---

## Useful Tools and Packages

This section covers commonly used tools and packages across projects.

### Python Virtual Environments

Always use virtual environments to isolate project dependencies:

```bash
# Create a virtual environment
python3.13 -m venv venv

# Activate (macOS/Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Deactivate
deactivate
```

### Package Managers

**pip (Python)**
```bash
# Upgrade pip
python3.13 -m pip install --upgrade pip

# Install from requirements.txt
pip install -r requirements.txt

# Install specific package
pip install package_name
```

**npm (Node.js)**
```bash
# Install package globally
npm install -g package_name

# Install local dependencies
npm install

# Install and save to package.json
npm install package_name --save
```

**Homebrew (macOS)**
```bash
# Install package
brew install package_name

# Install cask (GUI applications)
brew install --cask application_name

# Update Homebrew and packages
brew update && brew upgrade
```

### Common Python Packages

**Web and API Development**
```bash
pip install requests          # HTTP library for API calls
pip install canvasapi         # Canvas LMS API client
pip install flask             # Web framework
pip install fastapi           # Modern web framework
```

**Data Processing and Analysis**
```bash
pip install pandas            # Data manipulation and analysis
pip install numpy             # Numerical computing
pip install scipy             # Scientific computing
pip install opencv-python     # Computer vision and image processing
```

**Image Processing**
```bash
pip install Pillow            # Python Imaging Library
pip install insightface       # Face recognition and analysis
pip install onnxruntime       # ONNX model runtime
```

**Machine Learning and AI**
```bash
pip install huggingface_hub   # Hugging Face model downloads
pip install replicate         # Replicate API client
pip install scikit-learn      # Machine learning library
```

**Text Processing and Utilities**
```bash
pip install fuzzywuzzy        # Fuzzy string matching
pip install python-Levenshtein # String similarity (required by fuzzywuzzy)
pip install reportlab         # PDF generation
```

### Development Servers

**Python HTTP Server**
```bash
# Simple local server (Python 3)
python3 -m http.server 5173

# Visit: http://127.0.0.1:5173/
```

**Node.js Serve**
```bash
# Install globally
npm install -g serve

# Run server
serve -l 5173 .

# Visit: http://localhost:5173/
```

### Code Quality Tools

**Python Linting and Formatting**
```bash
pip install black             # Code formatter
pip install flake8            # Linter
pip install pylint            # Advanced linter
pip install mypy              # Type checking
```

**JavaScript/TypeScript Tools**
```bash
npm install -g eslint         # JavaScript linter
npm install -g prettier       # Code formatter
npm install -g typescript     # TypeScript compiler
```

### Git Tools

**Git Configuration**
```bash
# Configure Git
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Set default branch name
git config --global init.defaultBranch main

# Useful aliases
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
```

**GitHub CLI (gh)**
```bash
# macOS
brew install gh

# Linux
sudo apt-get install gh

# Windows
winget install GitHub.cli

# Authenticate
gh auth login
```

### Shell Scripting Tools

**Bash Scripting**
- Use `#!/bin/bash` shebang for bash scripts
- Make scripts executable: `chmod +x script.sh`
- Run with: `./script.sh`

**PowerShell (Windows)**
- Built into Windows 10/11
- Use `#!/usr/bin/env pwsh` for cross-platform scripts
- Execution policy: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`

### File and System Utilities

**jq (JSON processor)**
```bash
# macOS
brew install jq

# Linux
sudo apt-get install jq

# Windows
winget install jqlang.jq
```

**curl and wget**
```bash
# Usually pre-installed on macOS/Linux
# For Windows: included with Git for Windows

# Download file
curl -O https://example.com/file.zip
wget https://example.com/file.zip
```

### Database Tools (Optional)

**SQLite**
```bash
# Usually pre-installed with Python
# Access via Python: import sqlite3
```

**PostgreSQL Client**
```bash
# macOS
brew install postgresql

# Linux
sudo apt-get install postgresql-client

# Windows
# Download from: https://www.postgresql.org/download/windows/
```

### Version Managers

**pyenv (Python Version Manager)**
```bash
# macOS
brew install pyenv

# Linux
curl https://pyenv.run | bash

# Install Python version
pyenv install 3.13.0
pyenv global 3.13.0
```

**nvm (Node Version Manager)**
```bash
# Install nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# Install and use Node.js
nvm install --lts
nvm use --lts
```

### Project Templates

**Python Project Structure**
```
project_name/
├── venv/                 # Virtual environment (gitignored)
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
├── .gitignore          # Git ignore rules
├── src/                # Source code
├── tests/              # Test files
└── scripts/            # Utility scripts
```

**Node.js Project Structure**
```
project_name/
├── node_modules/       # Dependencies (gitignored)
├── package.json        # Project configuration
├── package-lock.json   # Dependency lock file
├── README.md          # Project documentation
├── .gitignore        # Git ignore rules
├── src/              # Source code
└── scripts/          # Utility scripts
```

---

## Premade Packages

Ready-to-use premade packages are available in the [`premade-packages/`](./premade-packages/) folder:

**Discord Integration** (see [`premade-packages/discord/`](./premade-packages/discord/)):
- [Token Messaging](./premade-packages/discord/token-messaging/) - Send messages using Discord account token
- [Discord Bot](./premade-packages/discord/bot/) - Full-featured Discord bot with commands
- [Webhook](./premade-packages/discord/webhook/) - Send messages via webhooks

**Automation**:
- [Webhook Listener](./premade-packages/automation/webhook-listener/) - Receive and log webhooks with Flask
- [Email Sender](./premade-packages/automation/email-sender/) - Send templated HTML emails via SMTP
- [File Watcher](./premade-packages/automation/file-watcher/) - Monitor directory for file changes

**API Tools**:
- [API Client](./premade-packages/api/api-client/) - Reusable REST API client with rate limiting

**Utilities**:
- [Logger](./premade-packages/utils/logger/) - Structured logging with console and file output
- [Environment Manager](./premade-packages/utils/env-manager/) - Check and generate .env files
- [Signature Verifier](./premade-packages/utils/signature-verifier/) - Validate HMAC signatures for webhooks

**Development Tools**:
- [CLI Menu](./premade-packages/dev-tools/cli-menu/) - Interactive command-line menu system
- [Config Manager](./premade-packages/dev-tools/config-manager/) - Handle YAML/JSON configuration files

**Server Development**:
- [Localhost Server](./premade-packages/localhost-server/) - Python HTTP server tutorial

Each package includes:
- Complete working code
- Setup instructions
- Requirements file
- Environment variable templates
- Security best practices

See the [Premade Packages README](./premade-packages/README.md) for more details.

---

## Legacy Code Templates

The following templates are also available for reference:

### Send Discord Messages via Python

**Requirements:**
```bash
pip install requests
```

**Template:**
```python
import requests
import json
import os

# Store token in environment variable for security
# Set it with: export DISCORD_TOKEN="your_token_here" (macOS/Linux)
# Or: $env:DISCORD_TOKEN="your_token_here" (Windows PowerShell)
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "YOUR_TOKEN_HERE")
CHANNEL_ID = "YOUR_CHANNEL_ID_HERE"

def send_discord_message(message_content, channel_id=None):
    """
    Send a message to a Discord channel using the Discord API.
    
    Args:
        message_content (str): The message to send
        channel_id (str, optional): Channel ID. Uses default if not provided.
    
    Returns:
        bool: True if successful, False otherwise
    """
    if channel_id is None:
        channel_id = CHANNEL_ID
    
    api_url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    
    headers = {
        "Authorization": DISCORD_TOKEN,
        "Content-Type": "application/json"
    }
    
    payload = {
        "content": message_content
    }
    
    try:
        response = requests.post(api_url, headers=headers, data=json.dumps(payload))
        
        if response.status_code == 200:
            print("Message sent successfully!")
            return True
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
            print(f"Response: {response.json()}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
if __name__ == "__main__":
    send_discord_message("Hello from Python!")
```

**How to get Discord Token:**
1. Open Discord in your browser
2. Press `F12` to open Developer Tools
3. Go to Network tab
4. Send a message in any channel
5. Find the request to `messages` endpoint
6. Look for `Authorization` header - that's your token

**How to get Channel ID:**
1. Enable Developer Mode in Discord (Settings → Advanced → Developer Mode)
2. Right-click on the channel
3. Click "Copy ID"

### Start Localhost Server

**Simple HTTP Server (Python):**

```python
import http.server
import socketserver
import webbrowser
import threading
import os

def start_localhost_server(port=5173, directory=None, open_browser=True):
    """
    Start a simple HTTP server on localhost.
    
    Args:
        port (int): Port number (default: 5173)
        directory (str, optional): Directory to serve. Defaults to current directory.
        open_browser (bool): Whether to open browser automatically
    """
    if directory:
        os.chdir(directory)
    
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), handler)
    
    server_url = f"http://localhost:{port}"
    
    print(f"Server starting on {server_url}")
    print(f"Serving directory: {os.getcwd()}")
    print("Press Ctrl+C to stop the server")
    
    def start_server():
        httpd.serve_forever()
    
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    if open_browser:
        webbrowser.open(server_url)
    
    try:
        while True:
            import time
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping server...")
        httpd.shutdown()

# Example usage
if __name__ == "__main__":
    # Serve current directory on port 5173
    start_localhost_server()
    
    # Or serve a specific directory
    # start_localhost_server(port=8000, directory="/path/to/your/html/files")
```

**Quick Command Line Version:**
```bash
# macOS/Linux/Windows
python3 -m http.server 5173

# Then visit: http://localhost:5173
```

### Environment Variables Helper

**Template for managing environment variables:**

```python
import os
from typing import Optional

def get_env_var(key: str, default: Optional[str] = None, required: bool = False) -> Optional[str]:
    """
    Get an environment variable with error handling.
    
    Args:
        key (str): Environment variable name
        default (str, optional): Default value if not found
        required (bool): If True, raise error if variable is missing
    
    Returns:
        str: Environment variable value or default
    """
    value = os.getenv(key, default)
    
    if required and value is None:
        raise ValueError(f"Required environment variable '{key}' is not set")
    
    return value

# Example usage
API_KEY = get_env_var("API_KEY", required=True)
OPTIONAL_SETTING = get_env_var("OPTIONAL_SETTING", default="default_value")
```

### File Operations Helper

```python
import os
import json
from pathlib import Path

def read_json_file(file_path: str) -> dict:
    """Read and parse a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json_file(file_path: str, data: dict, indent: int = 2) -> None:
    """Write data to a JSON file."""
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)

def ensure_directory_exists(directory: str) -> None:
    """Create directory if it doesn't exist."""
    Path(directory).mkdir(parents=True, exist_ok=True)
```

### API Request Helper

```python
import requests
import time
from typing import Optional, Dict, Any

def make_api_request(
    url: str,
    method: str = "GET",
    headers: Optional[Dict[str, str]] = None,
    data: Optional[Dict[str, Any]] = None,
    retries: int = 3,
    retry_delay: float = 1.0
) -> Optional[requests.Response]:
    """
    Make an API request with retry logic.
    
    Args:
        url (str): API endpoint URL
        method (str): HTTP method (GET, POST, etc.)
        headers (dict): Request headers
        data (dict): Request payload
        retries (int): Number of retry attempts
        retry_delay (float): Delay between retries in seconds
    
    Returns:
        requests.Response or None
    """
    for attempt in range(retries):
        try:
            if method.upper() == "GET":
                response = requests.get(url, headers=headers, timeout=10)
            elif method.upper() == "POST":
                response = requests.post(url, headers=headers, json=data, timeout=10)
            else:
                response = requests.request(method, url, headers=headers, json=data, timeout=10)
            
            response.raise_for_status()
            return response
            
        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                print(f"Request failed, retrying in {retry_delay}s... ({attempt + 1}/{retries})")
                time.sleep(retry_delay)
            else:
                print(f"Request failed after {retries} attempts: {e}")
                return None
    
    return None
```

### Logging Setup

```python
import logging
import sys
from pathlib import Path

def setup_logging(log_file: Optional[str] = None, log_level: int = logging.INFO):
    """
    Set up logging configuration.
    
    Args:
        log_file (str, optional): Path to log file
        log_level (int): Logging level
    """
    handlers = [logging.StreamHandler(sys.stdout)]
    
    if log_file:
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        handlers.append(logging.FileHandler(log_file))
    
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=handlers
    )
    
    return logging.getLogger(__name__)

# Example usage
logger = setup_logging("logs/app.log")
logger.info("Application started")
logger.error("Something went wrong")
```

### Date and Time Utilities

```python
from datetime import datetime, timedelta
import pytz

def get_current_timestamp() -> str:
    """Get current timestamp in ISO format."""
    return datetime.now().isoformat()

def format_date(date_obj: datetime, format_string: str = "%Y-%m-%d") -> str:
    """Format datetime object to string."""
    return date_obj.strftime(format_string)

def parse_date(date_string: str, format_string: str = "%Y-%m-%d") -> datetime:
    """Parse date string to datetime object."""
    return datetime.strptime(date_string, format_string)

def days_ago(days: int) -> datetime:
    """Get datetime for N days ago."""
    return datetime.now() - timedelta(days=days)
```

### Complete Project Template

Create a new file `template.py` with this structure:

```python
#!/usr/bin/env python3
"""
Project Template
Description of what this project does.
"""

import os
import sys
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Main function."""
    logger.info("Starting application...")
    
    # Your code here
    
    logger.info("Application completed.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
        sys.exit(1)
```

---

## Docker Container Setup

### Basic Docker Usage

1. **Pull a Python image:**
   ```bash
   docker pull python:3.13
   ```

2. **Run a container:**
   
   **Windows (PowerShell):**
   ```powershell
   docker run -it --rm -v ${PWD}:/workspace -w /workspace python:3.13 bash
   ```
   
   **macOS/Linux:**
   ```bash
   docker run -it --rm -v $(pwd):/workspace -w /workspace python:3.13 bash
   ```

### Dockerizing Python Projects

#### Basic Dockerfile for Python Projects

Create a `Dockerfile` in your project root:

```dockerfile
# Use Python 3.13 as base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port (if your app uses one)
EXPOSE 5173

# Run the application
CMD ["python", "your_script.py"]
```

#### Docker Compose for Python Projects

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  app:
    build: .
    container_name: python-app
    volumes:
      - .:/app
      - /app/venv  # Exclude venv from volume
    ports:
      - "5173:5173"
    environment:
      - PYTHONUNBUFFERED=1
    command: python your_script.py
    restart: unless-stopped
```

#### Docker Compose for Python with Localhost Server

```yaml
version: '3.8'

services:
  web:
    build: .
    container_name: python-web-server
    volumes:
      - .:/app
    ports:
      - "5173:5173"
    environment:
      - PYTHONUNBUFFERED=1
    command: python -m http.server 5173
    restart: unless-stopped
```

#### Docker Compose for Node.js Projects

```yaml
version: '3.8'

services:
  app:
    build: .
    container_name: node-app
    volumes:
      - .:/app
      - /app/node_modules  # Exclude node_modules from volume
    ports:
      - "5173:5173"
    environment:
      - NODE_ENV=development
    command: npm start
    restart: unless-stopped
```

Create `Dockerfile` for Node.js:

```dockerfile
FROM node:20-slim

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 5173

CMD ["npm", "start"]
```

### Docker Commands

**Windows (PowerShell):**
```powershell
# Build image
docker build -t my-app .

# Run container
docker run -d -p 5173:5173 --name my-app my-app

# View running containers
docker ps

# View logs
docker logs my-app

# Stop container
docker stop my-app

# Remove container
docker rm my-app

# Use Docker Compose
docker-compose up -d
docker-compose down
docker-compose logs -f
```

**macOS/Linux:**
```bash
# Build image
docker build -t my-app .

# Run container
docker run -d -p 5173:5173 --name my-app my-app

# View running containers
docker ps

# View logs
docker logs my-app

# Stop container
docker stop my-app

# Remove container
docker rm my-app

# Use Docker Compose
docker-compose up -d
docker-compose down
docker-compose logs -f
```

### Dockerizing Discord Bot Project

**Dockerfile:**
```dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Use environment variable for token
ENV DISCORD_TOKEN=""
ENV CHANNEL_ID=""

CMD ["python", "discord_bot.py"]
```

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  discord-bot:
    build: .
    container_name: discord-bot
    environment:
      - DISCORD_TOKEN=${DISCORD_TOKEN}
      - CHANNEL_ID=${CHANNEL_ID}
    restart: unless-stopped
```

**Create `.env` file:**
```env
DISCORD_TOKEN=your_token_here
CHANNEL_ID=your_channel_id_here
```

**Run:**
```bash
docker-compose up -d
```

### Dockerizing Localhost Server Project

**Dockerfile:**
```dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5173

CMD ["python", "server.py"]
```

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  web-server:
    build: .
    container_name: web-server
    ports:
      - "5173:5173"
    volumes:
      - .:/app
      - /app/venv
    environment:
      - PYTHONUNBUFFERED=1
    command: python -m http.server 5173
    restart: unless-stopped
```

### Docker with Environment Variables

**docker-compose.yml with .env:**
```yaml
version: '3.8'

services:
  app:
    build: .
    env_file:
      - .env
    environment:
      - PYTHONUNBUFFERED=1
    ports:
      - "${PORT:-5173}:5173"
    volumes:
      - .:/app
```

### Connect Cursor to Docker Container

1. **Install the Dev Containers extension:**
   - Extension ID: `ms-vscode-remote.remote-containers`
   - Install via: `cursor --install-extension ms-vscode-remote.remote-containers`

2. **Open your project folder in Cursor**

3. **Create Dev Container:**
   - Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows)
   - Type "Dev Containers: Add Dev Container Configuration Files"
   - Select your base image (e.g., Python 3.13, Node.js 20)

4. **Reopen in Container:**
   - Press `Cmd+Shift+P` / `Ctrl+Shift+P`
   - Type "Dev Containers: Reopen in Container"
   - Cursor will build and connect to the container

### Docker .dockerignore

Create `.dockerignore` to exclude unnecessary files:

```
venv/
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
node_modules/
.git/
.gitignore
.env
*.log
.DS_Store
Thumbs.db
```

### Multi-stage Dockerfile (Production)

For production deployments:

```dockerfile
# Build stage
FROM python:3.13-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Production stage
FROM python:3.13-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .

ENV PATH=/root/.local/bin:$PATH

EXPOSE 5173

CMD ["python", "your_script.py"]
```

---

## Quick Setup Checklist

- [ ] Install Cursor IDE
- [ ] Install Git and verify with `git --version`
- [ ] Install Python 3.13 and verify with `python3.13 --version`
- [ ] Install Node.js and verify with `node --version`
- [ ] Install Docker and verify with `docker --version`
- [ ] Install Python extension (`ms-python.python`)
- [ ] Install Python Debugger extension (`ms-python.debugpy`)
- [ ] Install Pylance extension (`ms-python.vscode-pylance`)
- [ ] Install PowerShell extension (Windows only) (`ms-vscode.PowerShell`)
- [ ] Install Rainbow CSV extension (`mechatroner.rainbow-csv`)
- [ ] Install Dev Containers extension (`ms-vscode-remote.remote-containers`)
- [ ] Test Docker with `docker run hello-world`
- [ ] Configure Python interpreter in Cursor (Cmd+Shift+P → "Python: Select Interpreter")
- [ ] Test Python debugging in a sample file

---

## Verification Commands

Run these commands to verify your installation:

```bash
# Check Git
git --version

# Check Python
python3.13 --version
python3.13 -m pip --version

# Check Node.js
node --version
npm --version

# Check Docker
docker --version
docker-compose --version
docker ps

# Check Cursor (if in PATH)
cursor --version
```

---

## Troubleshooting

### Python Issues
- **Python not found**: Add Python to your PATH
- **Wrong Python version**: Use `python3.13` explicitly or set up aliases
- **pip not found**: Run `python3.13 -m ensurepip --upgrade`

### Docker Issues
- **Permission denied**: Add your user to the docker group (Linux)
- **Docker daemon not running**: Start Docker Desktop (macOS/Windows) or `sudo systemctl start docker` (Linux)
- **WSL 2 required**: Install WSL 2 on Windows before Docker Desktop

### Extension Issues
- **Extensions not installing**: Check internet connection and Cursor version
- **Python extension not working**: Ensure Python interpreter is selected in Cursor settings

### Cursor Issues
- **Cursor not launching**: Check system requirements
- **AI features not working**: Ensure you're signed in and have an active subscription

---

## Additional Resources

- **Cursor Documentation**: [https://docs.cursor.sh](https://docs.cursor.sh)
- **Python Documentation**: [https://docs.python.org/3.13/](https://docs.python.org/3.13/)
- **Node.js Documentation**: [https://nodejs.org/docs/](https://nodejs.org/docs/)
- **Docker Documentation**: [https://docs.docker.com/](https://docs.docker.com/)
- **Git Documentation**: [https://git-scm.com/doc](https://git-scm.com/doc)

---

## Notes

- Keep all tools updated to the latest stable versions
- Python 3.13 is the recommended version, but 3.12+ is compatible
- Node.js LTS version is recommended for stability
- Docker Desktop requires significant system resources (RAM/CPU)
- Some extensions may require additional configuration after installation

---

**Last Updated**: January 2025

**Maintained by**: ethanstoner

