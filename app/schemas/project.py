from pydantic import BaseModel, ConfigDict


class ProjectBase(BaseModel):
    name: str
    description: str


class ProjectCreate(ProjectBase):
    pass


class ProjectResponse(ProjectBase):
    id: int
    owner_id: int

    model_config = ConfigDict(from_attributes=True)
