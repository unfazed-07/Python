def repeat(func):
    def wrapper(*args, **kwargs):
        for _ in range(5):
            func(*args, **kwargs)
        return wrapper
    
@repeat
def greet(name):
    print(f"Hello, {name}")

greet("Steve")