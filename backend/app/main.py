import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
  
from fastapi import FastAPI
from app.routes import user, health

from app.db.database import engine, Base  # import properly



app = FastAPI()

Base.metadata.create_all(bind=engine)  # create tables

app.include_router(user.router)
app.include_router(health.router)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # or specify "http://localhost:3000" for React dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)  

@app.get("/")   
def read_root():
    return {"message": "CyberGarde SOC is running"}

@app.on_event("startup")
async def startup():
    print("App is starting up...")

@app.on_event("shutdown")
async def shutdown():  
    print("App is shutting down...")
