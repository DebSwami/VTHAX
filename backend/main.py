from fastapi import FastAPI
from dotenv import load_dotenv
from supabase import create_client
import os

load_dotenv()
app = FastAPI()

# Supabase client
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

@app.get("/")
def root():
    return {"message": "Backend running"}

@app.get("/profiles")
def get_profiles():
    response = supabase.table("profiles").select("*").execute()
    return response.data
