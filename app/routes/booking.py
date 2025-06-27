from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import asyncio

from app.core.deps import get_current_user, get_db
from app.schemas.booking import BookingCreate, BookingOut
from app.crud import booking as booking_crud
from app.models.user import User
from app.websockets.manager import manager

router = APIRouter(prefix="/bookings", tags=["Bookings"])

@router.post("/", response_model=BookingOut)
async def create_booking(
    booking: BookingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = booking_crud.create_booking(db, booking, current_user.id)
    if result is None:
        raise HTTPException(status_code=400, detail="Время занято")
    
    # отправка уведомления по WebSocket
    asyncio.create_task(
        manager.broadcast(
            f"📢 Новое бронирование пользователем {current_user.email}: "
            f"ресурс {booking.resource_id} с {booking.start_time} по {booking.end_time}"
        )
    )
    return result

@router.get("/", response_model=list[BookingOut])
def list_bookings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return booking_crud.get_bookings(db)
