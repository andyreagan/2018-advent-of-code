# MassMutual Python month of Code
# My solution for Michael's problem
#
# 2019-08-13
# Andy Reagan


def collatz_f(i: int) -> int:
    if i % 2 == 0:
        return int(i / 2)
    else:
        return int(3*i + 1)


def get_path(i: int) -> list:
    # print(i)
    l = [i]
    while i != 1:
        i = collatz_f(i)
        l.append(i)
        # print(i, l)
    return l


def get_path_length(i: int) -> int:
    # print(i)
    l = 1
    while i != 1:
        i = collatz_f(i)
        l += 1
        # print(i, l)
    return l

for n, l in ((1, 1), (2, 2), (4, 3), (13, 10)):
    assert get_path_length(n) == l

get_path_length(10)
get_path_length(15)
get_path_length(18)
get_path_length(19)
get_path(15)

n = 20
all_path_lengths = [get_path_length(i+1) for i in range(n)]
all_path_lengths

all_maps = [collatz_f(i+1)-1 for i in range((n-1)*3+1)]
cycle_lengths = [1  for i in range((n-1)*3+1)]
for i in range(1,n):
    print(i+1, "maps to", all_maps[i]+1, "which has cycle len", cycle_lengths[all_maps[i]])
    cycle_lengths[i] += cycle_lengths[all_maps[i]]
    if i>4 and ((i+1)-1) % 3 == 0 and int(((i+1)-1)/3) % 2 == 1:
        print(i+1, "was mapped from", int(((i+1)-1)/3))
        print("add cycle length", cycle_lengths[all_maps[i]], "back onto", int(((i+1)-1)/3))
        cycle_lengths[int(((i+1)-1)/3)-1] += cycle_lengths[i]
        # and add it back to the 2 multiples of int(((i+1)-1)/3)
        # and all of those multiples which would have mapped from an odd number
        # and their multiples....etc!
cycle_lengths[:n]

# assume that n is even...
cache_size = 10*n+1
all_path_lengths = [None for i in range(cache_size)]
all_path_lengths[1] = 1

def get_path_length_cache(i: int, cache: list) -> (int, list):
    # print(i)
    l = 0
    new_elements = []
    while i > (len(cache)-1) or cache[i] is None:
        new_elements.append(i)
        i = collatz_f(i)
        l += 1
        # print(i, l)
    l += cache[i]
    return (l, new_elements)

get_path_length_cache(2, all_path_lengths)
all_path_lengths[2] = 2
get_path_length_cache(3, all_path_lengths)

for i in range(2, n):
    print(i)
    if all_path_lengths[i] is None:
        l, new_elements = get_path_length_cache(i, all_path_lengths)
        print("path length is", l)
        for j, x in enumerate(new_elements):
            if x < len(all_path_lengths)-1:
                all_path_lengths[x] = l-j
all_path_lengths[10+1]

for i in range(1,n+1):
    assert all_path_lengths[i] == get_path_length(i)
