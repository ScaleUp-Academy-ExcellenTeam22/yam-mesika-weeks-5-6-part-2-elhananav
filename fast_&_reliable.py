import time


def average_runtime(words_structure):
    """
    This function takes structure and return the average time it took(1000 times) to search the word 'zwitterion'
    in that structure.
    :param words_structure: The structure to be searched in
    :return: the average time it took to search 'zwitterion' 1000 times
    """
    start_time = time.time()
    for _ in range(1000):
        "zwitterion" in words_structure
    return (time.time() - start_time) / 1000


if __name__ == "__main__":
    with open("words.txt", "r") as f:
        words_list = [word for line in f for word in line.split()]
        words_set = set(words_list)
    print("search in list: ", average_runtime(words_list))
    print("search in set: ", average_runtime(words_set))
