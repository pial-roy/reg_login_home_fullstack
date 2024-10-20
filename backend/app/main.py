from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .database import get_database
import bcrypt

app = FastAPI()

# Add CORS middleware
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

@app.post("/register/")
async def register_user(user: UserCreate):
    db = await get_database()
    existing_user = await db.users.find_one({"username": user.username})
    existing_email = await db.users.find_one({"email": user.email})

    if existing_user or existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    new_user = {
        "username": user.username,
        "email": user.email,
        "password": hashed_password.decode('utf-8')
    }
    
    await db.users.insert_one(new_user)
    return {"message": "User registered successfully!"}

@app.post("/login/")
async def login_user(user: UserLogin):
    db = await get_database()
    db_user = await db.users.find_one({"email": user.email})

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    if not bcrypt.checkpw(user.password.encode('utf-8'), db_user['password'].encode('utf-8')):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    return {"message": "Login successful!", "username": db_user["username"]}