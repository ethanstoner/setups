# Quick Reference: Cursor Setup

## One-Liner Install Commands

### 1. Windows (PowerShell as Admin)
```powershell
# Install Git
winget install Git.Git

# Install Python 3.13
winget install Python.Python.3.13

# Install Node.js
winget install OpenJS.NodeJS.LTS

# Install Docker Desktop (requires WSL 2)
winget install Docker.DockerDesktop

# Install Cursor extensions
cursor --install-extension ms-python.python
cursor --install-extension ms-python.debugpy
cursor --install-extension ms-python.vscode-pylance
cursor --install-extension ms-vscode.PowerShell
cursor --install-extension mechatroner.rainbow-csv
cursor --install-extension ms-vscode-remote.remote-containers
```

### 2. macOS (Homebrew)
```bash
# Install all dependencies
brew install git python@3.13 node
brew install --cask docker

# Install Cursor extensions via CLI
cursor --install-extension ms-python.python
cursor --install-extension ms-python.debugpy
cursor --install-extension ms-python.vscode-pylance
cursor --install-extension ms-vscode.PowerShell
cursor --install-extension mechatroner.rainbow-csv
cursor --install-extension ms-vscode-remote.remote-containers
```

### 3. Linux (Ubuntu/Debian)
```bash
# Install Git
sudo apt-get update && sudo apt-get install -y git

# Install Python 3.13
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install -y python3.13 python3.13-venv python3.13-pip

# Install Node.js
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install Docker
sudo apt-get install -y docker.io docker-compose
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

# Install Cursor extensions
cursor --install-extension ms-python.python
cursor --install-extension ms-python.debugpy
cursor --install-extension ms-python.vscode-pylance
cursor --install-extension ms-vscode.PowerShell
cursor --install-extension mechatroner.rainbow-csv
cursor --install-extension ms-vscode-remote.remote-containers
```

## Docker Quick Commands

### Windows (PowerShell)
```powershell
# Build and run with Docker Compose
docker-compose up -d

# View logs
docker-compose logs -f

# Stop containers
docker-compose down

# Build image
docker build -t my-app .

# Run container
docker run -d -p 5173:5173 --name my-app my-app
```

### macOS/Linux
```bash
# Build and run with Docker Compose
docker-compose up -d

# View logs
docker-compose logs -f

# Stop containers
docker-compose down

# Build image
docker build -t my-app .

# Run container
docker run -d -p 5173:5173 --name my-app my-app
```

## Essential Extension IDs

| Extension | ID | Required |
|-----------|-----|----------|
| Python | `ms-python.python` | Yes |
| Python Debugger | `ms-python.debugpy` | Yes |
| Pylance | `ms-python.vscode-pylance` | Yes |
| PowerShell | `ms-vscode.PowerShell` | Windows |
| Rainbow CSV | `mechatroner.rainbow-csv` | Yes |
| Dev Containers | `ms-vscode-remote.remote-containers` | Recommended |

## Quick Links

- **Cursor Download**: https://cursor.sh/download
- **Python 3.13**: https://www.python.org/downloads/
- **Node.js LTS**: https://nodejs.org/
- **Docker Desktop**: https://www.docker.com/products/docker-desktop
- **Git**: https://git-scm.com/downloads

## Verification

```bash
git --version          # Should show git version
python3.13 --version   # Should show Python 3.13.x
node --version         # Should show v20.x or higher
npm --version          # Should show npm version
docker --version       # Should show Docker version
```

## Key Shortcuts (Cursor)

- `Cmd+Shift+P` / `Ctrl+Shift+P`: Command Palette
- `Cmd+Shift+X` / `Ctrl+Shift+X`: Extensions
- `Cmd+,` / `Ctrl+,`: Settings
- `Cmd+K Cmd+S` / `Ctrl+K Ctrl+S`: Keyboard Shortcuts

