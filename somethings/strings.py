"""not should use it """
# create a concatenated string from 0 to 19 (e.g. "012..1819")
nums = ""
for n in range(20):
    nums += str(n)  # slow and inefficient
print(nums)

""" This code bellow is the best"""
# create a concatenated string from 0 to 19 (e.g. "012..1819")
nums = [str(n) for n in range(20)]
print("".join(nums))

"""concat two strings"""
foo = 'foo'
bar = 'bar'

foobar = '%s%s' % (foo, bar)  # It is OK
foobar = '{0}{1}'.format(foo, bar)  # It is better
foobar = '{foo}{bar}'.format(foo=foo, bar=bar)  # It is best
