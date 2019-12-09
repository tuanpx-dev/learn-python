class A:
    def __init__(self):
        self.test = 'test'
        self.name = None


a = A()
t = None


def gen_t():
    t = 'kakak'
    return t


if hasattr(a, 'name'):
    print(a.name)
else:
    setattr(a, 'name', gen_t())
