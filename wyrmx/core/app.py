from fastapi import FastAPI
from .router import bindRouters

class WyrmxAPP: 

    def __init__(self):

        self.__app = FastAPI()
        bindRouters(self.__app)
