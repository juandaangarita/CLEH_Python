def divisors(num):
    divisor = [i for i in range(1, num + 1) if num % i == 0]
    return divisor


def run():
    num = input('Enter a positive integer number: ')
    assert num.isnumeric() and int(num) > 0, 'You should enter a positive number'
    print(f'The divisor of {num} are')
    print(divisors(int(num)))
    print('End of the program')


if __name__ == '__main__':
    run()
