from pydantic import BaseModel

class ResourceBase(BaseModel):
    name: str
    description: str | None = None
    location: str | None = None

class ResourceCreate(ResourceBase):
    pass

class ResourceOut(ResourceBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
