import heapq

from data_structures.heaps.heap import visualize_heap


def main():

    heap = []
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 4)
    heapq.heappush(heap, 2)

    visualize_heap(heap, "first.diagram")
    heapq.heappop(heap)
    visualize_heap(heap, "second.diagram")
