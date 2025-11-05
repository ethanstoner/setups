# Cursor Extension Installation Script (PowerShell)
# This script installs all required extensions for Cursor IDE

Write-Host "Installing Cursor Extensions..." -ForegroundColor Cyan
Write-Host ""

# Check if cursor command exists
if (-not (Get-Command cursor -ErrorAction SilentlyContinue)) {
    Write-Host "Error: Cursor command not found in PATH" -ForegroundColor Red
    Write-Host "Please ensure Cursor is installed and added to your PATH" -ForegroundColor Yellow
    exit 1
}

# Array of extension IDs
$Extensions = @(
    "ms-python.python",
    "ms-python.debugpy",
    "ms-python.vscode-pylance",
    "ms-vscode.PowerShell",
    "mechatroner.rainbow-csv",
    "ms-vscode-remote.remote-containers"
)

# Install each extension
foreach ($Extension in $Extensions) {
    Write-Host "Installing $Extension..." -ForegroundColor Yellow
    cursor --install-extension $Extension
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Successfully installed $Extension" -ForegroundColor Green
    } else {
        Write-Host "Failed to install $Extension" -ForegroundColor Red
    }
    Write-Host ""
}

Write-Host "Extension installation complete!" -ForegroundColor Green
Write-Host ""
Write-Host "To verify installations:" -ForegroundColor Cyan
Write-Host "1. Open Cursor"
Write-Host "2. Go to Extensions (Ctrl+Shift+X)"
Write-Host "3. Check that all extensions are installed"

