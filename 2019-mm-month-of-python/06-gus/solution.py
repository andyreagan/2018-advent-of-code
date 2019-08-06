# MassMutual Python month of Code
# My solution for Gus's problem
#
# 2019-08-06
# Andy Reagan
import sys


def main():
    assert len(sys.argv) == 3
    m = int(sys.argv[1])  # across
    n = int(sys.argv[2])  # down

    column = list(range(1, n + 1))
    new_column = list(range(1, n + 1))
    for i in range(2, m):  # across
        for j in range(1, n):  # down
            new_column[j] = new_column[j - 1] + column[j]
        column = new_column
        new_column = list(range(1, n + 1))
    print(column[-1])


if __name__ == '__main__':
    main()
