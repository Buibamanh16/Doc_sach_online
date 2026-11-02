from sqlalchemy import Column, BigInteger, Integer, String, Text, Numeric, SmallInteger, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from backend.app.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    full_name = Column(String(150), nullable=True)
    avatar_url = Column(Text, nullable=True)
    role = Column(String(20), nullable=False, default="user")
    status = Column(String(20), nullable=False, default="active")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Author(Base):
    __tablename__ = "authors"

    author_id = Column(BigInteger, primary_key=True, index=True)
    pen_name = Column(String(150), nullable=False)
    biography = Column(Text, nullable=True)
    avatar_url = Column(Text, nullable=True)

class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)

class Book(Base):
    __tablename__ = "books"

    book_id = Column(BigInteger, primary_key=True, index=True)
    owner_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    cover_url = Column(Text, nullable=True)
    published_year = Column(SmallInteger, nullable=True)
    status = Column(String(20), nullable=False, default="draft")
    avg_rating = Column(Numeric(3, 2), nullable=False, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Chapter(Base):
    __tablename__ = "chapters"

    chapter_id = Column(BigInteger, primary_key=True, index=True)
    book_id = Column(BigInteger, ForeignKey("books.book_id"), nullable=False)
    chapter_no = Column(Integer, nullable=False)
    title = Column(String(255), nullable=False)
    content_url = Column(Text, nullable=True)
    price = Column(Integer, nullable=False, default=0)
    is_free = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())