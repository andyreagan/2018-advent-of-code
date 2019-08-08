import sys


def find_max_option(prices):
    max_future = [max(prices[i:]) for i in range(len(prices))]
    max_profit = [m-p for m, p in zip(max_future, prices)]
    return max(max_profit)


def test_find_max_option():
    assert find_max_option("7,6,4,3,1") == 0.0
    assert find_max_option("7,1,5,3,6,4") == 5.0


if __name__ == '__main__':
    print(find_max_option(list(map(float, sys.stdin.read().split(",")))))
