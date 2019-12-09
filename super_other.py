def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def say_whee(a):
    a = a+1
    print("Whee!",a)

# a = say_whee(1)
say_whee = my_decorator(say_whee)
say_whee()
