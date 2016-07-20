""" Module for practise python basics concepts: 5_exercise. """

numbers = range(2, 101, 2)
# numbers = range(100, 1, -2)
x = 11
t_list = [num for num in numbers]
r_exp = range(1, 11)

""" What do we have in the list? (Natural language)"""
help(numbers)

""" Last  10 elements of the list. """
# print([num for i, num in enumerate(numbers) if i > len(numbers) - 11])
print(t_list[-10:])

""" All elements except three first. """
# print([num for i, num in enumerate(numbers) if i > 2])
print(t_list[3:])

""" Minimum value on first fifteen elements. """
print(min(t_list[:15]))

""" Add minimum value at the end of the list. """
t_list.append(min(t_list[:]))
print(t_list)

""" Revert the order of the list. """
print([t_list[i] for i in range(len(t_list) - 1, -1, -1)])

""" The plus of the elements which have pair index. """
plus_pairs = 0
for i in range(len(t_list) - 1):
    if i % 2 == 0:
        plus_pairs = plus_pairs + t_list[i]
print(plus_pairs)

""" The arithmetic average of the elements. """
arith_average = 0
for num in t_list:
    arith_average += num
print(arith_average / len(t_list))

""" With [1, 2, 3, 4, 5], generate [1, 2, 3, 4, 5, 4, 3, 2, 1]. """
init_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# final_list = []
# for i in range(-init_list[-1], len(init_list) - 1, 1):
#     if i >= 0:
#         i = abs(i - init_list[-2]) - 1
#     final_list.append(init_list[i])
# print(final_list)
print([init_list[abs(i - init_list[-2]) - 1] if i >= 0 else init_list[i] for i in
       range(-init_list[-1], len(init_list) - 1, 1)])

""" Print out "sentido de la vida encontrado" if x is equal to 42 (if).
Else, print out "sigue buscando" (else). """
if x == 42:
    print("sentido de la vida encontrado")
else:
    print("sigue buscando")
""" If x is lower than 100, print out his value and increase by one.
Else, raise his value to the 2 power."""
if x < 100:
    print("Se va a incrementar el valor de {}".format(x))
    x += 1
else:
    x **= 2
""" If it is greater than 0 and pair, print out 'exacto.
Else, update the value by half. """
if x > 0 and x % 2 == 0:
    print("exacto")
else:
    x /= 2
""" If it is greater than 0, odd and lower or equal than 365, print out 'podría ser un
día' else 'no lo es'. """
if 365 >= x > 0 == x % 2:
    print("podría ser un día")
else:
    print("no lo es")
""" If the number is different from 0, print out 'algo es algo'.
Else, update the value by 100. """
if x == 0:
    print("algo es algo")
else:
    x = 100
print(x)

""" What do we have in the list? (Natural language)"""
# help(r_exp)
l_exp = [exp for exp in r_exp]

""" Add [18, 19] to the list. """
l_exp.append(18)
l_exp.append(19)
print(l_exp)

""" For each element, print out 2 ** x. """
print([2 ** exp for i, exp in enumerate(l_exp)])

""" For each element, raise his value to the 2 power and print out the result. """
print([exp ** 2 for exp in l_exp])

""" Reverse the order of the result of the previous exercise (Iterating backwards). """
print([l_exp[i] ** 2 for i in range(len(l_exp) - 1, -1, -1)])

""" For each element, test if 2 ** x is pair"""
print([2 ** exp % 2 == 0 for exp in l_exp])

""" Print out each element with his index. """
print(["Index: {1}, Value: {0}".format(exp, i) for i, exp in enumerate(l_exp)])

""" Using a variable in which we are going to store the result of the plus of 7 ** x.
Power of 7 for each element. """
t_res = 0
for exp in l_exp:
    t_res += 7 ** exp
print(t_res)

""" Stop the operations of the previous exercise if the value is greater than 200. """
t_res_gt = 0
for exp in l_exp:
    if t_res_gt > 200:
        break
    t_res_gt += 7 ** exp
print(t_res_gt)
