import inspect
# functions
def whoami():
    return inspect.stack()[1][3]
def myfun():
    x=whoami()
    print(x)

myfun()