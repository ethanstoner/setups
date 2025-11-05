#!/bin/bash
# Cursor Extension Installation Script
# This script installs all required extensions for Cursor IDE

echo "Installing Cursor Extensions..."
echo ""

# Check if cursor command exists
if ! command -v cursor &> /dev/null; then
    echo "Error: Cursor command not found in PATH"
    echo "Please ensure Cursor is installed and added to your PATH"
    exit 1
fi

# Array of extension IDs
EXTENSIONS=(
    "ms-python.python"
    "ms-python.debugpy"
    "ms-python.vscode-pylance"
    "ms-vscode.PowerShell"
    "mechatroner.rainbow-csv"
    "ms-vscode-remote.remote-containers"
)

# Install each extension
for EXTENSION in "${EXTENSIONS[@]}"; do
    echo "Installing $EXTENSION..."
    cursor --install-extension "$EXTENSION"
    if [ $? -eq 0 ]; then
        echo "Successfully installed $EXTENSION"
    else
        echo "Failed to install $EXTENSION"
    fi
    echo ""
done

echo "Extension installation complete!"
echo ""
echo "To verify installations:"
echo "1. Open Cursor"
echo "2. Go to Extensions (Cmd+Shift+X / Ctrl+Shift+X)"
echo "3. Check that all extensions are installed"

