def decarator_exception():
    def fun2(fun1):
        def wrapper(*args,**kwargs):
            try:
                return fun1(*args,**kwargs)
            except Exception as err:
                return err
        return wrapper
    return fun2


@decarator_exception()
def fun1(a, b):
    return a+b

print(fun1(1,"1"))