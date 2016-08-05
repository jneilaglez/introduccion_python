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
del list1[2:]
print(list1)

""" Is list empty? """
print(list1 == [])

""" Add "nuevo ultimo". """
list1.append("nuevo ultimo")
print(list1)
