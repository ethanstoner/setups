# Logger Preset

Structured logging setup with console and file output, JSON formatting, and color output.

## Features

- Console and file logging
- JSON formatter for structured logs
- Color output for CLI
- Rotating file handler
- Configurable log levels

## Usage

```python
from logger_setup import setup_logger

# Setup logger
logger = setup_logger("my_app", log_file="logs/app.log")

# Use logger
logger.info("Application started")
logger.error("Something went wrong", exc_info=True)
logger.debug("Debug information")
```

## Configuration

The logger automatically:
- Creates log directory if it doesn't exist
- Rotates logs when they reach 10MB
- Keeps 5 backup files
- Formats logs as JSON for file, readable text for console

