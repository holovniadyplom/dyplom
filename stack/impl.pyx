cpdef int alg(int n):
    cdef list l = []
    for i in range(n):
        l.append(i)
    return len(l)