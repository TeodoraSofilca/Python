def get_sum(n):
    if n == 0:
        return 0
    return n + get_sum(n - 1)


print(get_sum(3), "recursive sum")
print('----------------------------------------------------------')

def get_sum_even(n):
    sum = 0
    if n == 0:
        return 0
    if n % 2 == 0:
        sum += n
    return sum + get_sum_even(n - 1)


print(get_sum_even(10), "recursive even sum")
print('----------------------------------------------------------')


def get_sum_odd(n):
    sum = 0
    if n == 0:
        return 0
    if n % 2 != 0:
        sum += n
    return sum + get_sum_odd(n - 1)


print(get_sum_odd(10), "recursive odd sum")
print('----------------------------------------------------------')
