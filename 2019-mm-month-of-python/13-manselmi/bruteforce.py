import sys


def collatz_f(i: int) -> int:
    if i % 2 == 0:
        return int(i / 2)
    else:
        return int(3*i + 1)


def get_path_length(i: int) -> int:
    # print(i)
    l = 1
    while i != 1:
        i = collatz_f(i)
        l += 1
        # print(i, l)
    return l


def main(n):
    all_path_lengths = [get_path_length(i+1) for i in range(n)]
    m = max(all_path_lengths)
    print(m, all_path_lengths.index(m)+1)


if __name__ == '__main__':
    main(int(sys.argv[1]))
