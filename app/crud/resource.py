from sqlalchemy.orm import Session
from app.models.resource import Resource
from app.schemas.resource import ResourceCreate

def create_resource(db: Session, resource: ResourceCreate, owner_id: int):
    db_resource = Resource(**resource.dict(), owner_id=owner_id)
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

def get_resources(db: Session):
    return db.query(Resource).all()

def get_resource(db: Session, resource_id: int):
    return db.query(Resource).filter(Resource.id == resource_id).first()

def delete_resource(db: Session, resource_id: int):
    resource = db.query(Resource).filter(Resource.id == resource_id).first()
    if resource:
        db.delete(resource)
        db.commit()
        return True
    return False
