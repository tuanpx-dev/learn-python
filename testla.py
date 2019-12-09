from multiprocessing import Pool
import os


def f(x):
    return x * x


if __name__ == '__main__':
    with Pool() as p:
        print(dir(p))
        print(os.cpu_count())
        print(p._processes)
        print(p.map(f, [1, 2, 3,4,5,6,7,8,9,10,11,12,13,14]))
