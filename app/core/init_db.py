from app.core.database import Base, engine
from app.models import user

def init_db():
    Base.metadata.create_all(bind=engine)
