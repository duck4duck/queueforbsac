from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from ..config import settings


class DatabaseHelper:
    def __init__(
        self,
        url: str,
        echo: bool = False,
        echo_pool: bool = False,
        max_overflow: int = 10,
        pool_size: int = 5,
    ):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
            pool_size=pool_size,
            echo_pool=echo_pool,
            max_overflow=max_overflow,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine, autocommit=False, expire_on_commit=False, autoflush=False
        )

        async def dispose(self):
            await self.engine.dispose()

        async def get_session(self):
            async with self.session_factory() as session:
                yield session


db_helper = DatabaseHelper(
    str(settings.db.url),
    echo=settings.db.echo,
    echo_pool=settings.db.echo_pool,
    max_overflow=settings.db.max_overflow,
    pool_size=settings.db.pool_size,
)
