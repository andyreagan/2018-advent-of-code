# MassMutual Python month of Code
# My solution for Alex's problem
#
# 2019-08-07
# Andy Reagan
import sys

_vowels = 'AEIOU'.lower()


def test_main():
    s = 'banana'
    r = main(s)
    assert r[0] == 'Stuart'
    assert r[1] == 12
    print('pass tests')


def main(s):
    s = s.lower()
    assert s == s.lower()
    # faster lookup
    vowels = {x for x in _vowels}

    stuart = dict()
    kevin = dict()
    for i, char in enumerate(s):
        if char in vowels:
            # print(i, char)
            # print(s[i:])
            if s[i:] in kevin:
                kevin[s[i:]] += 1
            else:
                kevin[s[i:]] = 1
            for j in range(1, len(s) - i):
                # print(s[i:-j])
                if s[i:-j] in kevin:
                    kevin[s[i:-j]] += 1
                else:
                    kevin[s[i:-j]] = 1
                    # print(i, char)
        else:
            # print(s[i:])
            if s[i:] in stuart:
                stuart[s[i:]] += 1
            else:
                stuart[s[i:]] = 1
            for j in range(1, len(s) - i):
                # print(s[i:-j])
                if s[i:-j] in stuart:
                    stuart[s[i:-j]] += 1
                else:
                    stuart[s[i:-j]] = 1
    # print(kevin)
    # print(stuart)
    if sum(kevin.values()) > sum(stuart.values()):
        return ('Kevin', sum(kevin.values()))
    else:
        return ('Stuart', sum(stuart.values()))


if __name__ == '__main__':
    r = main(sys.argv[1])
    print(r[0], r[1])
