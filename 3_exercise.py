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

""" Module for practise python basics concepts: 3_exercise. """

import re

""" Print out next sequence [0, 1, 2 . . . 100]. """
print([num for num in range(101)])

""" Print out next sequence [0, 2, 4 . . . 200]. """
print([num for num in range(0, 201, 2)])

""" Print out next sequence [86, 84, 82 . . . 14]. """
print([num for num in range(86, 13, -2)])

""" Print out next sequence [10, 9, 8 . . . 0]. """
print([num for num in range(10, -1, -1)])

""" Print out power of 2 less than or equal to 2046, using while loop. """
pow_x = 0
l_pow2 = []
while 2 ** pow_x <= 2048:
    l_pow2.append(2 ** pow_x)
    pow_x += 1
print(l_pow2)

""" Read user values until pair number, using while loop. """
while True:
    pair_x = input("Pair number: ")
    if pair_x.isdigit():
        if int(pair_x) % 2 == 0:
            print("{} is pair".format(pair_x))
            break
        else:
            print("{} is not pair".format(pair_x))
    else:
        print("{} is not a number".format(pair_x))

""" Print out first 15 powers of 2. """
print([pot2 ** 2 for pot2 in range(15)])

""" Read a string and on each letter denote if is a vowel or consonant"""
print(['Not a letter' if not let.isalpha() else 'V' if let.lower() in (
    'a', 'e', 'i', 'o', 'u') else 'C' for let in
       input("Say something: ")])

""" With two list of ints, 'numeros1' and 'numeros2', create other which contains those
values of the first that are
included in the second. Intersection of both list. """
numeros1 = [0, 1, 2, 3, 4]
numeros2 = [2, 4, 6, 8, 9]
# print([inter for inter in numeros1 if inter in numeros2])
print(list(set(numeros1).intersection(numeros2)))

""" With two list of ints, 'numeros1' and 'numeros2' with the same length, create other
with the first element is the
product of the first element of both and successively. """
print(
    [num1 * num2 for i, num1 in enumerate(numeros1) for j, num2 in enumerate(numeros2) if
     i == j])

""" With two list of ints, 'numeros1' and 'numeros2', storage in one the results of
multiply each elements of
'numeros1' by each elements of 'numeros2'. The resulting list will have len(numeros1) *
len(numeros2) elements. """
print([num1 * num2 for num1 in numeros1 for num2 in numeros2])

""" For each next strings stored in a list, print out the index and the string,
and indicate if the word is too short
(five or less characters) or too long (more than five characters). """
t_strings = ["Hola", "Mundialmente", "Mundo"]
# [print(i, "-> LONG") if len(t_str0) > 5 else print(i, "-> SHORT") for i, t_str0 in
# enumerate(t_strings)]
print(["LONG" if len(t_str1) > 5 else "SHORT" for i, t_str1 in enumerate(t_strings)])

""" Get integer list and calculate the arithmetic average. """
l_ints = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 0
for ent in l_ints:
    x += ent
print(x / len(l_ints))

""" Read a user string and print out a friendly message if the string is a palindrome,
ie: this spanish palindromes:
                  La ruta natural
           ¿Son mulas o cívicos alumnos?
          Dábale arroz a la zorra el abad
"""
palin = "Son mulas o civicos alumnos"
palin = re.sub('[\s+]', '', palin).lower()
if 0 in [1 if palin[i] == palin[(len(palin) - 1) - i] else 0 for i in
         range(int(len(palin) / 2))]:
    print("THIS IS NOT A PALINDROME")
else:
    print("NICE PALINDROME")
