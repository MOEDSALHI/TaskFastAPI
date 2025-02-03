from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    title: str
    description: str
    completed: bool


class TaskCreate(TaskBase):
    pass


class TaskResponse(TaskBase):
    id: int
    project_id: int

    # class Config:
    #     from_attributes = True
    model_config = ConfigDict(from_attributes=True)
