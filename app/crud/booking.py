from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models.booking import Booking
from app.schemas.booking import BookingCreate
from datetime import datetime

def is_available(db: Session, resource_id: int, start_time: datetime, end_time: datetime) -> bool:
    """Проверка: нет ли бронирований, пересекающихся по времени"""
    overlapping = db.query(Booking).filter(
        Booking.resource_id == resource_id,
        and_(
            Booking.start_time < end_time,
            Booking.end_time > start_time
        )
    ).first()
    return overlapping is None

def create_booking(db: Session, booking: BookingCreate, user_id: int):
    if not is_available(db, booking.resource_id, booking.start_time, booking.end_time):
        return None
    db_booking = Booking(
        resource_id=booking.resource_id,
        user_id=user_id,
        start_time=booking.start_time,
        end_time=booking.end_time
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

def get_bookings(db: Session):
    return db.query(Booking).all()
