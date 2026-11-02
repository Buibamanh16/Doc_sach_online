import psycopg

def make_db():
    # Kết nối vào DB mặc định 'postgres' để tạo 'bookverse_db'
    # Sửa lại '123456' thành mật khẩu postgres của bạn
    try:
        conn = psycopg.connect(
            "postgresql://postgres:manh0964@localhost:5432/postgres", 
            autocommit=True
        )
        cursor = conn.cursor()
        
        # Kiểm tra xem DB đã tồn tại chưa
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'bookverse_db'")
        exists = cursor.fetchone()
        
        if not exists:
            cursor.execute("CREATE DATABASE bookverse_db")
            print("✅ Đã tạo thành công Database 'bookverse_db'!")
        else:
            print("ℹ️ Database 'bookverse_db' đã tồn tại sẵn rồi.")
            
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"❌ Lỗi: {e}")

if __name__ == "__main__":
    make_db()