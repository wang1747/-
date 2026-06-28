from fastapi import FastAPI
from database import init_db,add_logs,get_logs
from schemas import LogCreate,LogOut
from database import get_daily_hours


app=FastAPI()

init_db()

@app.get("/")
def read_root():
    return {"message":"Study Log API is running"}


@app.post("/logs")
def create_log(log: LogCreate):
    add_logs(log.date, log.subject, log.hours, log.notes)
    return {"message": "Log added successfully"}


@app.get("/logs")
def read_logs():
    logs=get_logs()
    return logs


@app.get("/logs/daily")
def read_daily_logs():
    logs=get_daily_hours()
    return logs


