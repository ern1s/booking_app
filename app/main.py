from fastapi import FastAPI
from app.routes import user, resource, booking
from app.core.database import Base, engine
from app.websockets.routes import router as ws_router

app = FastAPI()

app.include_router(user.router)
app.include_router(resource.router)
app.include_router(booking.router)
app.include_router(ws_router)

Base.metadata.create_all(bind=engine)
