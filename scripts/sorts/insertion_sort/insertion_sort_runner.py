from sorts.insertion_sort.insertion_sort import InsertionSort


def main():
    sorter = InsertionSort()

    # Array Example
    array = [32, 22, 41, 29, 33, 17, 36, 45, 28]
    print("Original array:", array)
    print("Sorted array:", sorter.sort_array(array.copy()))

    print(
        """
\t- Best Case Sort: O(n)\n
\t- Average Case Sort: O(n2)\n
\t- Worst Case Sort: O(n2)\n

          """
    )
