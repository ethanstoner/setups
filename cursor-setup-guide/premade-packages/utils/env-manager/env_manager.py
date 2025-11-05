#!/usr/bin/env python3
"""
Environment Manager
Check .env files and generate .env.example files.
"""

import os
import re
from pathlib import Path
from typing import List, Set


def read_env_file(file_path: str) -> dict:
    """
    Read .env file and return dict of key-value pairs.
    
    Args:
        file_path (str): Path to .env file
    
    Returns:
        dict: Environment variables
    """
    env_vars = {}
    
    if not os.path.exists(file_path):
        return env_vars
    
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            
            # Skip comments and empty lines
            if not line or line.startswith('#'):
                continue
            
            # Parse KEY=VALUE
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                env_vars[key] = value
    
    return env_vars


def check_env(example_file: str = ".env.example", env_file: str = ".env") -> List[str]:
    """
    Check if .env file has all required variables from .env.example.
    
    Args:
        example_file (str): Path to .env.example
        env_file (str): Path to .env
    
    Returns:
        list: Missing variable names
    """
    example_vars = read_env_file(example_file)
    env_vars = read_env_file(env_file)
    
    missing = []
    for key in example_vars.keys():
        if key not in env_vars or not env_vars[key] or env_vars[key] == f"your_{key.lower()}_here":
            missing.append(key)
    
    return missing


def generate_env_example(code_file: str, output_file: str = ".env.example"):
    """
    Generate .env.example from code file by finding os.getenv() calls.
    
    Args:
        code_file (str): Path to code file
        output_file (str): Path to output .env.example file
    """
    if not os.path.exists(code_file):
        print(f"Error: {code_file} not found")
        return
    
    env_vars = set()
    
    # Pattern to match os.getenv("KEY") or os.getenv('KEY')
    pattern = r'os\.getenv\(["\']([^"\']+)["\']'
    
    with open(code_file, 'r') as f:
        content = f.read()
        matches = re.findall(pattern, content)
        env_vars.update(matches)
    
    # Pattern to match os.environ["KEY"] or os.environ['KEY']
    pattern2 = r'os\.environ\[["\']([^"\']+)["\']'
    matches2 = re.findall(pattern2, content)
    env_vars.update(matches2)
    
    # Write .env.example
    with open(output_file, 'w') as f:
        for var in sorted(env_vars):
            f.write(f"{var}=your_{var.lower()}_here\n")
    
    print(f"Generated {output_file} with {len(env_vars)} variables")


def validate_env(env_file: str = ".env", required_vars: List[str] = None) -> bool:
    """
    Validate that .env file has all required variables set.
    
    Args:
        env_file (str): Path to .env file
        required_vars (list): List of required variable names
    
    Returns:
        bool: True if all variables are set
    """
    if required_vars is None:
        required_vars = []
    
    env_vars = read_env_file(env_file)
    missing = [var for var in required_vars if var not in env_vars or not env_vars[var]]
    
    if missing:
        print(f"Missing required variables: {', '.join(missing)}")
        return False
    
    return True


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python env_manager.py [check|generate|validate]")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "check":
        missing = check_env()
        if missing:
            print(f"Missing variables: {', '.join(missing)}")
            sys.exit(1)
        else:
            print("All required variables are set!")
    
    elif command == "generate":
        code_file = sys.argv[2] if len(sys.argv) > 2 else "*.py"
        generate_env_example(code_file)
    
    elif command == "validate":
        required = sys.argv[2:] if len(sys.argv) > 2 else []
        if validate_env(required_vars=required):
            print("Environment validation passed!")
        else:
            sys.exit(1)
    
    else:
        print(f"Unknown command: {command}")

