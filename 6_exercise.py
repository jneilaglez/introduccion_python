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

""" Module for practise python basics concepts: 6_exercise.

Static objects:
GEN_PATH -- folder of generated files
RES_PATH -- folder of resources files
"""
import os

GEN_PATH = "generated"
RES_PATH = "resources"
if not os.path.exists(GEN_PATH):
    os.mkdir(GEN_PATH)

df = open(os.path.join(RES_PATH, "data"), "r")
lines = df.readlines()
df.close()

""" Length in characters of the first line. """
print(len(lines[0]))
# print("First line of file: \n{0}".format(lines[0].rstrip('n')))

""" File's number of lines. """
print(len(lines))

""" How many numbers does the file contain? """
print(len(lines[0].split()))

""" Stores the numbers sum of the first line inside another file. """
dg = open(os.path.join(GEN_PATH, "storage_data"), "w")
res = 0
for num in lines[0].split():
    res += int(num)
dg.write(str(res))
dg.close()

""" Stores in other fi text file a line with sum operation that includes all
 operands and the result, ie: # 24 + 34 + 2 = 60. """
dop = open(os.path.join(GEN_PATH, "result_data"), "w")
dop.write(
    "+".join(lines[0].split()) + "=" + str(sum(int(num) for num in lines[0].split())))
dop.close()

""" Adds the line [1, 2 ... 10] a "data" (do not overwrite!). """
df = open(os.path.join(RES_PATH, "data"), "a")
df.write("   ".join([" " + str(i) if i < 10 else str(i) for i in range(1, 11)]) + "\n")
df.close()

""" The product of last line. """
res_prod = 1
for prod in lines[len(lines) - 1].split():
    res_prod *= int(prod)
print(res_prod)

""" Number of lines of "with_comments" if it  ignores those lines that are 
commented (starts with #). """
with_com = open(os.path.join(RES_PATH, "with_comments"), "r")
doc = [cc for cc in with_com if not cc.startswith("#")]
with_com.close()
print(len(doc))

""" Sum of all odd numbers of the document. """
odd_num = [int(n) for num in [lin.split() for lin in doc] for n in num if
           int(n) % 2 != 0]

# res_sum = 0
# for s in odd_num:
#    res_sum += s
# print(res_sum)
print(sum(odd_num))
