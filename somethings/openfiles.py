from contextlib import contextmanager


class CustomOpen(object):
    """
    Open file simple su dung tiep can lop
    """

    def __init__(self, filename):
        self.file = open(filename)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with CustomOpen('file') as f:
    contents = f.read()


@contextmanager
def custom_open(filename):
    """
    Cac mo file  bang contextmanager tuy thuoc boi canh
    :param filename:
    :return:
    """
    f = open(filename)
    try:
        yield f
    finally:
        f.close()


with custom_open('file') as f:
    contents = f.read
