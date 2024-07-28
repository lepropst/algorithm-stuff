import heapq
from graphviz import Digraph


class Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        # For priority queue comparison based on frequency
        return self.freq < other.freq


# def build_huffman_tree(text):
#     """Builds a Huffman encoding tree from text."""

#     # Calculate character frequencies
#     freq = {}
#     for char in text:
#         freq[char] = freq.get(char, 0) + 1

#     # Build the priority queue (min-heap) with nodes (frequency as key)
#     priority_queue = [Node(char, f) for char, f in freq.items()]
#     heapq.heapify(priority_queue)  # Create a min-heap
#     while len(priority_queue) > 1:
#         # Pop the two nodes with the lowest frequencies
#         left = heapq.heappop(priority_queue)
#         right = heapq.heappop(priority_queue)
#         newNode = Node(
#             char=left.char + right.char,
#             freq=left.freq + right.freq,
#             left=left,
#             right=right,
#         )
#         # Ensure left node has lower frequency or lexicographically lower char in case of ties
#         if left.freq > right.freq or (
#             left.freq == right.freq and left.char > right.char
#         ):
#             left, right = right, left  # Swap to ensure the left has lower frequency

#         # Create a new internal node with these two nodes as children and insert into the queue.

#         heapq.heappush(priority_queue, newNode)

#     return priority_queue[0]  # The root of the Huffman tree


def build_huffman_tree(text):
    """Builds a Huffman encoding tree from text."""

    # Calculate character frequencies for letters only
    freq = {}
    for char in text:

        freq[char] = freq.get(char, 0) + 1

    # Build the priority queue (min-heap) with nodes (frequency as key)
    priority_queue = [Node(char, f) for char, f in freq.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        # Pop the two nodes with the lowest frequencies
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        # Ensure left node has lower frequency or lexicographically lower char in case of ties
        if left.freq > right.freq or (
            left.freq == right.freq
            and left.char != None
            and right.char != None
            and left.char > right.char
        ):
            left, right = right, left

        # Create a new internal node with these two nodes as children and insert into the queue.
        new_node = Node(freq=left.freq + right.freq)
        new_node.left = left
        new_node.right = right
        heapq.heappush(priority_queue, new_node)

    return priority_queue[0]  # The root of the Huffman tree


def get_huffman_codes(root, current_code=""):
    """Traverses the tree to get Huffman codes for each character."""
    codes = {}

    if root is None:
        return codes
    if root.char:
        codes[root.char] = current_code
    codes.update(get_huffman_codes(root.left, current_code + "0"))
    codes.update(get_huffman_codes(root.right, current_code + "1"))
    return codes


def print_tree(root):
    """Visualizes the Huffman tree using graphviz."""
    dot = Digraph(comment="Huffman Tree")

    def add_node(node, parent=None):
        node_id = str(id(node))  # Unique identifier for each node
        label = f"{node.char if node.char else '*'}\n{node.freq}"
        dot.node(node_id, label)

        if parent:
            edge_label = "0" if node is parent.left else "1"
            dot.edge(str(id(parent)), node_id, label=edge_label)

        if node.left:
            add_node(node.left, node)
        if node.right:
            add_node(node.right, node)

    add_node(root)
    dot.render("huffman_tree", format="png")  # Render to a PNG file


def decode_huffman(encoded_text, root):
    """Decodes a Huffman-encoded string using the provided Huffman tree."""

    decoded_text = ""
    current_node = root

    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:  # bit == "1"
            current_node = current_node.right

        if current_node.char:  # If we reach a leaf node (character)
            decoded_text += current_node.char
            current_node = root  # Reset to the root for the next character

    return decoded_text
