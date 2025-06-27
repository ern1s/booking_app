from datetime import datetime
from pydantic import BaseModel

class BookingBase(BaseModel):
    resource_id: int
    start_time: datetime
    end_time: datetime

class BookingCreate(BookingBase):
    pass

class BookingOut(BookingBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
