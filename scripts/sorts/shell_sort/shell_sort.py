class ShellSort:
    def sort_array(self, arr):
        n = len(arr)
        gap = n // 2

        while gap > 0:
            print(f"\nGAP{gap} - - - - - - - Gap: {gap}")

            for i in range(gap, n):
                temp = arr[i]
                j = i
                print(f"\tArray: {arr}")

                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                    print(f"\tShifting {arr[j]} to the right")

                arr[j] = temp
                print(f"\t\t- Inserting {temp} at index {j}\n")
                print(f"RESULT - - - - - - Result: {arr}\n")

            gap //= 2

        return arr
