from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app import models
from backend.app.schemas import UserLogin, LoginResponse # Hoặc import schema tương ứng
from backend.app.utils import verify_password

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)

@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    # 1. Tìm user theo username
    user = db.query(models.User).filter(models.User.username == user_data.username).first()
    
    # 2. Kiểm tra tài khoản
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tên đăng nhập hoặc mật khẩu không chính xác!"
        )
    
    # 3. Kiểm tra mật khẩu (so sánh hash hoặc chuỗi thô)
    is_valid = False
    if user.password.startswith("$2b$") or user.password.startswith("$2a$"):
        is_valid = verify_password(user_data.password, user.password)
    else:
        is_valid = (user.password == user_data.password)

    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tên đăng nhập hoặc mật khẩu không chính xác!"
        )
    
    # 4. Trả về kết quả
    return {
        "success": True,
        "message": "Đăng nhập thành công!",
        "data": {
            "user_id": user.user_id,
            "username": user.username
        }
    }