# MassMutual Python month of Code
# My solution for Jordan's problem
#
# Version 2: don't need a boolean tracker
#
# 2019-08-10
# Andy Reagan


def get_held_rain(x):
    # the way to do this without looping over the level would be to keep an
    # array of len(max(x)) for the gap counter
    totaltotal = 0
    for level in range(max(x)):
        # print("floor", level+1)
        building = [y >= (level + 1) for y in x]
        # print(building)
        gap = 0
        total = 0
        for i, b in enumerate(building[:-1]):
            # options:
            # 1. not currently in a gap, still in an opening
            # 2. not currently in a gap, at a building
            # 3. currently in a gap, at a building
            # 4. currently in a gap, still at on opening
            # there is a building, and you were in a gap
            # if (not ingap) and not b:
            #     continue
            if (gap == 0) and b and (not building[i + 1]):
                gap += 1
            # elif (not ingap) and b and (building[i+1]):
            #     continue
            # elif ingap and b: # this won't happen because of the lookahead (ingap already turned off)
            #     total += gap
            #     gap = 0
            #     ingap = False
            elif (gap > 0) and not b and (building[i + 1]):
                total += gap
                gap = 0
            elif (gap > 0) and not b and (not building[i + 1]):
                gap += 1
        # print(total)
        totaltotal += total
    return totaltotal


x = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
assert get_held_rain(x) == 6
x = [0, 3, 1, 2, 0, 0, 3, 1, 4, 1, 3, 2, 1, 0, 1, 0]
print(get_held_rain(x))
