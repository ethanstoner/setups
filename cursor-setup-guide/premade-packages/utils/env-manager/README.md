# Environment Manager

Tool to check `.env` files for missing keys and auto-generate `.env.example`.

## Features

- Validate `.env` file against `.env.example`
- Auto-generate `.env.example` from code
- Check for missing required variables
- Helpful error messages

## Usage

```python
from env_manager import check_env, generate_env_example

# Check if all required variables are set
missing = check_env(".env.example", ".env")
if missing:
    print(f"Missing variables: {missing}")

# Generate .env.example from code
generate_env_example("config.py", ".env.example")
```

## Command Line

```bash
# Check environment
python env_manager.py check

# Generate example
python env_manager.py generate
```

