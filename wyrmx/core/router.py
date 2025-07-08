from fastapi import APIRouter, FastAPI

registeredRouters: list[APIRouter] = []


def registerRouter(router: APIRouter): 
    registeredRouters.append(router)

def bindRouters(app: FastAPI):
    for router in registeredRouters: app.include_router(router)