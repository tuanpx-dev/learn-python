import itertools


class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age


a = A('tuan', 10)
a1 = A('tuan1', 11)
a2 = A('tuan2', 12)
a3 = A('tuan3', 19)
a4 = A('tuan4', 14)
a5 = A('tuan5', 18)
a6 = A('tuan6', 16)
a7 = A('tuan7', 17)

data = [a, a1, a2, a3, a4, a5, a6, a7]
s = sorted(data, key=lambda k: k.age)
print(type(s))
u = lambda s: s.age

m = itertools.groupby(sorted(data, key=lambda k: k.age), lambda k: k.age)
for i, j in m:
    print(i, j)
