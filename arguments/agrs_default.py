def function_stupid(name):
    name = name if name else 'world stupid'
    print(name)


def function_smart(name: str = 'world smart'):
    print(name)


function_stupid('this is function bad')
function_smart('this is function smart')
