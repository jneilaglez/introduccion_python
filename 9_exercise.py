"""
    Copyright (C) 2016  Jesús Neila González jneilaglez@gmail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

""" Module for practise python basics concepts: 9_exercise. """

x = [8, 2, 3, -1, 2, -5, 7]
people = ["Sara", "Pedro", "Miguel"]

""" The square of 3 of each element of list x. """
print([i ** 3 for i in x])
print(list(map(lambda a: a ** 3, x)))

""" The square of 2 of each odd elements of list x. """
print([i ** 2 for i in x if i % 2 != 0])
print(list(map(lambda a: a ** 2, list(filter(lambda a: a % 2 != 0, x)))))

""" The square of 2 of pair and positive elements of list x. """
print([i ** 2 for i in x if i % 2 == 0 and i > 0])
print(list(map(lambda a: a ** 2, list(filter(lambda a: a % 2 == 0 and a > 0, x)))))

""" Elements of people with more than 5 characters. """
print([i for i in people if len(i) > 5])
print(list(filter(lambda a: len(a) > 5, people)))

""" Elements of list people which contain the 'o' vowel. """
print([i for i in people if 'o' in i])
print(list(filter(lambda a: 'o' in a, people)))

""" Elements of list people which contain 'e' vowel and have less than 6 
characters. """
print([i for i in people if 'i' in i and len(i) >= 6])
print(list(filter(lambda a: 'i' in a and len(a) >= 6, people)))
