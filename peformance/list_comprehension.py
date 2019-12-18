# example

# {
# Better

cube_numbers = [n ** 3 for n in range(1, 10) if n % 2 == 1]

# Less
cube_numbers2 = []
for n in range(0, 10):
    if n % 2 == 1:
        cube_numbers2.append(n ** 3)

# }

# 2. Remember the built-In functions.
pass

# 3. Use xrange() instead of range() only python 2
import sys

numbers = range(1, 1000000)
print(sys.getsizeof(numbers))

# 4. try it generator.
pass

# 5. Use “in” if possible.
for name in []:
    print('{} is a member'.format(name))

# 6. Be lazy with your module importing.
pass

# 7. Use sets and unions.
# {
# Better

a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5, 6]

overlaps = set(a) & set(b)

print(overlaps)

# Less
a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5, 6]

overlaps = []
for x in a:
    for y in b:
        if x == y:
            overlaps.append(x)

print(overlaps)

# }

# 8. Remember to use multiple assignment.
first_name, last_name, city = "Kevin", "Cunningham", "Brighton"
# You can use this method to swap the values of variables.

# {
# Better
x, y = y, x

# Less
temp = x
x = y
y = temp
# }

# 9. Avoid global variables.
pass

# 10. Use join() to concatenate strings.
# {
# Better

new = " ".join(["This", "will", "only", "create", "one", "string", "and", "we", "can", "add", "spaces."])
print(new)

# Less
new = "This" + "is" + "going" + "to" + "require" + "a" + "new" + "string" + "for" + "every" + "word"
print(new)

# }

# 11. Keep up-to-date on the latest Python releases.
pass

# 12. Use “while 1” for an infinite loop.
pass

# 13. Try another way.
pass

# 14. Exit early.
# Try to leave a function as soon as you know it can do no more meaningful work.
pass

# 15. Learn itertools.
import itertools

iter = itertools.permutations(["Alice", "Bob", "Carol"])
list(iter)

# 16. Try decorator caching.
import functools


@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# 17. Use keys for sorts.
import operator

my_list = [("Josh", "Grobin", "Singer"), ("Marco", "Polo", "General"), ("Ada", "Lovelace", "Scientist")]
my_list.sort(key=operator.itemgetter(0))
print(my_list)
