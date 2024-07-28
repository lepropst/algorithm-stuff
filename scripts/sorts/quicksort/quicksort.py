class QuickSort:
    def sort_array(self, arr, low, high):
        if low < high:
            print(f"\nPartitioning subarray: {arr[low:high+1]}")
            pivot_index = self.partition(arr, low, high)
            print(f"QUICKSORT(list, {low}, {high})")
            print(f"Pivot index: {pivot_index}, Pivot value: {arr[pivot_index]}")
            print(f"Partitioned array: {arr}")

            self.sort_array(arr, low, pivot_index - 1)  # Sort left subarray
            self.sort_array(arr, pivot_index + 1, high)  # Sort right subarray
        return arr

    def partition(self, arr, low, high):
        print(f"  Initial array: {arr[low:high+1]}")

        pivot_ptr = low
        left_ptr = low + 1
        right_ptr = high

        while left_ptr <= right_ptr:
            print(
                f"  LeftPtr: {left_ptr}, RightPtr: {right_ptr}, PivotPtr: {pivot_ptr}"
            )

            # Move left_ptr to the right
            while left_ptr <= high and arr[left_ptr] <= arr[pivot_ptr]:
                left_ptr += 1

            # Move right_ptr to the left
            while right_ptr >= low and arr[right_ptr] > arr[pivot_ptr]:
                right_ptr -= 1

            if left_ptr < right_ptr:
                # Swap values at left_ptr and right_ptr
                arr[left_ptr], arr[right_ptr] = arr[right_ptr], arr[left_ptr]
                print(
                    f"  Swapping {arr[left_ptr]} (index {left_ptr}) with {arr[right_ptr]} (index {right_ptr})"
                )
                print(f"  Result: {arr[low:high+1]}")

        # Swap pivot into its correct position
        arr[pivot_ptr], arr[right_ptr] = arr[right_ptr], arr[pivot_ptr]
        print(
            f"  Swapping pivot {arr[right_ptr]} (index {right_ptr}) to final position"
        )
        print(f"  Result: {arr[low:high+1]}")
        return right_ptr  # Return the final pivot index


# ... (rest of the code (main function) remains the same)
