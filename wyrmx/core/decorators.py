

def singleton(cls):

    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


def controller(cls):
    setattr(cls, "isController", True)
    return singleton(cls)


def service(cls):
    setattr(cls, "isService", True)
    return singleton(cls)


def model(cls):
    setattr(cls, "isModel", True)
    return cls



