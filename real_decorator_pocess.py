from real_decorator import decorator_like


@decorator_like
def say_somethings(name, *args, **kwargs):
    f = 'hello {name}'.format(name=name)
    return f


will_say = say_somethings('world', value_a=2, value_b=5)
print(will_say)
