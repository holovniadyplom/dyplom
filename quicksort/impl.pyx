cpdef list alg(list array):

    if len(array) < 2:
        return array

    cdef list low = []
    cdef list same = []
    cdef list high = []

    pivot = array[len(array) // 2]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return alg(low) + same + alg(high)