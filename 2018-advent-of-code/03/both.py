# coding: utf-8
d = open("part1.txt","r").read().rstrip().split("\n")
t = open("test.txt","r").read().rstrip().split("\n")
t
d[:3]
import re
get_ipython().run_line_magic('pinfo', 're.match')
re.match('#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)', t[0])
r = re.match('#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)', t[0])
r.groups
r.groups()
t[0]
len(t)
import numpy as np
mat = np.ones((len(t),5))
mat
for i, x in enumerate(t):
    mat[i,:] = np.array(list(re.match('#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)', x).groups()))
    
mat
t
mat[:, 1]+mat[:, 3]
np.max(mat[:, 1]+mat[:, 3])
np.max(mat[:, 2]+mat[:, 4])
fabric = np.zeros((np.max(mat[:, 1]+mat[:, 3]), np.max(mat[:, 2]+mat[:, 4])))
fabric = np.zeros((int(np.max(mat[:, 1]+mat[:, 3])), int(np.max(mat[:, 2]+mat[:, 4]))))
fabric
fabric[mat[0, 1]:(mat[0, 1]+mat[0, 3]), mat[0, 2]:(mat[0, 2]+mat[0, 4])]
mat
fabric[int(mat[0, 1]):int(mat[0, 1]+mat[0, 3]), int(mat[0, 2]):int(mat[0, 2]+mat[0, 4])]
fabric[int(mat[0, 1]):int(mat[0, 1]+mat[0, 3]), int(mat[0, 2]):int(mat[0, 2]+mat[0, 4])] += 1
i = 0
fabric[int(mat[i, 1]):int(mat[i, 1]+mat[i, 3]), int(mat[i, 2]):int(mat[i, 2]+mat[i, 4])] += 1
fabric = np.zeros((int(np.max(mat[:, 1]+mat[:, 3])), int(np.max(mat[:, 2]+mat[:, 4]))))
fabric[int(mat[i, 1]):int(mat[i, 1]+mat[i, 3]), int(mat[i, 2]):int(mat[i, 2]+mat[i, 4])] += 1
fabric
for i in [1,2]:
    fabric[int(mat[i, 1]):int(mat[i, 1]+mat[i, 3]), int(mat[i, 2]):int(mat[i, 2]+mat[i, 4])] += 1
    
fabric
(fabric > 0).sum()
(fabric > 1).sum()
mat = np.ones((len(d),5))
for i, x in enumerate(d):
    mat[i,:] = np.array(list(re.match('#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)', x).groups()))
    
mat.shape
mat[-1,:]
fabric = np.zeros((int(np.max(mat[:, 1]+mat[:, 3])), int(np.max(mat[:, 2]+mat[:, 4]))))
fabric.shape
for i in range(mat.shape[0]):
    fabric[int(mat[i, 1]):int(mat[i, 1]+mat[i, 3]), int(mat[i, 2]):int(mat[i, 2]+mat[i, 4])] += 1
    
fabric
fabric.sum()
(fabric > 1).sum()
1000*1000
for i in range(mat.shape[0]):
    if fabric[int(mat[i, 1]):int(mat[i, 1]+mat[i, 3]), int(mat[i, 2]):int(mat[i, 2]+mat[i, 4])].sum() == mat[i, 3]*mat[i, 4]
for i in range(mat.shape[0]):
    if fabric[int(mat[i, 1]):int(mat[i, 1]+mat[i, 3]), int(mat[i, 2]):int(mat[i, 2]+mat[i, 4])].sum() == mat[i, 3]*mat[i, 4]:
        print(i)
        
mat[411,:]
mat[0,:]
