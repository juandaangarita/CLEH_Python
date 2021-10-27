def func_odd(list):
    odd_list = [i for i in list if i % 2 != 0]
    return odd_list

def func_square_list(list):
    square_list = [i ** 2 for i in list]
    return square_list

def multiply_list(list):
    multiply_list = 1
    for element in list:
        multiply_list *= element
    return multiply_list