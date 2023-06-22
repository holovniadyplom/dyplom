cpdef list alg(list array):
    """
    https://realpython.com/sorting-algorithms-python/
    """

    cdef int n = len(array)
    cdef int i, j
    cdef bint already_sorted

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break

    return array