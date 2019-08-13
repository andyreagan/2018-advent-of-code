import sys


def collatz_f(int i):
    if i % 2 == 0:
        return i / 2
    else:
        return 3*i + 1


def get_path_length(int i):
    cdef int l
    l = 1
    while i != 1:
        i = collatz_f(i)
        l += 1
    return l


def main(n):
    cdef int[n] all_path_lengths
    for i in range(n):
        all_path_lengths[i] = get_path_length(i+1)
    m = max(all_path_lengths)
    print(m, all_path_lengths.index(m)+1)


if __name__ == '__main__':
    main(int(sys.argv[1]))
