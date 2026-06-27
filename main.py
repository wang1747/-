from fastapi import FastAPI
from database import init_db,add_logs,get_logs
from schemas import LogCreate,LogOut

app=FastAPI()

init_db()

@app.get("/")
def read_root():
    return {"message":"Study Log API is running"}}


@app.post("/logs")
def create_log(log: LogCreate):
    add_logs(log.date, log.content,log.duration)
    return {"message": "Log added successfully"}


@app.get("/logs")
def read_logs():
    logs=get_logs()
    return logs
