from django.test import TestCase

# Create your tests here.
from django.utils.functional import partition

# list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = partition(lambda a: a > 2, range(6))
print(k)
