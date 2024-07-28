from sorts.buble_sort.bubble_sort import BubbleSort


def main():
    sorter = BubbleSort()

    # Array Example
    array = [21, 52, 45, 24, 33, 67, 72, 25, 28]
    print("Original array:", array)
    print("Sorted array:", sorter.sort_array(array.copy()))

    print(
        """
\t- Best Case Sort: O(n)\n
\t- Average Case Sort: O(n2)\n
\t- Worst Case Sort: O(n2)\n"""
    )
