def parent(num):
    a = num * num
    print("Printing from the parent() function")

    def first_child(a):
        print("Printing from the first_child() function", a+2)

    def second_child():
        print("Printing from the second_child() function")

    if num == 1:
        return first_child
    else:
        return second_child


a = parent(1)
# b = parent(2)

# a()
a(1)
