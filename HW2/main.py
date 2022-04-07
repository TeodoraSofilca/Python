import mymodule

def my_func(*args, **kwargs):
    sum = 0
    for arg in args:
        if type(arg) == int:
            sum += arg
    print(sum)

print("3 examples of my_func")
my_func(1, 5, -3, 'abc', [12, 56, 'cad'])
my_func()
my_func(2, 4, 'abc', param_1=2)

print('----------------------------------------------------------')


def isint_func(*args, **kwargs):
    param_1 = input("Please enter an integer: ")
    if type(param_1) == int:
        print(param_1)
    elif type(param_1) != int:
        print('0')
    print(type(param_1)) # input() vine cu type de str, asadar niciun numar introdus de la tastatura nu va fi int
    # decat daca il vom  converti la int


isint_func()




