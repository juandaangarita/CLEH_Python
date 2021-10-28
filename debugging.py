def divisors(num):
    divisor = [i for i in range(1, num + 1) if num % i == 1]
    return divisor


def run():
    num = int(input('Enter a number: '))
    print(divisors(num))
    print('End of the program')


if __name__ == '__main__':
    run()