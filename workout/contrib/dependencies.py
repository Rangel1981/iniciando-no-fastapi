from typing import Annotated
from workout.configs.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

DatabaseDependency = Annotated[AsyncSession, Depends(get_session)]
