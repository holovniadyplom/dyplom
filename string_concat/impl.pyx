cpdef str alg(int n):
    cdef str result = ""

    for i in range(n):
        result += str(i)

    return result