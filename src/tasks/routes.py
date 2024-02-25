from fastapi import APIRouter, FastAPI
from typing import List

from src.tasks.schemas import TaskResponse

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


@router.get("/")
def list_tasks() -> List[TaskResponse]:
    raise NotImplementedError()


@router.post("/")
def create_task() -> TaskResponse:
    raise NotImplementedError()


@router.delete("/{task_id}")
def delete_task(task_id: int) -> TaskResponse:
    raise NotImplementedError()
