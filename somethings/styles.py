"""
    Bad
"""
x = 2
print('one')
print('two')

if x == 1: print('one')

# if <complex comparison> and <other complex comparison>:
#     # do something


"""
    Good  should follow
"""
print('one')
print('two')

if x == 1:
    print('one')
"""
cond1 = <complex comparison>
cond2 = <other complex comparison>
if cond1 and cond2:
    # do something
"""









"""
    How to return value when processing a function
"""


def complex_function(a, b, c):
    if not a:
        return None  # Raising an exception might be better
    if not b:
        return None  # Raising an exception might be better
    # Some complex code trying to compute x from a, b and c
    # Resist temptation to return x if succeeded
    if not x:
        pass
        # Some Plan-B computation of x
    return x  # One single exit point for the returned value x will help
    # when maintaining the code.








"""
    Created a lists with N 
"""
four_nones = [None] * 4
print(four_nones)
four_lists = [[] for __ in range(4)]
print(four_lists)







"""
    Create a string from list character
"""
letters = ['s', 'p', 'a', 'm']
word = ''.join(letters)







"""
    Search in lists and search in tuple
    if have more data should use tuple because performance 
"""
s = set(['s', 'p', 'a', 'm'])
l = ['s', 'p', 'a', 'm']


def lookup_set(s):
    return 's' in s


def lookup_list(l):
    return 's' in l






"""
    Check a variable equals constant 
"""

# Bad not use
attr = 4
if attr == True:
    print('True!')

if attr == None:
    print('attr is None!')

# Use it
# Just check the value
if attr:
    print('attr is truthy!')

# or check for the opposite
if not attr:
    print('attr is falsey!')

# or, since None is considered false, explicitly check for it
if attr is None:
    print('attr is None!')







"""
    Access a dictionary
"""

# Bad doesn't use it
d = {'hello': 'world'}
if d.has_key('hello'):
    print(d['hello'])  # prints 'world'
else:
    print('default_value')

# Good
d = {'hello': 'world'}

print(d.get('hello', 'default_value'))  # prints 'world'
print(d.get('thingy', 'default_value'))  # prints 'default_value'

# Or:
if 'hello' in d:
    print(d['hello'])





# needlessly allocates a list of all (gpa, name) entires in memory
valedictorian = max([(student.gpa, student.name) for student in graduates])
