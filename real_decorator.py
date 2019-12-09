import functools


def decorator_like(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value_a = kwargs.get('value_a')
        value_b = kwargs.get('value_b')
        f = 'do something before {sum}'.format(sum=value_a + value_b)
        value = func(*args, **kwargs)
        f1 = 'do something after {bla}'.format(bla=value_a * value_b)
        concate = f + value + f1
        return concate

    return wrapper_decorator
