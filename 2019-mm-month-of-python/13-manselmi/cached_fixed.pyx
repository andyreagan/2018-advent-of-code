import sys


cdef collatz_f(unsigned int i):
    if i % 2 == 0:
        i = i / 2
    else:
        i =  3 * i + 1
    return i


cdef get_path_length_cache(unsigned int i, cache):
    cdef unsigned int l = 0
    cdef list new_elements = []
    while i > (len(cache)-1) or cache[i] == 0:
        new_elements.append(i)
        i = collatz_f(i)
        l += 1
    l += cache[i]
    return (l, new_elements)


cpdef main(unsigned int n):
    '''Cache the paths are already known.

    Use 1-based indexing for convience (ignore the first entry).'''
    cdef unsigned int cache_size = 2*n+1
    cdef unsigned int i, j, x, l, m
    # cdef unsigned int[cache_size] all_path_lengths
    # for i in range(cache_size):
    #     all_path_lengths[i] = 0
    cdef list all_path_lengths = [0 for i in range(cache_size)]
    all_path_lengths[0] = 1
    all_path_lengths[1] = 1
    for i in range(2, n+1):
        if all_path_lengths[i] == 0:
            l, new_elements = get_path_length_cache(i, all_path_lengths)
            for j, x in enumerate(new_elements):
                if x < len(all_path_lengths)-1:
                    all_path_lengths[x] = l-j
    m = max(all_path_lengths)
    print(m, all_path_lengths.index(m))
