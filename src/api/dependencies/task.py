from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.services.task import TaskService
from src.repositories.task import TaskRepository

from src.db.session.session import get_session


def get_task_repository():
    return TaskRepository()


async def get_task_service(
        session: AsyncSession = Depends(get_session),
        repository: TaskRepository = Depends(get_task_repository)
) -> TaskService:
    return TaskService(session, repository)
