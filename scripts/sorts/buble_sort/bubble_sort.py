class BubbleSort:
    def sort_array(self, arr):
        n = len(arr)

        for i in range(n):
            swapped = False  # Optimization: Check if any swaps were made
            print(f"\nPass {i + 1}:")

            for j in range(0, n - i - 1):
                print(f"  Array: {arr}")

                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                    swapped = True
                    print(
                        f"  Swapped {arr[j]} (index {j}) with {arr[j + 1]} (index {j + 1})"
                    )
                else:
                    print(
                        f"  No swap needed between {arr[j]} (index {j}) and {arr[j + 1]} (index {j + 1})"
                    )

                print(f"  Result: {arr}")

            if not swapped:  # If no swaps, array is sorted
                break
        return arr
