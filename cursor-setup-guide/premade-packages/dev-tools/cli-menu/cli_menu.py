#!/usr/bin/env python3
"""
CLI Menu System
Interactive command-line menu for running tools and presets.
"""

import os
import sys
import subprocess
from typing import List, Optional, Callable


class MenuItem:
    """Menu item with label and action."""
    
    def __init__(self, label: str, action: Optional[Callable] = None, command: Optional[str] = None):
        """
        Args:
            label (str): Display label
            action (callable, optional): Function to call
            command (str, optional): Shell command to run
        """
        self.label = label
        self.action = action
        self.command = command
    
    def execute(self):
        """Execute the menu item action."""
        if self.action:
            return self.action()
        elif self.command:
            try:
                result = subprocess.run(
                    self.command,
                    shell=True,
                    check=False
                )
                return result.returncode == 0
            except Exception as e:
                print(f"Error executing command: {e}")
                return False
        return True


class Menu:
    """Interactive CLI menu."""
    
    def __init__(self, title: str, items: List[MenuItem]):
        """
        Args:
            title (str): Menu title
            items (list): List of MenuItem objects
        """
        self.title = title
        self.items = items
        self.selected_index = 0
    
    def _clear_screen(self):
        """Clear the screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display(self):
        """Display the menu with clean, properly aligned formatting."""
        self._clear_screen()
        
        # Calculate menu width based on content
        max_item_length = max(len(item.label) for item in self.items) if self.items else 0
        menu_width = max(50, min(max_item_length + 12, 60))
        
        # Title section
        border = "=" * menu_width
        print(f"\n{border}")
        title_line = self.title.center(menu_width)
        print(title_line)
        print(border)
        print()
        
        # Menu items - left aligned within borders
        for i, item in enumerate(self.items):
            if i == self.selected_index:
                print(f"  > [{i + 1}] {item.label}")
            else:
                print(f"    [{i + 1}] {item.label}")
        
        print()
        print(border)
        help_text = "Navigation: ↑↓ | Select: Enter | Quit: 'q'"
        help_line = help_text.center(menu_width)
        print(help_line)
        print(border)
    
    def run(self):
        """Run the interactive menu."""
        try:
            import termios
            import tty
            
            # Unix-like systems
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            
            try:
                tty.setraw(sys.stdin.fileno())
                
                while True:
                    self.display()
                    
                    # Read key
                    key = sys.stdin.read(1)
                    
                    if key == '\x1b':  # Escape sequence
                        key += sys.stdin.read(2)
                        if key == '\x1b[A':  # Up arrow
                            self.selected_index = (self.selected_index - 1) % len(self.items)
                        elif key == '\x1b[B':  # Down arrow
                            self.selected_index = (self.selected_index + 1) % len(self.items)
                    elif key == '\r' or key == '\n':  # Enter
                        item = self.items[self.selected_index]
                        self._clear_screen()
                        if item.label.lower() == "exit" or (item.command is None and item.action is None):
                            break
                        
                        border = "=" * 60
                        print(f"\n{border}")
                        exec_text = f"Executing: {item.label}"
                        exec_line = exec_text.center(60)
                        print(exec_line)
                        print(f"{border}\n")
                        
                        item.execute()
                        
                        print(border)
                        input("  Press Enter to continue...")
                    elif key == 'q':
                        break
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        
        except (ImportError, OSError):
            # Fallback for Windows or systems without termios
            self._run_simple()
    
    def _run_simple(self):
        """Simple menu runner for Windows or systems without termios."""
        while True:
            self.display()
            
            try:
                choice = input(f"\nEnter choice (1-{len(self.items)}) or 'q' to quit: ")
                
                if choice.lower() == 'q':
                    break
                
                index = int(choice) - 1
                if 0 <= index < len(self.items):
                    item = self.items[index]
                    if item.label.lower() == "exit" or (item.command is None and item.action is None):
                        break
                    
                    self._clear_screen()
                    border = "=" * 60
                    print(f"\n{border}")
                    exec_text = f"Executing: {item.label}"
                    exec_line = exec_text.center(60)
                    print(exec_line)
                    print(f"{border}\n")
                    
                    item.execute()
                    
                    print(f"\n{border}")
                    input("  Press Enter to continue...")
                else:
                    print("\nInvalid choice. Please try again.")
                    input("Press Enter to continue...")
            except (ValueError, KeyboardInterrupt):
                break


if __name__ == "__main__":
    # Example usage
    def hello_world():
        print("Hello, World!")
        return True
    
    items = [
        MenuItem("Option 1: Hello World", action=hello_world),
        MenuItem("Option 2: List Files", command="ls -la"),
        MenuItem("Option 3: Show Date", command="date"),
        MenuItem("Exit", None)
    ]
    
    menu = Menu("Example Menu", items)
    menu.run()

