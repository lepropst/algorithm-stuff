class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def convert_subtree(lst, subtree_root, bottom):
    """
    Converts a subtree within a list-based heap to a max heap.

    Args:
        lst: The list containing the heap elements.
        subtree_root: The index of the root of the subtree to be converted.
        bottom: The index of the last element in the list.
    """

    left_child_idx = subtree_root * 2 + 1
    done = False

    while left_child_idx <= bottom and not done:
        # Find the index of the largest child
        if left_child_idx == bottom:
            max_child_idx = left_child_idx  # Left child is the only child
        else:
            right_child_idx = left_child_idx + 1
            max_child_idx = (
                left_child_idx
                if lst[left_child_idx] > lst[right_child_idx]
                else right_child_idx
            )  # Ternary operator for comparison

        # Compare the subtree root element with the largest child element
        if lst[subtree_root] < lst[max_child_idx]:
            # Swap elements
            lst[subtree_root], lst[max_child_idx] = (
                lst[max_child_idx],
                lst[subtree_root],
            )

            # Update for the next iteration
            subtree_root = max_child_idx
            left_child_idx = subtree_root * 2 + 1
        else:
            done = True
