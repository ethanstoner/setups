# File Watcher

Watch a directory for file changes and trigger custom events.

## Features

- Monitor directory for file changes
- Trigger callbacks on file creation, modification, or deletion
- Easy to extend for custom automation

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```python
from file_watcher import watch_directory

def on_file_created(file_path):
    print(f"New file created: {file_path}")
    # Add your custom logic here

def on_file_modified(file_path):
    print(f"File modified: {file_path}")

watch_directory(
    path="./watch_folder",
    on_created=on_file_created,
    on_modified=on_file_modified
)
```

## Use Cases

- Auto-process new files
- Sync files to Discord/webhook
- Trigger builds on file changes
- Monitor logs and send alerts

