# TODO Add typing
def repeat_some_string(x: str, y: int):
    return [x for n in range(y)]


# TODO Prevent user from triggering stuff he shouldn't
def critical_func(some_var, key_arg=True, *, critical_switch=False):
    if critical_switch:
        print("PANIC, NOK")
        exit
    else:
        print("OK")


# TODO Make function take unlimited amount of args
def extendable_func(*args, **kwargs):
    """
    Prints models:`app.someModel` and kwargs
    """
    for arg in args:
        print(arg)

    for key, value in kwargs.items():
        print(key, value)


if __name__ == "__main__":
    extendable_func(1, 2, 3, 4, "alamakota", some_var="test", other_var=1)
