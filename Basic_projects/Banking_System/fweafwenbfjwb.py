def repeat(n):   
    def decorator(func):
        def wrapper(*arg, **kwargs):
            print("Calling wrapper")
            for _ in range(n):
                func(*arg, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(*name, **n):
    print(f"Hello, {name} {n}")

greet("Norm","grrtt", city="Delhii")