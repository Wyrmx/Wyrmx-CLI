


def get(path: str):

    def decorator(func):
        func._route_info = {
            "path": f"/{path}",
            "methods": ["GET"]
        }
        return func
    
    return decorator



def post(path: str):

    def decorator(func):
        func._route_info = {
            "path": f"/{path}",
            "methods": ["POST"]
        }
        return func
    
    return decorator




def patch(path: str):

    def decorator(func):
        func._route_info = {
            "path": f"/{path}",
            "methods": ["PATCH"]
        }
        return func
    
    return decorator



def put(path: str):

    def decorator(func):
        func._route_info = {
            "path": f"/{path}",
            "methods": ["PUT"]
        }
        return func
    
    return decorator




def delete(path: str):

    def decorator(func):
        func._route_info = {
            "path": f"/{path}",
            "methods": ["DELETE"]
        }
        return func
    
    return decorator



def options(path: str):

    def decorator(func):
        func._route_info = {
            "path": f"/{path}",
            "methods": ["DELETE"]
        }
        return func
    
    return decorator
