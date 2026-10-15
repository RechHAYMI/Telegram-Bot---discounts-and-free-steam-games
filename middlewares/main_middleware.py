from aiogram import BaseMiddleware
from typing import Dict, Any, Callable

class ShadowMiddleware(BaseMiddleware):

    async def __call__(self, handler, event, data): 
        pool = data.get("pool")
        db = DatabaseLayer(pool)
        data["db"] = db
        user = event.from_user 


        if user is not None and pool: 
            await db.add_user(user.id, user.username, user.first_name)
            
        data["is_admin"] = (user.id == ADMIN_ID) 
        return await handler(event, data) 