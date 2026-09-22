from fastapi import FastAPI
from pymongo import AsyncMongoClient
app=FastAPI()
client=AsyncMongoClient("mongodb+srv://2025csbuvib_db_user:qdTOQeZijnfAOab0@cluster0.o6pbpjd.mongodb.net/")
db=client["College"]

#Select Collection
students_collection=db["Student"]

@app.get("/")
async def home():
    return{
        "message":"FastAPI with MongoDB is running"
    }

@app.get("/health")
async def health():
    result= await db.command("ping")
    return{"MongoDB":"Connected","ping":result["ok"] }