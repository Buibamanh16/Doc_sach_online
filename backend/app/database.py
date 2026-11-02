from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Định dạng: postgresql://<username>:<password>@<host>:<port>/<database_name>
# Mặc định của PostgreSQL thường là user 'postgres' và port 5432
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:manh0964@localhost:5432/bookverse_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()