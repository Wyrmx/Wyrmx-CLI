

def singleton(cls):

    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


def controller(path: str):
    """
    Decorator to mark a class as a controller with a base route.
    Also enforces singleton.
    """
    def decorator(cls):
        setattr(cls, "isController", True)
        setattr(cls, "basePath", path)
        return singleton(cls)
    
    return decorator


def service(cls):
    setattr(cls, "isService", True)
    return singleton(cls)


def model(cls):
    setattr(cls, "isModel", True)
    return cls



