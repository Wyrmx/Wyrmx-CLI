from fastapi import FastAPI
from .router import bindRouters

class WyrmxAPP: 

    def __init__(self):

        self.__app = FastAPI()
        bindRouters(self.__app)
    
    async def __call__(self, scope, receive, send):
        await self.__app(scope, receive, send)
