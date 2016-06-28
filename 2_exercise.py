""" Module for practise python basics concepts: 2_exercise. """

list1 = ["primero", 2, "3.5", 4.0, "ultimo"]

""" ¿list length?. """
print(len(list1))

""" List length multiplied by the second value. """
print(len(list1) * list1[1])

""" Second multiplied by third. """
print(list1[1] * float(list1[2]))

""" Is the number 2 on the list? And 2.0? """
# print(type(2.0),type(2))
print(2 in list1, 2.0 in list1)

""" Delete first element. """
del list1[0]
print(list1)

"""  Delete last 2 elements simultaneously. """
del list1[len(list1) - 2:]
print(list1)

""" Is list empty? """
print(list1 == [])

""" Add "nuevo ultimo". """
list1.append("nuevo ultimo")
print(list1)
