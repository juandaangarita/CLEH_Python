import power2_natural_numbers
import palindrome
import high_order_functions
from functools import reduce

def run():
    # print(power2_natural_numbers.power2_natural_number(100))
    # print(power2_natural_numbers.power2_number_non_div3(100))
    # print(power2_natural_numbers.list_multiples_4_6_9(100))
    # print(power2_natural_numbers.dict_i_i3(10))
    # print(power2_natural_numbers.dict_i_sqrti(100))
    # print(palindrome.palindrome('Una palabra'))
    # palindrome_lambda = lambda string: string == string[::-1]
    # print(palindrome_lambda('ana'))
    list1 = [1, 4, 5, 6, 9, 13, 19, 21]
    list2 = [1, 2, 3, 4, 5]
    print(high_order_functions.func_odd(list1))

    odd_list_filter = list(filter(lambda x: x % 2 != 0, list1))
    print(odd_list_filter)
    # print(high_order_functions.func_filter_odd(list1))

    print(high_order_functions.func_square_list(list1))

    square_list_map = list(map(lambda x: x**2,list1))
    print(square_list_map)

    print(high_order_functions.multiply_list(list2))

    all_multiply = reduce(lambda a, b: a * b, list2)
    print(all_multiply)



if __name__ =="__main__":
    run()
