from fractions import Fraction


def knapsack_greedy_benefit(values, weights, capacity):

    n = len(values)
    items = list(zip(values, weights, range(n)))  # Create tuples (value, weight, index)
    items.sort(reverse=True)  # Sort by value in descending order

    total_value = 0
    selected_items = {}
    total_weight = 0
    for value, weight, index in items:
        if weight <= capacity:
            capacity -= weight
            total_value += value

            if not selected_items.get(index):
                selected_items[f"{value}-{index}"] = 1
            selected_items[f"{value}-{index}"] += 1
            total_weight += weight
    if total_weight <= capacity:

        return knapsack_greedy_benefit(values, weights, capacity)

    return total_value, selected_items


def knapsack_greedy_weight(values, weights, capacity):

    n = len(values)
    items = list(zip(values, weights, range(n)))
    items.sort(key=lambda x: x[1])  # Sort by weight in ascending order

    total_value = 0
    selected_items = {}
    total_weight = 0

    for value, weight, index in items:
        if weight <= capacity:
            capacity -= weight
            total_value += value

            if not selected_items.get(index):
                selected_items[f"{value}-{index}"] = 1
            selected_items[f"{value}-{index}"] += 1
            total_weight += weight
    if total_weight <= capacity:
        return knapsack_greedy_weight(values, weights, capacity)

    return total_value, selected_items


def knapsack_greedy_density(values, weights, capacity):

    n = len(values)
    items = list(zip(values, weights, range(n)))
    items.sort(
        key=lambda x: x[0] / x[1], reverse=True
    )  # Sort by density (value/weight) in descending order

    total_value = 0
    selected_items = {}
    total_weight = 0
    for value, weight, index in items:
        if weight <= capacity:
            capacity -= weight
            total_value += value

            if not selected_items.get(index):
                selected_items[f"{value}-{index}"] = 1
            selected_items[f"{value}-{index}"] += 1
            total_weight += weight
    if total_weight <= capacity:

        return knapsack_greedy_density(values, weights, capacity)

    return total_value, selected_items


def knapsack_fractional(values, weights, capacity):
    n = len(values)
    items = list(zip(values, weights, range(n)))
    items.sort(key=lambda x: x[0] / x[1], reverse=True)  # Sort by benefit density

    total_value = 0
    selected_items = []
    for value, weight, index in items:
        if capacity == 0:  # Knapsack is full
            break

        fraction = min(1, capacity / weight)  # Take all or fraction that fits
        capacity -= fraction * weight
        total_value += fraction * value
        simplified_fraction = Fraction(fraction).limit_denominator().__str__()
        print(
            f"Taking {fraction}, {simplified_fraction} amount of [{value} , {weight}]"
        )

        selected_items.append((index, simplified_fraction, fraction))

    return total_value, selected_items
