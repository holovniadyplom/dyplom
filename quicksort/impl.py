def alg(array: list[int]) -> list:

    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot = array[len(array) // 2]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return alg(low) + same + alg(high)
