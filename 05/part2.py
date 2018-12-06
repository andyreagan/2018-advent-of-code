# coding: utf-8
from stack_solution import crispr
def crispr_wrapper(d):
    left = ""
    right = d
    while len(right) > 0:
        left, right = crispr(left, right)
    return len(left)
d = open("data.txt","r").read().rstrip()
crispr_wrapper(d)
len(d)
d.replace("a","")
len(d)
reduced_sizes = [crispr_wrapper(d.replace(x.uppper(), "").replace(x.lower(), "")) for x in chars]
chars = list(set(d))
chars
chars = list(set(d.lower()))
chars
reduced_sizes = [crispr_wrapper(d.replace(x.uppper(), "").replace(x.lower(), "")) for x in chars]
reduced_sizes = [crispr_wrapper(d.replace(x.upper(), "").replace(x.lower(), "")) for x in chars]
reduced_sizes
chars
min(reduced_sizes)
np.array(chars)[min(reduced_sizes)==np.array(reduced_sizes)]
import numpy as np
np.array(chars)[min(reduced_sizes)==np.array(reduced_sizes)]
min(reduced_sizes)
