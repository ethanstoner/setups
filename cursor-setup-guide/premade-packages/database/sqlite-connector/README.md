# SQLite Database Connector

Simple SQLite database connector with SQLAlchemy ORM for logging and storing app state.

## Features

- SQLAlchemy ORM setup
- Example CRUD operations
- Database initialization
- Model definitions

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```python
from database import init_db, User, session

# Initialize database
init_db()

# Create
user = User(name="John", email="john@example.com")
session.add(user)
session.commit()

# Read
users = session.query(User).all()

# Update
user.name = "Jane"
session.commit()

# Delete
session.delete(user)
session.commit()
```

## Customization

Edit `models.py` to define your own database models.

