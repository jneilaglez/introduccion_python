""" Module for practise python basics concepts: 9_exercise. """

x = [8, 2, 3, -1, 2, -5, 7]
people = ["Sara", "Pedro", "Miguel"]

""" The square of 3 of each element of list x. """
print([i ** 3 for i in x])
print(list(map(lambda x: x ** 3, x)))

""" The square of 2 of each odd elements of list x. """
print([i ** 2 for i in x if i % 2 != 0])
print(list(map(lambda x: x ** 2,list(filter(lambda x: x % 2 != 0, x)))))

""" The square of 2 of pair and positive elements of list x. """
print([i ** 2 for i in x if i % 2 == 0 and i > 0])
print(list(map(lambda x: x ** 2,list(filter(lambda x: x % 2 == 0 and x > 0, x)))))

""" Elements of people with more than 5 characters. """
print([i for i in people if len(i) > 5])
print(list(filter(lambda x: len(x) > 5, people)))

""" Elements of list people which contain the 'o' vowel. """
print([i for i in people if 'o' in i])
print(list(filter(lambda x: 'o' in x, people)))

""" Elements of list people which contain 'e' vowel and have less than 6 
characters. """
print([i for i in people if 'i' in i and len(i) >= 6])
print(list(filter(lambda x: 'i' in x and len(x) >= 6, people)))