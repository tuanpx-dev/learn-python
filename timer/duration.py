from timer.timer_decorator import timer


@timer
def do_somethings(number):
    for _ in range(number):
        sum([i ** 2 for i in range(1000)])


do_somethings(1000)
