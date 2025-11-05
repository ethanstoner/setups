#!/usr/bin/env python3
"""
File Watcher
Monitor directory for file changes and trigger events.
"""

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from typing import Optional, Callable
from pathlib import Path


class FileChangeHandler(FileSystemEventHandler):
    """Handle file system events."""
    
    def __init__(
        self,
        on_created: Optional[Callable] = None,
        on_modified: Optional[Callable] = None,
        on_deleted: Optional[Callable] = None,
        on_moved: Optional[Callable] = None
    ):
        self.on_created = on_created
        self.on_modified = on_modified
        self.on_deleted = on_deleted
        self.on_moved = on_moved
    
    def on_created(self, event):
        if not event.is_directory:
            if self.on_created:
                self.on_created(event.src_path)
    
    def on_modified(self, event):
        if not event.is_directory:
            if self.on_modified:
                self.on_modified(event.src_path)
    
    def on_deleted(self, event):
        if not event.is_directory:
            if self.on_deleted:
                self.on_deleted(event.src_path)
    
    def on_moved(self, event):
        if not event.is_directory:
            if self.on_moved:
                self.on_moved(event.src_path, event.dest_path)


def watch_directory(
    path: str,
    on_created: Optional[Callable] = None,
    on_modified: Optional[Callable] = None,
    on_deleted: Optional[Callable] = None,
    on_moved: Optional[Callable] = None,
    recursive: bool = True
):
    """
    Watch a directory for file changes.
    
    Args:
        path (str): Directory path to watch
        on_created (callable): Callback for file creation
        on_modified (callable): Callback for file modification
        on_deleted (callable): Callback for file deletion
        on_moved (callable): Callback for file moves
        recursive (bool): Watch subdirectories
    """
    path_obj = Path(path)
    
    if not path_obj.exists():
        print(f"Creating directory: {path}")
        path_obj.mkdir(parents=True, exist_ok=True)
    
    event_handler = FileChangeHandler(
        on_created=on_created,
        on_modified=on_modified,
        on_deleted=on_deleted,
        on_moved=on_moved
    )
    
    observer = Observer()
    observer.schedule(event_handler, str(path), recursive=recursive)
    observer.start()
    
    print(f"Watching directory: {path}")
    print("Press Ctrl+C to stop")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nStopped watching")
    
    observer.join()


if __name__ == "__main__":
    def on_file_created(file_path):
        print(f"[CREATED] {file_path}")
    
    def on_file_modified(file_path):
        print(f"[MODIFIED] {file_path}")
    
    watch_directory(
        path="./watch_folder",
        on_created=on_file_created,
        on_modified=on_file_modified
    )

