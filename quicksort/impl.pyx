cpdef list alg(list array):
    """
    https://realpython.com/sorting-algorithms-python/#the-quicksort-algorithm-in-python
    list concat + list insert + recursion
    """

    if len(array) < 2:
        return array

    cdef list low = []
    cdef list same = []
    cdef list high = []

    # Исключаем рандомизацию и используем центральный элемент в качестве опорного
    pivot = array[len(array) // 2]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return alg(low) + same + alg(high)