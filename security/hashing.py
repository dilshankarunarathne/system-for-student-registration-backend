"""
    middleware for hashing passwords and creating tokens
"""

SECRET_KEY = "3ac975a63c346504ccc4bad65505c619a2cc502b01c7a92e3288f4d3b0def92b"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")