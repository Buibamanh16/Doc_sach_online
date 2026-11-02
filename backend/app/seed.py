from backend.app.database import engine, SessionLocal
from backend.app.models import Base, User
from backend.app.utils import hash_password  # Dùng hàm hash mật khẩu bằng bcrypt

def init_db():
    # 1. Tự động tạo bảng nếu chưa có
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    # 2. Xóa tài khoản admin cũ (nếu lưu mật khẩu dạng plain text) để tạo lại
    existing_user = db.query(User).filter(User.username == "admin").first()
    if existing_user:
        db.delete(existing_user)
        db.commit()

    # 3. Tạo tài khoản admin mới với mật khẩu đã mã hóa bcrypt
    hashed_pwd = hash_password("123456")
    test_user = User(
        username="admin",
        password=hashed_pwd,
        email="admin@example.com"
    )
    db.add(test_user)
    db.commit()
    print("✅ Đã tạo/cập nhật user 'admin' với mật khẩu đã băm bcrypt!")
    
    db.close()

if __name__ == "__main__":
    init_db()