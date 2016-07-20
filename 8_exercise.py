""" Module for practise python basics concepts: 8_exercise. 

Dinamic objects:
x -- List of numbers
y -- List of numbers
copy_sorted -- Sorted list
copy_sorted_reverse -- Sorted reverse list
square_2 -- Dictionary of numbers
num_t -- Dictionary of numbers
""" 

def n_num_list(lista, n):
    """
    Returns a list of n length without repeated numbers.
    :param lista: a list of numbers
    :param n: length of the result list
    :return: list without repeated numbers
    """
    may_n = []
    for may in lista:
        if may not in may_n and len(may_n) != n:
            may_n.append(may)
    return may_n
    
x = [8, 2, 3, 7, 5, 3, 7, 3, 1]
copy_sorted = sorted(x)
copy_sorted_reverse = sorted(x,reverse=True)

""" Highest value of the list. """
#print(copy_sorted[len(x) - 1])
print(max(x))

""" Lowest value of the list. """
#print(copy_sorted[0])
print(min(x))

""" 3 highest value of the list. """
print(n_num_list(copy_sorted_reverse,3))

""" Highest value of three first numbers of the list. """
#print(sorted(x[:3])[-1])
print(max(x[:3]))

""" Lowest value of four last numbers of the list. """
#print(sorted(x[-4:])[0])
print(min(x[-4:]))

""" Sum of five highest numbers of the list. """
print(sum(n_num_list(copy_sorted_reverse,5)))

""" Sum of 3 lowest numbers of the list. """
print(sum(n_num_list(copy_sorted,3)))

x = [8, 2, 3, 2, 2]
y = [8, 2, 3, 2, 9]

""" How many elements does x have if repeated numbers are deleted? """
print(len(set(x)))

""" List which contains the concatenation of both. """
print(x + y)

""" List which contains the union of both without duplicates. """
print(list(set(x).union(set(y))))

""" A set that contains the intersection of both. """
print(list(set(x).intersection(set(y))))

""" A dictionary that each integer of the list, x stores his square of 2. """
square_2 = {}
for i in list(set(x).union(set(y))):
    square_2[i] = i ** 2
print(square_2)

""" A dictionary that contains how many times each integer appears in the list 
y """
num_t = dict()
for i in y:
    if i not in num_t:
        num_t[i] = 1
    else:
        num_t[i] += 1
print(num_t)