from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_db, get_current_user
from app.schemas.resource import ResourceCreate, ResourceOut
from app.crud import resource as resource_crud
from app.models.user import User

router = APIRouter(prefix="/resources", tags=["Resources"])

@router.post("/", response_model=ResourceOut)
def create_resource(
    resource: ResourceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return resource_crud.create_resource(db, resource, current_user.id)

@router.get("/", response_model=list[ResourceOut])
def list_resources(db: Session = Depends(get_db)):
    return resource_crud.get_resources(db)

@router.get("/{resource_id}", response_model=ResourceOut)
def get_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = resource_crud.get_resource(db, resource_id)
    if not resource:
        raise HTTPException(status_code=404, detail="Ресурс не найден")
    return resource

@router.delete("/{resource_id}")
def delete_resource(
    resource_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    success = resource_crud.delete_resource(db, resource_id)
    if not success:
        raise HTTPException(status_code=404, detail="Ресурс не найден")
    return {"ok": True}

@router.get("/my/", response_model=list[ResourceOut])
def get_my_resources(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    all_resources = resource_crud.get_resources(db)
    return [r for r in all_resources if r.owner_id == current_user.id]
