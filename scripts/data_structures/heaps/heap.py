import heapq
import os
from graphviz import Digraph


def visualize_heap(heap_list, filename):
    dot = Digraph(comment=filename)

    # Add nodes to the graph
    for i, item in enumerate(heap_list):
        dot.node(str(i), label=str(item))

    # Add edges to the graph
    for i in range(len(heap_list)):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        if left_child < len(heap_list):
            dot.edge(str(i), str(left_child))
        if right_child < len(heap_list):
            dot.edge(str(i), str(right_child))

    # Render and view the graph
    dot.render(os.path.join(os.path.dirname(__name__), filename), view=True)
