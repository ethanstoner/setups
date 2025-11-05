# Config Manager

Portable configuration manager that handles YAML/JSON config files with version upgrades and safe merges.

## Features

- Read/write YAML and JSON config files
- Safe config merging
- Version management
- Default value handling
- Config validation

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```python
from config_manager import ConfigManager

# Load config
config = ConfigManager("config.yaml")

# Get values with defaults
api_key = config.get("api_key", default="default_key")
port = config.get("settings.port", default=5173)

# Set values
config.set("api_key", "new_key")
config.set("settings.port", 8080)

# Save config
config.save()

# Merge configs
config.merge({"new_setting": "value"})
```

## Configuration File Format

Supports both YAML and JSON:
- YAML: `config.yaml`
- JSON: `config.json`

