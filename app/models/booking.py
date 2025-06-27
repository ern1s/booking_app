from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    resource_id = Column(Integer, ForeignKey("resources.id"))
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    user = relationship("User", back_populates="bookings")
    resource = relationship("Resource", back_populates="bookings")
