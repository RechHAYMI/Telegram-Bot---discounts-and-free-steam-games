import time
from aiogram import BaseMiddleware

class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, limit=1.0):
        self.notebook = {}
        self.limit = limit

    async def __call__(self, handler, event, data):
        user_id = event.from_user.id
        now = time.time()
        if user_id in self.notebook:
            delta = now - self.notebook[user_id]
            if delta < self.limit:
                return None
        self.notebook[user_id] = now
        return await handler(event, data)