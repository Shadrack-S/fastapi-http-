from enum import Enum
from pydantic import BaseModel, Field

class QueryParams(BaseModel):
    name: str | None = None
    page_size: int = 10
    search_value: str | None = None
    is_active: bool | None = None



class TaskStatus(str, Enum):
    ongoing = "ongoing"
    in_progress = "in_progress"
    done = "done"

class TodoRequest(BaseModel):
    task_name: str = Field(
        ...,
        example="Todo work"
    )
    task_description: str = Field(
        ...,
        example="Task description"
    )
    status: TaskStatus = Field(
        ...,
        example="ongoing"
    )


class UpdateTodo(TodoRequest):
    id: int

class UpdateTodoResponse(UpdateTodo):
    pass