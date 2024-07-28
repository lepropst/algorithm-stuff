from sorts.bucket_sort.bucket_sort import bucket_sort


def main():
    arr = [33, 74, 60, 31, 49, 53, 68, 55, 72, 46, 34, 77]
    sorted_arr = bucket_sort(arr)
    print("\nOriginal array:", arr)
    print("Sorted array:", sorted_arr)
    print(
        "\n",
        "-" * 50,
        """        
So the run time of a bucket sort is generally expressed as:

T(n) = Θ (m + n)

where:

m= is the range of input values
n = number of elements to be sorted
If the range is in order of n, then bucket sort is linear: O(n)


""",
    )
