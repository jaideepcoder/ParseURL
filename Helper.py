class Switch(object):
    value = None

    def __new__(cls, *args, **kwargs):
        cls.value = args[0]
        return True


def case(*args):
    return any((arg == Switch.value for arg in args))