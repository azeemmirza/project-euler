'''
PROBLEM 01: MULTIPLES OF 3 OR 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
'''


def is_multiple(num, base):
    return num % base == 0


def multiples_of_three_five(limit):
    sum_of_multiples = 0

    for num in range(limit):
        if is_multiple(num, 3) or is_multiple(num, 5):
            sum_of_multiples += num

    return sum_of_multiples


if __name__ == '__main__':
    print(multiples_of_three_five(1000))
