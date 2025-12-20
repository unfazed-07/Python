import functools

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func} with {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@debug
def add(a,b):
    return a+b

print(add(2,3))
print(add.__name__)

import time
def factorial(n):
    time.sleep(1)
    print(f"Calulating {n}!")
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(6))