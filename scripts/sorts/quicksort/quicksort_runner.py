from sorts.quicksort.quicksort import QuickSort


def main():
    sorter = QuickSort()

    # Array Example
    array = [32, 22, 41, 29, 25, 17, 36, 45, 28]
    print("Original array:", array)
    print("Sorted array:", sorter.sort_array(array.copy(), 0, len(array) - 1))

    # ... (you can add binary tree and heap sorting here if needed)
