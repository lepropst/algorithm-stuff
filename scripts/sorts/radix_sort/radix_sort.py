def counting_sort(arr, exp1):
    """Counting sort for a specific digit place value."""

    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Assuming decimal base (0-9)

    print(f"  Processing digit place value: {exp1}")
    print(f"    Initial array: {arr}")

    # Count occurrences of each digit at the current place value
    for i in range(n):
        index = int(arr[i] / exp1) % 10
        count[index] += 1

    # Calculate cumulative counts
    for i in range(1, 10):
        count[i] += count[i - 1]
    print(f"    Cumulative counts: {count}")

    # Build the output array in reverse order
    for i in range(n - 1, -1, -1):
        index = int(arr[i] / exp1) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy the output array to the original array
    for i in range(n):
        arr[i] = output[i]

    print(f"    Sorted array after this pass: {arr}")


def radix_sort(arr):
    """Radix Sort with pass-by-pass output."""
    max1 = max(arr)
    exp = 1

    print("Radix Sort (LSB First):")

    while max1 // exp > 0:  # Process each digit place
        counting_sort(arr, exp)
        exp *= 10
