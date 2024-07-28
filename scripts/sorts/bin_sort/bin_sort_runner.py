from sorts.bin_sort.bin_sort import bin_sort


def main():
    arr = [33, 74, 60, 31, 49, 53, 68, 55, 72, 46, 34, 77]
    sorted_arr = bin_sort(arr)
    print("\nOriginal array:", arr)
    print("Sorted array:", sorted_arr)
