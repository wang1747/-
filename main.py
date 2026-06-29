from fastapi import FastAPI, HTTPException
from database import (init_db, add_logs, get_logs, get_logs_by_subject,
                      get_total_hours, get_weekly_hours, get_daily_hours,
                      update_logs, delete_logs, get_log_by_id)
from schemas import LogCreate, LogOut


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


@app.get("/logs/subject/{subject}")
def read_logs_by_subject(subject: str):
    logs = get_logs_by_subject(subject)
    return logs


@app.get("/logs/total")
def read_total_hours():
    hours = get_total_hours()
    return {"total_hours": hours[0][0] if hours[0][0] else 0}


@app.get("/logs/weekly")
def read_weekly_hours():
    hours = get_weekly_hours()
    return {"weekly_hours": hours[0][0] if hours[0][0] else 0}


@app.put("/logs/{log_id}")
def update_log(log_id: int, log: LogCreate):
    existing = get_log_by_id(log_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Log not found")
    update_logs(log_id, log.date, log.subject, log.hours, log.notes)
    return {"message": "Log updated successfully"}


@app.delete("/logs/{log_id}")
def delete_log(log_id: int):
    existing = get_log_by_id(log_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Log not found")
    delete_logs(log_id)
    return {"message": "Log deleted successfully"}


