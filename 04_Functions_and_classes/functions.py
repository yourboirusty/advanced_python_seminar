# TODO Add typing
def repeat_some_string(x, y):
    return [x for n in range(y)]


# TODO Prevent user from triggering stuff he shouldn't
def critical_func(some_var, critical_switch=False):
    if critical_switch:
        print("PANIC, NOK")
        exit
    else:
        print("OK")


# TODO Make function take unlimited amount of args
def extendable_func():
    pass


if __name__ == "__main__":
    repeat_some_string('alamakota', 12)
