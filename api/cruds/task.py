from typing import List, Tuple, Optional

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession


from datetime import date


import api.models.task as task_model
import api.schemas.task as task_schema


async def create_task(
    db: AsyncSession, task_create: task_schema.TaskCreate
) -> task_model.Task:
    task = task_model.Task(**task_create.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task




async def get_tasks_with_done(db: AsyncSession) -> List[Tuple[int, str, bool]]:
    result: Result = await (
        db.execute(
            select(
                task_model.Task.id,
                task_model.Task.title,
                task_model.Task.deadline,
                task_model.Done.id.isnot(None).label("done"),
            )
            .outerjoin(task_model.Done)
        )
    )
    return result.all()





async def get_task(db: AsyncSession, task_id: int) -> Optional[task_model.Task]:
    result: Result = await db.execute(
        select(task_model.Task).filter(task_model.Task.id == task_id)
    )
    task: Optional[Tuple[task_model.Task]] = result.first()
    return task[0] if task is not None else None

async def delete_task(db: AsyncSession, original: task_model.Task) -> None:
    await db.delete(original)
    await db.commit()


async def update_task(
    db: AsyncSession, task_create: task_schema.TaskCreate, original: task_model.Task
) -> task_model.Task:
    original.title = task_create.title
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original



async def get_tasks_by_deadline_exact(db: AsyncSession, keyword: str):
    result = await db.execute(
        select(task_model.Task).filter(task_model.Task.deadline == keyword)
    )
    return result.all()



async def get_tasks_by_today_deadline(db: AsyncSession):
    today_str = date.today().strftime("%Y-%m-%d")
    result = await db.execute(
        select(
            task_model.Task.id,
            task_model.Task.title,
            task_model.Task.deadline,
            task_model.Done.id.isnot(None).label("done"),
        )
        .outerjoin(task_model.Done)
        .filter(task_model.Task.deadline == today_str) 
    )
    return result.all()
