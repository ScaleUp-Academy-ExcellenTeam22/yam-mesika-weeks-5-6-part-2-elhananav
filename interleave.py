from itertools import chain


def interleave(*args):
    """
    This function takes one or more iterable parameters and return list of all
    the variables intertwined with each other.
    :param args: One or more iterable parameters.
    :return: List of all the variables intertwined with each other.
    """
    return list(chain.from_iterable(zip(*args)))


def interleave_generator(*args):
    """
    This function takes one or more iterable parameters and return list of all
    the variables intertwined with each other. The function return only one of the
    variables each time its called.
    :param args: One or more iterable parameters.
    :return: List of all the variables intertwined with each other.
    """
    weave_list = list(chain.from_iterable(zip(*args)))
    for c in weave_list:
        yield c


if __name__ == '__main__':
    for item in interleave_generator('abc', [1, 2, 3], ('!', '@', '#')):
        print(item)
