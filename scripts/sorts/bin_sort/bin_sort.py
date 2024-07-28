from functools import reduce


def bin_sort(arr, num_buckets=10):
    """Sorts a list of numbers using bin sort.

    Args:
        arr: The list of numbers to be sorted.
        num_buckets: The number of buckets to use (default is 10).

    Returns:
        A new list containing the sorted elements.
    """

    min_val = min(arr)
    max_val = max(arr)
    value_range = max_val - min_val

    # Create and initialize buckets as lists
    buckets = [[] for _ in range(num_buckets)]

    print("Distributing Elements into Buckets:")
    for num in arr:  # Place items into the correct bucket
        bucket_index = int(((num - min_val) / value_range) * (num_buckets - 1))
        buckets[bucket_index].append(num)
        print(f"  Placed {num} in bucket {bucket_index}")
    bucket_counts = [f"{index} -> {len(x)}" for index, x in enumerate(buckets)]
    bucket_total = sum([len(x) for x in buckets])
    for x in buckets:
        print(x)

    print(
        "Number of items in each bucket",
        "\n".join(bucket_counts),
        f"\nTotal sum {bucket_total}",
    )
    print("\nSorting Buckets:")
    sorted_arr = []
    for bucket in buckets:  # Sort items in each non-empty bucket
        bucket.sort()
        sorted_arr.extend(bucket)
        print(f"  Sorted bucket: {bucket}")

    return sorted_arr
