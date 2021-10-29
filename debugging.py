def divisors(num):
    divisor = [i for i in range(1, num + 1) if num % i == 0]
    return divisor


def run():
    try:
        num = int(input('Enter a positive integer number: '))
        if num <= 0:
            raise ValueError
        else:
            print(f'The divisor of {num} are')
            print(divisors(num))
            print('End of the program')
    except ValueError:
        print('You need to enter a positive number')
        run()


if __name__ == '__main__':
    run()