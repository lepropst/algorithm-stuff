from sorts.count_sort.count_sort import CountSortNode, count_sort


def main():
    arr = [
        CountSortNode(2, 1),
        CountSortNode(1, 2),
        CountSortNode(0, 3),
        CountSortNode(1, 4),
        CountSortNode(2, 5),
        CountSortNode(1, 6),
    ]
    sorted_arr = count_sort(arr)
    print(
        "\nOriginal array:\n",
        "".join(map(str, [f"\t- {x } index {index}\n" for index, x in enumerate(arr)])),
    )
    print(
        "Sorted array:\n",
        "".join(
            map(
                str, [f"\t- {x } index {index}\n" for index, x in enumerate(sorted_arr)]
            )
        ),
    )
