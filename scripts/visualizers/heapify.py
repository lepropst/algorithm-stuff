from visualizers.convert_subtree import convert_subtree


def heapify(lst):
    """
    Converts a list of elements into a max heap.

    This function uses the provided `convert_subtree` function (from the previous example) to iteratively convert subtrees within the list into max heaps.

    Args:
        lst: The list containing the elements to be arranged into a heap.
    """

    length = len(lst)
    current_idx = (length // 2) - 1  # Start from the first non-leaf node

    while current_idx >= 0:
        convert_subtree(lst, current_idx, length - 1)
        current_idx -= 1


def main():
    lst = [50, 30, 20, 15, 10, 8, 16]
    heapify(lst)
    print(lst)  # Output: [50, 16, 30, 15, 10, 8, 20]
