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


def isint_func():
    try:
        param_1 = int(input("Please enter an integer: "))
    except ValueError:
        return 0
    else:
        return param_1


print(isint_func())
