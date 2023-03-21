
def decorator(func):
    def wrapper():
        func()
        print("Let’s try that again!")
        func()
    return wrapper