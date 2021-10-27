def power2_natural_number(limit):
    """
    This function is used to power avery natural number until the limit
    :param limit: The upper limit of the list of natural numbers wich you want to know the power to 2
    :type int
    :returns power2: A list containing the list with the power2 natural number until limit """
    power2 = []
    for n in range(limit+1):
        power2.append(n ** 2)
    return power2


def power2_number_non_div3(limit):
    """
    This function is used to power avery natural number until the limit
    :param limit: The upper limit of the list of natural numbers wich you want to know the power to 2
    :type int
    :returns power2: A list containing the list with the power2 natural number until limit """
    # power2_non3 = []
    # for n in range(limit+1):
    #     if (n ** 2) % 3 != 0:
    #         power2_non3.append(n ** 2)

    # This can be resume if it used a listh comprehensions wich is created this way list = [element for element in iterable if condition], wich is read the middle part, then the first part and then the final like this: For each element in the iterable that element will be saved only if the condition is true. The example is read: for each number in the range of the limit +1 only if number power 2 module 3 is different than cero
    power2_non3 = [number ** 2 for number in range(limit + 1) if (number ** 2) % 3 != 0]
    return power2_non3


def list_multiples_4_6_9(limit):
    list = [number for number in range(1, limit + 1) if number % 4 == 0 and number % 6 == 0 and number % 9 == 0]
    return list


def dict_i_i3(limit):
    # dict = {}
    # for i in range(1, limit +1):
    #     if i**3 % 3 != 0:
    #         dict[i] = i ** 3
    dict = {number: number**3 for number in range(1, limit + 1) if number ** 3 % 3 != 0}
    return dict

def dict_i_sqrti(limit):
    # dict = {}
    # for i in range(1, limit +1):
    #     if i**3 % 3 != 0:
    #         dict[i] = i ** 3
    dict = {number: number**0.5 for number in range(1, limit + 1)}
    return dict