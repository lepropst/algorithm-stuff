import os
import graphviz


class AvlNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Initially, a new node's height is 1


class avl_tree:
    def __init__(self):
        self.root = None

    # Function to get the height of a node
    def get_height(self, node):
        return node.height if node else 0

    # Function to get the balance factor of a node
    def get_balance(self, node):
        return self.get_height(node.right) - self.get_height(node.left) if node else 0

    # Right rotation
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x
        # Postorder Traversal

    def postorder_traversal(self):
        result = []
        self._postorder_traversal(self.root, result)
        return result

    def _postorder_traversal(self, root, result):
        if root:
            self._postorder_traversal(root.left, result)
            self._postorder_traversal(root.right, result)
            result.append(root.key)

    # Preorder Traversal
    def preorder_traversal(self):
        result = []
        self._preorder_traversal(self.root, result)
        return result

    def _preorder_traversal(self, root, result):
        if root:
            result.append(root.key)
            self._preorder_traversal(root.left, result)
            self._preorder_traversal(root.right, result)

    # Left rotation
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    # Insert a new node into the tree
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if not root:
            return AvlNode(key)
        elif key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Rebalance the tree if needed (left left, left right, right right, right left cases)
        # ... (implementation omitted for brevity)

        return root

    # Inorder traversal (for testing)
    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, root, result):
        if root:
            self._inorder_traversal(root.left, result)
            result.append(root.key)
            self._inorder_traversal(root.right, result)


def printToFile(string: str):
    with open(
        os.path.join(os.path.dirname(__file__), "avl-tree-output.md"), "+a"
    ) as file:
        file.write(string)


def visualize_tree(root, filename):
    dot = graphviz.Digraph(comment="AVL Tree")

    def add_nodes_edges(node, parent=None):
        if node:
            dot.node(str(node.key))
            if parent:
                dot.edge(str(parent.key), str(node.key))
            add_nodes_edges(node.left, node)
            add_nodes_edges(node.right, node)

    add_nodes_edges(root)
    dot.render(
        format="svg",
        view=False,
        filename=os.path.join(os.path.dirname(__file__), filename),
    )  # Render and open SVG


def main():
    try:
        if not os.path.exists(os.path.join(os.path.dirname(__name__), "svgs")):
            os.mkdir(os.path.join(os.path.dirname(__name__), "svgs"))
        with open(
            os.path.join(os.path.dirname(__file__), "avl-tree-output.md"), "w"
        ) as file:
            file.write("")
    except Exception:
        print("Unable to write to file")
    names = ["JESURANGL", "EMILORANG"]
    for name in names:

        # Create AVL tree
        tree = avl_tree()
        for letter in name[:9]:
            str = (
                f'\nInserting letter: {letter}\n\n<img src="svgs/{name}/inserting-{letter}.svg"/>\n\n'
                + "-" * 20
                + "\n"
            )
            tree.insert(letter)
            # ... (add your rebalancing logic and visualization here, if needed)
            visualize_tree(
                tree.root,
                filename=os.path.join("svgs", name, f"inserting-{letter}"),
            )
            printToFile(str)

        # Pre-order traversal
        traversals = [
            ", ".join(tree.preorder_traversal()),
            ", ".join(tree.postorder_traversal()),
            ", ".join(tree.inorder_traversal()),
        ]
        labels = ["pre", "post", "inorder"]

        if not os.path.exists(os.path.join(os.path.dirname(__file__), "svgs", name)):
            os.mkdir(os.path.join(os.path.dirname(__file__), "svgs", name))
        with open(
            os.path.join(os.path.dirname(__file__), f"svgs", name, "traversals.json"),
            mode="w+",
        ) as file:
            file.write("{")
            for label, traversal in zip(labels, traversals):
                txt = f"{label}: {traversal},\n\n"
                file.write(txt)
            file.write("}")

        # Deletion and rebalancing (repeat three times)
        for _ in range(3):
            if tree.root:
                str = f'\nDeleting root node: {tree.root.key}\n\n<img src="svgs/{name}/deleting-{tree.root.key}.svg"/>\n'

                # ... (add your deletion and rebalancing logic here)
                visualize_tree(
                    tree.root,
                    filename=os.path.join("svgs", name, f"deleting-{tree.root.key}"),
                )
                printToFile(str)
