class CountSortNode:
    def __init__(
        self,
        key,
        value,
    ):
        self.value = value
        self.key = key

    def __str__(self) -> str:
        return f"{self.value} - {self.key}"

    def __repr__(self) -> str:
        return f"value:{self.value}\tkey:{self.key}\n"


def count_sort(arr):
    """Sorts a list of Nodes using counting sort based on the key attribute.

    Args:
        arr: The list of Node objects to be sorted.

    Returns:
        A new list containing the sorted Node objects.
    """

    max_key = max(node.key for node in arr)  # Find the maximum key
    min_key = min(node.key for node in arr)  # Find the minimum key
    count = [0] * (max_key - min_key + 1)  # Initialize the count array
    print(f"\nCount array\n", count, end="\n\n")
    print("Counting Occurrences:")
    for node in arr:  # Count occurrences of each key
        count[node.key - min_key] += 1
        print(f"  Count of key {node.key}: {count[node.key - min_key]}")
    print(f"\nCount array after step one\n", count, end="\n\n")
    print("\nCumulative Counts:")
    for i in range(1, len(count)):  # Calculate cumulative counts
        count[i] += count[i - 1]
        print(f"  Cumulative count up to key {i + min_key}: {count[i]}")
    print(f"\nCount array after step two\n", count, end="\n\n")
    print("\nBuilding Sorted Array:")
    sorted_arr = [None] * len(arr)  # Create the output array
    for node in reversed(arr):  # Fill the output array in reverse order
        index = count[node.key - min_key] - 1
        sorted_arr[index] = node  # Place the Node object
        count[node.key - min_key] -= 1  # Decrement count for the next occurrence
        print(
            f"  Placed Node with key {node.key} and value {node.value} at index {index}"
        )

    return sorted_arr
