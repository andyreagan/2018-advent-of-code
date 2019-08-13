import sys


def collatz_f(i: int) -> int:
    if i % 2 == 0:
        return int(i / 2)
    else:
        return int(3*i + 1)


def get_path_length_cache(i: int, cache: list) -> (int, list):
    l = 0
    new_elements = []
    while i > (len(cache)-1) or cache[i] is None:
        new_elements.append(i)
        i = collatz_f(i)
        l += 1
    l += cache[i]
    return (l, new_elements)


def main(n: int):
    '''Cache the paths are already known.

    Use 1-based indexing for convience (ignore the first entry).'''

    cache_size = 2*n+1
    all_path_lengths = [None for i in range(cache_size)]
    all_path_lengths[0] = 1
    all_path_lengths[1] = 1
    for i in range(2, n+1):
        if all_path_lengths[i] is None:
            l, new_elements = get_path_length_cache(i, all_path_lengths)
            for j, x in enumerate(new_elements):
                if x < len(all_path_lengths)-1:
                    all_path_lengths[x] = l-j
    m = max(all_path_lengths[:(n+1)])
    print(m, all_path_lengths[:(n+1)].index(m))


if __name__ == '__main__':
    main(int(sys.argv[1]))
