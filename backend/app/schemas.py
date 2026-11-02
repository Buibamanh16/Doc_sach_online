from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

# ==========================================
# 1. SCHEMAS AUTH (Dùng cho auth.py)
# ==========================================
class UserLogin(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    success: bool
    message: str
    data: Optional[Dict[str, Any]] = None


# ==========================================
# 2. SCHEMAS BOOKS (Dùng cho books.py)
# ==========================================
class BookResponse(BaseModel):
    book_id: int
    owner_id: int
    title: str
    description: Optional[str] = None
    cover_url: Optional[str] = None
    published_year: Optional[int] = None
    status: str
    avg_rating: float
    created_at: datetime

    class Config:
        from_attributes = True

class BookListResponse(BaseModel):
    total: int
    page: int
    limit: int
    books: List[BookResponse]