# CLI Menu System

Interactive command-line menu system for running available presets and tools.

## Features

- Interactive menu with arrow key navigation
- Easy to add new menu items
- Color-coded output
- Cross-platform support

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```python
from cli_menu import Menu, MenuItem

# Create menu items
items = [
    MenuItem("Run Discord Bot", "python ../discord/bot/bot.py"),
    MenuItem("Start Localhost Server", "python ../localhost-server/server.py"),
    MenuItem("Watch Files", "python ../automation/file-watcher/file_watcher.py"),
    MenuItem("Exit", None)
]

# Create and run menu
menu = Menu("Main Menu", items)
menu.run()
```

## Customization

Edit `cli_menu.py` to add your own menu items and actions.

