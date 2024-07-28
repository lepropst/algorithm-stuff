from sorts.shell_sort.shell_sort import ShellSort


def main():
    sorter = ShellSort()

    # Array Example
    array = [32, 22, 41, 29, 30, 17, 36, 45, 28]
    print("Original array:", array)
    print("Sorted array:", sorter.sort_array(array.copy()))

    print(
        """
--------------------------------------------------------------------------------
\t- Best Case Sort: O(n log n)\n
\t- Average Case Sort:O(n2)\n
\t- Worst Case Sort: O(n2)\n
      
"""
    )
