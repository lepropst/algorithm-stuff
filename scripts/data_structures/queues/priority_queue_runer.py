from data_structures.queues.priority_queue import PriorityQueue


def main():
    pq = PriorityQueue()
    pq.push("task1", 3)
    pq.push("task2", 1)
    pq.push("task3", 2)
    pq.push("task4", 4)
    pq.push("task5", 0)

    pq.visualize()
