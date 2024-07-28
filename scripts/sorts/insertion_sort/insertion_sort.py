class InsertionSort:
    def sort_array(self, arr):
        n = len(arr)

        for i in range(1, n):
            key = arr[i]
            j = i - 1

            print(f"\nStep {i}:")
            print(f"  Array: {arr}")
            print(f"  Key: {key}")

            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]  # Shift element to the right
                j -= 1
                print(f"  Shifting {arr[j + 1]} to the right")

            arr[j + 1] = key  # Insert the key into the correct position
            print(f"  Inserting {key} at index {j + 1}")
            print(f"  Result: {arr}")

        return arr
