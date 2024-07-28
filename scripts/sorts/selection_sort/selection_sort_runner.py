import heapq

from sorts.selection_sort.selection_sort import SelectionSort


def main():
    sorter = SelectionSort()

    # Array Example
    array = [22, 52, 45, 29, 33, 17, 36, 25, 28]
    print("Unsorted array:", array)
    print("Sorted array:", sorter.sort_array(array.copy()))

    # Binary Tree Example (assuming a simple Node class)
    # ... (Create a binary tree)

    # Heap Example
    # heap = [64, 25, 12, 22, 11]
    # heapq.heapify(heap)
    # print("Unsorted heap:", heap)
    # print("Sorted from heap:", sorter.sort_heap(heap.copy()))

    performance_time = """
--------------------------------------------------
\t- Best Case Sort: O(n2)\n
\t- Average Case Sort: O(n2)\n
\t- Worst Case Sort: O(n2)\n
    """
    print(performance_time)
