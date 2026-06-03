from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling : {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finised : {func.__name__}")
        return result
    return wrapper

@log_activity
def brew_chai(type):
    print(f"Brewing : {type}")

brew_chai("Masala")