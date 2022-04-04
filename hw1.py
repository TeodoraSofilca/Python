# 1. declararea unei liste care să conțină elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine)
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

print('2. ---------------------------------------------------')
# 2. afișarea unei alte liste ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
my_list_sorted_asc = list(my_list)
my_list_sorted_asc.sort()
print(my_list_sorted_asc, '\n')

print('3. ---------------------------------------------------')
# 3. afișarea unei liste ordonată descendent (lista inițială trebuie păstrată în aceeași formă)
my_list_sorted_desc = list(my_list)
my_list_sorted_desc.sort(reverse=True)
print(my_list_sorted_desc, '\n')

print('4. ---------------------------------------------------')
# 4. afișarea numerelor de pe pozitii pare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)
my_list_sliced_even = my_list[::2]
print(my_list_sliced_even, '\n')

print('5. ---------------------------------------------------')
# 5. afișarea numerelor de pe pozitii impare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)
my_list_sliced_odd = my_list[1::2]
print(my_list_sliced_odd, '\n')

print('6. ---------------------------------------------------')
# 6. afișarea elementelor multipli ai lui 3
for el in my_list:
    if el % 3 == 0:
        print(el, end=" ")