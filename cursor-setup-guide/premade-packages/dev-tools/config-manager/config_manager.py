#!/usr/bin/env python3
"""
Config Manager
Handle YAML/JSON configuration files with version management.
"""

import json
import os
from pathlib import Path
from typing import Any, Dict, Optional
try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False


class ConfigManager:
    """Configuration manager for YAML/JSON files."""
    
    def __init__(self, config_path: str, default_config: Optional[Dict] = None):
        """
        Args:
            config_path (str): Path to config file
            default_config (dict, optional): Default configuration
        """
        self.config_path = Path(config_path)
        self.config: Dict[str, Any] = {}
        self.default_config = default_config or {}
        
        # Determine file type
        self.is_yaml = self.config_path.suffix.lower() in ['.yaml', '.yml']
        self.is_json = self.config_path.suffix.lower() == '.json'
        
        # Load existing config or use defaults
        if self.config_path.exists():
            self.load()
        else:
            self.config = self.default_config.copy()
            self.save()
    
    def load(self) -> Dict[str, Any]:
        """Load configuration from file."""
        try:
            with open(self.config_path, 'r') as f:
                if self.is_yaml:
                    if not YAML_AVAILABLE:
                        raise ImportError("PyYAML not installed. Install with: pip install pyyaml")
                    self.config = yaml.safe_load(f) or {}
                else:
                    self.config = json.load(f) or {}
        except Exception as e:
            print(f"Error loading config: {e}")
            self.config = self.default_config.copy()
        
        return self.config
    
    def save(self):
        """Save configuration to file."""
        # Ensure directory exists
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            with open(self.config_path, 'w') as f:
                if self.is_yaml:
                    if not YAML_AVAILABLE:
                        raise ImportError("PyYAML not installed. Install with: pip install pyyaml")
                    yaml.dump(self.config, f, default_flow_style=False, sort_keys=False)
                else:
                    json.dump(self.config, f, indent=2)
        except Exception as e:
            print(f"Error saving config: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value using dot notation.
        
        Args:
            key (str): Key path (e.g., "settings.port")
            default (any): Default value if key not found
        
        Returns:
            any: Configuration value
        """
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any):
        """
        Set configuration value using dot notation.
        
        Args:
            key (str): Key path (e.g., "settings.port")
            value (any): Value to set
        """
        keys = key.split('.')
        config = self.config
        
        # Navigate/create nested structure
        for k in keys[:-1]:
            if k not in config or not isinstance(config[k], dict):
                config[k] = {}
            config = config[k]
        
        # Set value
        config[keys[-1]] = value
    
    def merge(self, other_config: Dict[str, Any], overwrite: bool = True):
        """
        Merge another configuration dictionary.
        
        Args:
            other_config (dict): Configuration to merge
            overwrite (bool): Whether to overwrite existing values
        """
        def deep_merge(base: dict, update: dict):
            for key, value in update.items():
                if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                    deep_merge(base[key], value)
                elif overwrite or key not in base:
                    base[key] = value
        
        deep_merge(self.config, other_config)
    
    def has(self, key: str) -> bool:
        """Check if key exists in configuration."""
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return False
        
        return True
    
    def remove(self, key: str):
        """Remove a configuration key."""
        keys = key.split('.')
        config = self.config
        
        for k in keys[:-1]:
            if isinstance(config, dict) and k in config:
                config = config[k]
            else:
                return
        
        if isinstance(config, dict) and keys[-1] in config:
            del config[keys[-1]]


if __name__ == "__main__":
    # Example usage
    default_config = {
        "app": {
            "name": "My App",
            "version": "1.0.0"
        },
        "settings": {
            "port": 5173,
            "debug": False
        }
    }
    
    config = ConfigManager("example_config.yaml", default_config)
    
    # Get values
    print(f"App name: {config.get('app.name')}")
    print(f"Port: {config.get('settings.port')}")
    
    # Set values
    config.set("settings.port", 8080)
    config.set("settings.debug", True)
    
    # Merge
    config.merge({"new_setting": "value"})
    
    # Save
    config.save()
    print("Config saved!")

