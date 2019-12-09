from decorators import do_twice


@do_twice
def say_whee():
    print("Whee!")


@do_twice
def greet(name):
    print(f"Hello {name}")


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


print(say_whee.__name__)
help(say_whee)
# greet('super man')
# hi_abc = return_greeting("world")
