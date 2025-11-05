#!/usr/bin/env python3
"""
SQLite Database Connector
Simple database setup with SQLAlchemy.
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()


class User(Base):
    """Example User model."""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"


# Database setup
DATABASE_URL = "sqlite:///app.db"
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """Initialize database and create tables."""
    Base.metadata.create_all(bind=engine)
    print("Database initialized")


def get_session():
    """Get database session."""
    return SessionLocal()


# Global session (use get_session() for better practice)
session = SessionLocal()


if __name__ == "__main__":
    # Example usage
    init_db()
    
    # Create
    user = User(name="John Doe", email="john@example.com")
    session.add(user)
    session.commit()
    print(f"Created: {user}")
    
    # Read
    users = session.query(User).all()
    print(f"All users: {users}")
    
    # Update
    user.name = "Jane Doe"
    session.commit()
    print(f"Updated: {user}")
    
    # Delete
    session.delete(user)
    session.commit()
    print("Deleted user")

