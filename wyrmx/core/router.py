from fastapi import APIRouter, FastAPI

_registeredRouters: list[APIRouter] = []


def registerRouter(router: APIRouter): 
    _registeredRouters.append(router)

def bindRouters(app: FastAPI):
    for router in _registeredRouters: app.include_router(router)