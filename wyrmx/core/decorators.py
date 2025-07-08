from typing import Any
from fastapi import APIRouter
from .router import registerRouter

def singleton(cls):
    """
    Decorator to mark a class as a singleton.
    """

    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


def controller(routerPrefix: str):
    """
    Decorator to mark a class as a controller with a base route.
    Also enforces singleton.
    """

    def bindEndpoints(instance: Any):

         for attr_name in dir(instance):
            attr = getattr(instance, attr_name)

            if callable(attr) and hasattr(attr, "_route_info"):
                instance.router.add_api_route(
                    attr._route_info["path"],
                    attr,
                    methods=attr._route_info["methods"]
                )


    def decorator(cls):
        setattr(cls, "isController", True)
        setattr(cls, "routerPrefix", routerPrefix)
        setattr(cls, "router", APIRouter(prefix=f"/{routerPrefix}"))

        bindEndpoints(singleton(cls)())
        registerRouter(cls.router)

        return singleton(cls)
    
    return decorator


def service(cls):
    """
    Decorator to mark a class as a service with a base route.
    Also enforces singleton.
    """

    setattr(cls, "isService", True)
    return singleton(cls)


def model(cls):
    setattr(cls, "isModel", True)
    return cls



