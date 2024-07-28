# Example Usage
from sorts.radix_sort.radix_sort import radix_sort


def main():

    arr = [456, 789, 22, 75, 988, 687, 543, 321, 9, 38, 811, 745, 832, 86, 59, 10]
    # arr = [
    #     "big",
    #     "ace",
    #     "did",
    #     "dad",
    #     "bib",
    #     "abe",
    #     "bad",
    #     "dab",
    #     "id",
    #     "fad",
    #     "he",
    #     "fab",
    #     "had",
    #     "gig",
    #     "gag",
    # ]
    print("Original array:", arr)

    # Sort MSB first (default)
    radix_sort(arr.copy())

    # Sort LSB first
