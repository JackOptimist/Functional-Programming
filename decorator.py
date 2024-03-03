def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)

        return result

    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def subtract(x, y):
    return x - y

print(add(2, 3))
print(subtract(5, 2))
