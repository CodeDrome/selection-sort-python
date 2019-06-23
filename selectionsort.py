import random

RED = "\x1B[31m"
GREEN = "\x1B[32m"
RESET = "\x1B[0m"


def main():

    """
    Here we just demonstrate selection sort by calling a couple of functions
    to create a list of random data and sort it.
    """

    print("------------------")
    print("| codedrome.com  |")
    print("| Selection Sort |")
    print("------------------\n")

    data = populate_data()

    selection_sort(data)


def populate_data():

    """
    Create an empty list and add a few random integers to it.
    """

    data = []

    for i in range(0, 16):

        data.append(random.randint(1, 99))

    return data


def print_data(data, sortedto):

    """
    Prints the data on a single line, with the sorted portion
    in green and the unsorted portion in red, using ANSI terminal codes.
    """

    for i in range(0, len(data)):

        if i < sortedto:
            print(GREEN + "%-3d " % data[i] + RESET, end="")
        else:
            print(RED + "%-3d " % data[i] + RESET, end="")

    print("\n")


def selection_sort(data):

    """
    Applies the selection sort algorithm to a list of integers,
    also printing the data on each iteration to show progress.
    """

    print("Unsorted...")
    print_data(data, 0)

    print("Selection Sorting...")

    sorted_to = 0;

    while(sorted_to < len(data) - 1):

         index_of_lowest = find_lowest_index(data, sorted_to)

         swap(data, sorted_to, index_of_lowest)

         sorted_to += 1

         print_data(data, sorted_to)

    print("Sorted!")


def swap(data, i1, i2):

    """
    A neat little trick to swap integer values without using a third variable
    """

    if i1 != i2:
        data[i1] = data[i1] ^ data[i2]
        data[i2] = data[i1] ^ data[i2]
        data[i1] = data[i1] ^ data[i2]


def find_lowest_index(data, start):

    """
    Finds the index of the lowest item in the unsorted part of the data.
    """

    lowest_index = start

    for i in range(start, len(data)):
        if data[i] < data[lowest_index]:
            lowest_index = i

    return lowest_index


main()
