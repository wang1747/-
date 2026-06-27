#负责Pydantic 数据模型


from pydantic import BaseModel

class LogCreate(BaseModel):
        date: str
        subject: str
        hours: float
        notes: str = ""


class LogOut(BaseModel):
        id: int
        date: str
        subject: str
        hours: float
        notes: str






