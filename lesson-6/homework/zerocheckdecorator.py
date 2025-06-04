def check(func):
    def wrapper(a,b):
        try:
            return func(a,b)
        except ZeroDivisionError:
            return "0 ga bo'lib bo'lmaydi!"
    return wrapper
@check
def div(a,b):
    return a/b

print(div(6,0))