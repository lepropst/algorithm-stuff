from visualizers.convert_subtree import convert_subtree


def heap_sort(lst):
    """
    Sorts a list of elements in ascending order using heap sort,
    with detailed step-by-step output.
    """

    length = len(lst)
    current_idx = (length // 2) - 1

    # Build the max heap
    pass_num = 1
    print("Building Max Heap:")
    while current_idx >= 0:
        print(f"\nPass {pass_num}:")
        print(f"  Initial List: {lst}")
        convert_subtree(lst, current_idx, length - 1)
        print(f"  Resulting List: {lst}")
        current_idx -= 1
        pass_num += 1

    # Extract elements from the heap in sorted order
    print("\nSorting:")
    for i in range(length - 1, 0, -1):
        print(f"\nStep {length - i}:")
        print(
            f"  Swapping root {lst[0]} (index 0) with last element {lst[i]} (index {i})"
        )
        lst[0], lst[i] = lst[i], lst[0]
        print(f"  List after swap: {lst}")
        convert_subtree(lst, 0, i - 1)
        print(f"  List after heapify: {lst}")


# Example Usage (assuming you have the `convert_subtree` function from previous responses)
def main():
    lst = [82, 52, 45, 49, 33, 17, 36, 15, 18]

    heap_sort(lst)
    print(lst)  # Output: [8, 10, 15, 16, 20, 30, 50]
