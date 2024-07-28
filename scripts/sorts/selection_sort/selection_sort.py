import heapq


class SelectionSort:
    def sort_array(self, arr):
        n = len(arr)
        for i in range(n - 1):
            min_index = i
            print(f"\nStep {i + 1}:")
            print(f"  Array: {arr}")

            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j

            arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap
            print(
                f"  Swapped {arr[i]} (index {i}) with {arr[min_index]} (index {min_index})"
            )
            print(f"  Result: {arr}")

        return arr

    def sort_binary_tree(self, root):
        """Performs selection sort on a binary tree (in-place modification)."""

        def inorder_traversal(node, arr):
            """Helper function for inorder traversal."""
            if node:
                inorder_traversal(node.left, arr)
                arr.append(node.val)
                inorder_traversal(node.right, arr)

        values = []
        inorder_traversal(root, values)  # Extract values
        self.sort_array(values)  # Sort values

        # Update tree nodes (requires a mutable tree structure)
        index = 0

        def update_inorder(node):
            nonlocal index
            if node:
                update_inorder(node.left)
                node.val = values[index]
                index += 1
                update_inorder(node.right)

        update_inorder(root)
        return root

    def sort_heap(self, heap):
        """Performs selection sort on a heap (creates a sorted array)."""
        sorted_array = []
        while heap:
            sorted_array.append(heapq.heappop(heap))  # Pop smallest element
        return sorted_array
