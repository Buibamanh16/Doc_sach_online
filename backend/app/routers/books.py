from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app import models, schemas

router = APIRouter()

@router.get("/", response_model=schemas.BookListResponse)
def get_books(
    page: int = Query(1, ge=1, description="Trang hiện tại"),
    limit: int = Query(12, ge=1, le=100, description="Số lượng sách mỗi trang"),
    db: Session = Depends(get_db)
):
    offset = (page - 1) * limit
    
    # Chỉ lấy các sách có trạng thái 'published'
    query = db.query(models.Book).filter(models.Book.status == "published")
    
    total = query.count()
    books = query.offset(offset).limit(limit).all()
    
    return {
        "total": total,
        "page": page,
        "limit": limit,
        "books": books
    }