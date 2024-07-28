import heapq
import os
from graphviz import Digraph
import heapq


class PriorityQueue:
    def __init__(self):
        self._heap = []

    def push(self, item, priority):
        heapq.heappush(self._heap, (-priority, item))  # Negate priority for max-heap

    def pop(self):
        priority, item = heapq.heappop(self._heap)
        return item, -priority  # Negate priority back to original

    def peek(self):
        priority, item = self._heap[0]
        return item, -priority

    def is_empty(self):
        return len(self._heap) == 0

    def visualize(self):
        dot = Digraph(comment="Priority Queue (Max-Heap)")
        self._visualize(dot, 0)
        dot.render(
            os.path.join(os.path.dirname(__file__), "priority_queue.gv"), view=True
        )

    def _visualize(self, dot, index):
        if index < len(self._heap):
            priority, item = self._heap[index]
            dot.node(str(index), label=f"{item} ({-priority})")  # Negate priority

            left_child = 2 * index + 1
            right_child = 2 * index + 2
            if left_child < len(self._heap):
                dot.edge(str(index), str(left_child))
                self._visualize(dot, left_child)
            if right_child < len(self._heap):
                dot.edge(str(index), str(right_child))
                self._visualize(dot, right_child)
