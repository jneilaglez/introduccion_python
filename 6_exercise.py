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

df = open(os.path.join(RES_PATH, "data"),"r")
lines = df.readlines()
df.close()

""" Lenght in characters of the first line. """
print(len(lines[0]))
#print("First line of file: \n{0}".format(lines[0].rstrip('n')))

""" File's number of lines. """
print(len(lines))

""" How many numbers does the file contain? """
print(len(lines[0].split()))

""" Stores the amount of numbers of the first line inside other file. """
dg = open(os.path.join(GEN_PATH, "storage_data"),"w")
res = 0
for num in lines[0].split():
    res += int(num)
dg.write(str(res))
dg.close()

""" Stores in other fi text file a line with sum operation tath includes all 
 operands and the result, ie: # 24 + 34 + 2 = 60. """
dop = open(os.path.join(GEN_PATH, "result_data"),"w")
dop.write("+".join(lines[0].split()) + "=" + str(sum(int(num) for num in lines[0].split())))
dop.close()

""" Adds the line [1, 2 ... 10] a "data" (do not overwrite!). """
df = open(os.path.join(RES_PATH, "data"),"a")
df.write("   ".join([" "+str(i) if i < 10 else str(i) for i in range(1,11)]) + "\n")
df.close()

""" The product of last line. """
res_prod = 1
for prod in lines[len(lines) - 1].split():
    res_prod *= int(prod)
print(res_prod)

""" Number of lines of "with_comments" if it  ignores those lines that are 
commented (starts with #). """
conc = open(os.path.join(RES_PATH, "with_comments"),"r")
doc = [cc for cc in conc if not cc.startswith("#")]
conc.close()
print(len(doc))

""" Sum of all odd numbers of the document. """
odd_num = [int(n) for num in [lin.split() for lin in doc] for n in num if int(n) % 2 is not 0]
#res_sum = 0                             
#for s in odd_num:
#    res_sum += s
#print(res_sum)
print(sum(odd_num))