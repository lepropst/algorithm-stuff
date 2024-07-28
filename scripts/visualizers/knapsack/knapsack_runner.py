from visualizers.knapsack.knapsack import (
    knapsack_fractional,
    knapsack_greedy_benefit,
    knapsack_greedy_density,
    knapsack_greedy_weight,
)


def main():

    values = [32, 77, 84, 39, 45]
    weights = [16, 22, 21, 13, 18]
    capacity = 45
    [print(value / weight, value, weight) for value, weight in zip(values, weights)]
    total_value, selected_items = knapsack_greedy_benefit(values, weights, capacity)
    print("\n\nknapsack_greedy_benefit\n", "-" * 25)
    print("\tTotal value:", total_value)
    print("\tSelected items (indices):", selected_items)
    total_value, selected_items = knapsack_greedy_weight(values, weights, capacity)
    print("knapsack_greedy_weight\n", "-" * 25)
    print("\tTotal value:", total_value)
    print("\tSelected items (indices):", selected_items)
    total_value, selected_items = knapsack_greedy_density(values, weights, capacity)
    print("knapsack_greedy_density\n", "-" * 25)
    print("\tTotal value:", total_value)
    print("\tSelected items (indices):", selected_items)
    total_value, selected_items = knapsack_fractional(values, weights, capacity)
    print("knapsack fractional\n", "-" * 25)
    print("\tTotal value:", total_value)
    print("\tSelected items (indices):", selected_items)
