# coding: utf-8
d = open("test.txt","r").read().split("\n")
d[0]
d[-1]
d = open("test.txt","r").read().rstrip().split("\n")
d[-1]
def dictify(x):
    y = {}
    for a in x:
        if a in y:
            y[a] += 1
        else:
            y[a] = 1
            
dictify(d[0])
def dictify(x):
    y = {}
    for a in x:
        if a in y:
            y[a] += 1
        else:
            y[a] = 1
    return y
dictify(d[0])
2 in {v: k for k,v in dictify(d[0])}
2 in {v: k for k,v in dictify(d[0]).items()}
3 in {v: k for k,v in dictify(d[0]).items()}
3 in {v: k for k,v in dictify(d[-1]).items()}
twos = [2 in {v: k for k,v in dictify(y).items()} for y in d]
twos
threes = [3 in {v: k for k,v in dictify(y).items()} for y in d]
threes
np.sum(np.array(twos))
import numpy as np
np.sum(np.array(twos))
np.sum(np.array(threes))
d = open("data.txt","r").read().rstrip().split("\n")
twos = [2 in {v: k for k,v in dictify(y).items()} for y in d]
threes = [3 in {v: k for k,v in dictify(y).items()} for y in d]
np.sum(np.array(twos))
np.sum(np.array(twos)) * np.sum(np.array(threes))
