import itertools


def a_perfect_dish_to_share():
    """
    This function finds all exists perfect numbers.
    A perfect number is a positive integer that is equal to the sum of its positive divisors,
     excluding the number itself.
    :return: Each time return the next perfect number.
    """
    for roll in itertools.count(start=1):
        dividers = [num for num in range(1, roll//2 + 1) if roll % num == 0]
        if sum(dividers) == roll:
            yield roll


if __name__ == '__main__':
    perfect_number_generator = a_perfect_dish_to_share()
    for number in perfect_number_generator:
        print(number)
