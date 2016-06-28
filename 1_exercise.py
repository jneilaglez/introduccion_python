""" Module for practise python basics concepts: 1_exercise. """

""" Use the arithmetic operators in the following operations. """
print(3 * 5)
print(3.0 * 5)
print(7.3 ** 2)
print(7.5 / 2)
print([2342.65 / 66])

t_str = "Cabeza grande, ojos hermosos"

""" String length. """
print(len(t_str))

""" First five characters of the string. """
print(t_str[:5])

""" Last seven characters of the string. """
print(t_str[-7:])

""" First five characters in pairs. """
f_aux1, f_aux2 = t_str[:5:2], t_str[1:5:2]
fl = (len(f_aux1) + len(f_aux2)) / 2
final = [f_aux1[c] + f_aux2[c] for c in range(int(fl))]
final.append(f_aux1[2])
print(final)

""" Last thirteen characters in threes. """
aux1, aux2, aux3 = t_str[-13::3], t_str[-12::3], t_str[-11::3]
l = (len(aux1) + len(aux2) + len(aux3)) / 3
final2 = [aux1[c] + aux2[c] + aux3[c] for c in range(int(l))]
final2.append(aux1[4])
print(final2)

""" Uppercase multiples of three. """
print([t_str[c].upper() for c in range(len(t_str)) if c % 3 == 0])

""" In pairs characters between fourth and seventeenth. """
m_aux1, m_aux2 = t_str[4:16:2], t_str[5:17:2]
ml = (len(m_aux1) + len(m_aux2)) / 2
final3 = [m_aux1[c] + m_aux2[c] for c in range(int(ml))]
print(final3)

""" Is x char in the string? """
print('x' in t_str)

""" And o, in uppercase or lowercase? """
print(('o' or 'O') in t_str)
