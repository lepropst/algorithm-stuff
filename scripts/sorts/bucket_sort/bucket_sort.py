from math import ceil, floor
import math


def bucket_sort(arr):
    """Sorts a list of floating-point numbers using bucket sort.

    Args:
        arr: The list of floating-point numbers to be sorted.

    Returns:
        A new list containing the sorted elements.
    """

    num_buckets = 3  # You can adjust this for finer-grained buckets
    minimum = 30
    max = 86
    bucket_range = (max - minimum) + 1
    bucket_size = round(floor(((bucket_range + num_buckets) - 1) / num_buckets))
    # Create empty buckets
    buckets = [[] for _ in range(num_buckets)]
    print(f"bucket_range: {bucket_range}, bucket_size: {bucket_size}")
    # Scatter: Distribute input array values into buckets

    for num in arr:
        index = int((num - minimum) / bucket_size)

        buckets[index].append(num)
        print(f"  Placed {num} in bucket {index}")
    print("Number of items in each bucket: ", [len(x) for x in buckets])
    print("\nSorting Buckets:")
    # Sort each bucket individually
    for i in range(num_buckets):
        buckets[i] = sorted(buckets[i])  # Use Python's built-in sort for simplicity
        print(f"  Sorted bucket {i}: {buckets[i]}")

    # Gather: Concatenate the sorted buckets to get the final result
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr
