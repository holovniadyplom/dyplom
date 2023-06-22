cpdef int alg(int n):
    cdef int a = 0, b = 1
    cdef int i
    if n < 2:
        return n
    for i in range(2, n + 1):
        a, b = b, a + b
    return b