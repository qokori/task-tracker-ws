from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.core.config.settings import settings


async def get_session() -> AsyncGenerator[AsyncSession | None]:
    async with settings.async_session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
