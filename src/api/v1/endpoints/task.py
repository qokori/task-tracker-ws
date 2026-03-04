from uuid import UUID

from fastapi import APIRouter, Depends
from src.services.task import TaskService

from src.api.dependencies.task import get_task_service

f
from src.api.schemas.task import TaskFetchListParamsSchema, TaskResponseSchema, TaskCreateSchema, TaskUpdateSchema

router = APIRouter(prefix='/tasks', tags=['Task'])


@router.get('', response_model=list[TaskResponseSchema])
async def fetch_list(
        input_dto: TaskFetchListParamsSchema,
        service: TaskService = Depends(get_task_service)
) -> list[TaskResponseSchema]:
    return await service.fetch_list(input_dto)


@router.post('', response_model=TaskResponseSchema)
async def create(
        input_dto: TaskCreateSchema,
        service: TaskService = Depends(get_task_service)
) -> TaskResponseSchema:
    return await service.create(input_dto)


@router.get('/{task_id}', response_model=TaskResponseSchema)
async def fetch_by_id(
        task_id: UUID,
        service: TaskService = Depends(get_task_service)
) -> TaskResponseSchema:
    return await service.fetch_by_id(task_id)


@router.get('/{task_id}', response_model=TaskResponseSchema)
async def update(
        task_id: UUID,
        input_dto: TaskUpdateSchema,
        service: TaskService = Depends(get_task_service)
) -> TaskResponseSchema:
    return await service.update(task_id, input_dto)


@router.get('/{task_id}')
async def delete(
        task_id: UUID,
        service: TaskService = Depends(get_task_service)
):
    return await service.delete(task_id)
