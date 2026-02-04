from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# --- 数据库连接配置 ---
# 格式: postgresql://用户名:密码@地址:端口/数据库名
# 这里使用了你提供的参数：
# 用户名: postgres (默认)
# 密码: cbj20040119
# 地址: 127.0.0.1
# 端口: 5519
# 库名: rescue
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:cbj20040119@127.0.0.1:5519/rescue"

# --- 创建数据库引擎 ---
# 注意：切换到 PostgreSQL 后，必须删掉 SQLite 专用的 connect_args={"check_same_thread": False} 参数
# 否则会报错 "TypeError: Invalid argument(s) 'check_same_thread' sent to create_engine()"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# --- 创建会话工厂 ---
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# --- 声明模型基类 ---
Base = declarative_base()

# --- 依赖项：获取数据库会话 ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()