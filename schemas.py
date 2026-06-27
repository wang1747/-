#负责Pydantic 数据模型


from pydantic import BaseModel

class LogCreate(BaseModel):
        date: str
        content: str
        duration: float


class LogOut(BaseModel):
        id: int
        date: str
        content: str
        duration: float






