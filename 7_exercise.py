""" Module for practise python basics concepts: 7_exercise. """


def error_message(num):
    """
    Receiving a number, print out a message.
    :param num: number
    :return: error message
    """
    return "Function only accepts integers " + str(type(num)) + " " + str(num)


def is_integer(num):
    """
    Receiving a number, test if is an integer.
    :param num:
    :return: True if the number is an int or False
    """
    if type(num) is int:
        return True
    else:
        return False


def get_sum_int(num_list):
    """
    Receiving a list as parameter, return the plus of all its elements. Can not use sum function.
    :param num_list: list of ints
    :return: plus of all elements
    """
    res = 0
    for i in num_list:
        if not is_integer(i):
            return error_message(i)
        res += i
    return res


print(get_sum_int([1, 2, 3]))


def double_pow(x, y, z):
    """
    Receiving a 3 numbers, calculates x ** y ** z
    :param x: int number
    :param y: int number
    :param z: int number
    :return: pow of pow x ** y ** z
    """
    if not is_integer(x) or not is_integer(y) or not is_integer(z):
        return "Function only accepts integers"
    return x ** y ** z


print(double_pow(2, 2, 2))


def get_pair_int(num_list):
    """
    Receiving a list of ints, return other with those elements which are pair or greater than 113.
    :param num_list: list of ints
    :return: list with pair elements greater than 113
    """
    pares = []
    for i in num_list:
        if not is_integer:
            return error_message(i)
        elif i % 2 == 0 and i >= 113:
            pares.append(i)
    return pares


print(get_pair_int([1, 2, 3, 4, 5, 114, 116, 117]))


def get_arithmetic_average(num_list):
    """
    Receiving a list of ints, return the arithmetic average of its elements
    :param num_list: list of ints
    :return: arithmetic average
    """
    arith_aver = 0
    for i in num_list:
        if not is_integer:
            error_message(i)
        else:
            arith_aver += i
    return arith_aver / len(num_list)


print(get_arithmetic_average([1, 2, 3]))


def get_factorial(num):
    """
    Calculates a factorial of a number.
    :param num: int number
    :return: factorial of the number
    """
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial


print(get_factorial(4))


def get_divisors(num):
    """
    Receiving a number, returns a list with all its dividers.
    :param num: int number
    :return: list with all of its dividers
    """
    divisors = []
    for i in range(1, num + 1):
        if num % i is 0:
            divisors.append(i)
    return divisors


print(get_divisors(15))


def is_prime(num):
    """
    Receiving a number, determines if it is prime or not.
    :param num: int number
    :return: True if the number is prime or False if not
    """
    prime = False
    for i in range(1, num):
        if num % i == 0 and i != 1:
            prime = False
            break
        else:
            prime = True
    return prime


print(is_prime(11))
