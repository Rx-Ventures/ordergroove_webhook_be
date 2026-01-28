import logging

from redis.asyncio import Redis

from app.core.config import settings

logger = logging.getLogger(__name__)


class RedisClient:
    def __init__(self):
        self._client: Redis | None = None

    async def connect(self) -> None:
        try:
            self._client = Redis.from_url(
                settings.REDIS_URL,
                decode_responses=True,
            )
            await self._client.ping()
            logger.info("Redis connected successfully")
        except Exception as e:
            logger.error(f"Redis connection failed: {e}")
            self._client = None

    async def disconnect(self) -> None:
        if self._client:
            await self._client.close()
            logger.info("Redis disconnected")

    async def get(self, key: str) -> str | None:
        if not self._client:
            return None
        try:
            return await self._client.get(key)
        except Exception as e:
            logger.error(f"Redis get error: {e}")
            return None

    async def set(
        self, 
        key: str, 
        value: str, 
        ttl: int | None = None
    ) -> bool:
        if not self._client:
            return False
        try:
            await self._client.set(key, value, ex=ttl)
            return True
        except Exception as e:
            logger.error(f"Redis set error: {e}")
            return False

    async def delete(self, key: str) -> bool:
        if not self._client:
            return False
        try:
            await self._client.delete(key)
            return True
        except Exception as e:
            logger.error(f"Redis delete error: {e}")
            return False


redis_client = RedisClient()