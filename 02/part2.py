# coding: utf-8
get_ipython().run_line_magic('less', 'part1.py')
d = open("test.txt","r").read().rstrip().split("\n")
get_ipython().run_line_magic('less', 'part1.py')
import numpy as np
get_ipython().run_line_magic('less', 'part1.py')
d = open("data.txt","r").read().rstrip().split("\n")
d = open("test.txt","r").read().rstrip().split("\n")
d
get_ipython().run_line_magic('less', 'part1.py')
def dictify(x):
    y = {}
    for a in x:
        if a in y:
            y[a] += 1
        else:
            y[a] = 1
    return y
from part1 import dictify
dictify(d[0])
dictify(d[1])
d_dicts = [dictify(x) for x in d]
def compare(x,y):
    diff_count = 0
    for k in x:
        if k in y:
            diff_count += np.abs(x[k]-y[k])
        else:
            diff_count += x[k]
    for k in y:
        if k not in x:
            diff_count += y[k]
    return diff_count == 1
compare(d_dicts[0], d_dicts[1])
for i in range(len(d_dicts)):
    for j in range(i,len(d_dicts)):
        print(i,j)
        
for i in range(len(d_dicts)):
    for j in range(i+1,len(d_dicts)):
        print(i,j)
        
for i in range(len(d_dicts)):
    for j in range(i+1,len(d_dicts)):
        print(i, j, compare(d_dicts[i], d_dicts[j]))
        
        
        
def compare(x,y):
    diff_count = 0
    for k in x:
        if k in y:
            diff_count += np.abs(x[k]-y[k])
        else:
            diff_count += x[k]
    for k in y:
        if k not in x:
            diff_count += y[k]
    return diff_count
for i in range(len(d_dicts)):
    for j in range(i+1,len(d_dicts)):
        print(i, j, compare(d_dicts[i], d_dicts[j]))
        
        
        
def compare(x,y):
    diff_count = 0
    for k in x:
        if k in y:
            diff_count += np.abs(x[k]-y[k])
        else:
            diff_count += x[k]
    for k in y:
        if k not in x:
            diff_count += y[k]
    return diff_count
def compare_strings(x,y):
    assert len(x) == len(y)
    truthy_chars = [x[i] != y[i] for i in range(len(x))]
    return np.sum(np.array(truthy_chars))


        
for i in range(len(d_dicts)):
    for j in range(i+1,len(d_dicts)):
        print(i, j, compare(d[i], d[j]))
        
        
        
        
for i in range(len(d_dicts)):
    for j in range(i+1,len(d_dicts)):
        print(i, j, compare_strings(d[i], d[j]))
        
        
        
        
        
for i in range(len(d_dicts)):
    for j in range(i+1,len(d_dicts)):
        print(i, j, compare_strings(d[i], d[j]))
        if compare_strings(d[i], d[j])[0] == 1:
            print(np.array(list(d[i]))[compare_strings(d[i], d[j])[1])])

                    
        
for i in range(len(d_dicts)):
    for j in range(i+1,len(d_dicts)):
        print(i, j, compare_strings(d[i], d[j]))
        if compare_strings(d[i], d[j])[0] == 1:
            print(np.array(list(d[i]))[compare_strings(d[i], d[j])[1]])
            

                    
        
def compare_strings(x,y):
    assert len(x) == len(y)
    truthy_chars = [x[i] != y[i] for i in range(len(x))]
    return (np.sum(np.array(truthy_chars)), np.array(truthy_chars))




        
for i in range(len(d_dicts)):
    for j in range(i+1,len(d_dicts)):
        print(i, j, compare_strings(d[i], d[j]))
        if compare_strings(d[i], d[j])[0] == 1:
            print(np.array(list(d[i]))[compare_strings(d[i], d[j])[1]])
            

                    
        
for i in range(len(d_dicts)):
    for j in range(i+1,len(d_dicts)):
        print(i, j, compare_strings(d[i], d[j]))
        if compare_strings(d[i], d[j])[0] == 1:
            print(np.array(list(d[i]))[compare_strings(d[i], d[j])[1]])
            
            

                    
        
for i in range(len(d_dicts)):
    for j in range(i+1,len(d_dicts)):
        # print(i, j, compare_strings(d[i], d[j]))
        if compare_strings(d[i], d[j])[0] == 1:
            print(np.array(list(d[i]))[!compare_strings(d[i], d[j])[1]])
            
            

                    
        
for i in range(len(d_dicts)):
    for j in range(i+1,len(d_dicts)):
        # print(i, j, compare_strings(d[i], d[j]))
        if compare_strings(d[i], d[j])[0] == 1:
            print(np.array(list(d[i]))[~compare_strings(d[i], d[j])[1]])
                    
for i in range(len(d_dicts)):
    for j in range(i+1,len(d_dicts)):
        # print(i, j, compare_strings(d[i], d[j]))
        if compare_strings(d[i], d[j])[0] == 1:
            print(np.array(list(d[i]))[~(compare_strings(d[i], d[j])[1])])
            
                    
for i in range(len(d_dicts)):
    for j in range(i+1,len(d_dicts)):
        # print(i, j, compare_strings(d[i], d[j]))
        if compare_strings(d[i], d[j])[0] == 1:
            print(np.array(list(d[i]))[(compare_strings(d[i], d[j])[1])])
            
            
                    
for i in range(len(d_dicts)):
    for j in range(i+1,len(d_dicts)):
        # print(i, j, compare_strings(d[i], d[j]))
        if compare_strings(d[i], d[j])[0] == 1:
            print(np.array(list(d[i]))[(compare_strings(d[i], d[j])[1])])
            
            
                    
for i in range(len(d_dicts)):
    for j in range(i+1,len(d_dicts)):
        # print(i, j, compare_strings(d[i], d[j]))
        if compare_strings(d[i], d[j])[0] == 1:
            print(np.array(list(d[i]))[~(compare_strings(d[i], d[j])[1])])
            
            
            
                    
for i in range(len(d_dicts)):
    for j in range(i+1,len(d_dicts)):
        # print(i, j, compare_strings(d[i], d[j]))
        if compare_strings(d[i], d[j])[0] == 1:
            print(d[i], d[j])
            print(np.array(list(d[i]))[~(compare_strings(d[i], d[j])[1])])
                                
d
get_ipython().run_line_magic('pwd', '')
d = open("test2.txt","r").read().rstrip().split("\n")
d
for i in range(len(d_dicts)):
    for j in range(i+1,len(d_dicts)):
        # print(i, j, compare_strings(d[i], d[j]))
        if compare_strings(d[i], d[j])[0] == 1:
            print(d[i], d[j])
            print(np.array(list(d[i]))[~(compare_strings(d[i], d[j])[1])])
                                
d = open("data.txt","r").read().rstrip().split("\n")
for i in range(len(d_dicts)):
    for j in range(i+1,len(d_dicts)):
        # print(i, j, compare_strings(d[i], d[j]))
        if compare_strings(d[i], d[j])[0] == 1:
            print(d[i], d[j])
            print(np.array(list(d[i]))[~(compare_strings(d[i], d[j])[1])])
                                
d_dicts = [dictify(x) for x in d]
for i in range(len(d_dicts)):
    for j in range(i+1,len(d_dicts)):
        # print(i, j, compare_strings(d[i], d[j]))
        if compare_strings(d[i], d[j])[0] == 1:
            print(d[i], d[j])
            print(np.array(list(d[i]))[~(compare_strings(d[i], d[j])[1])])
                                
for i in range(len(d_dicts)):
    for j in range(i+1,len(d_dicts)):
        # print(i, j, compare_strings(d[i], d[j]))
        if compare_strings(d[i], d[j])[0] == 1:
            print(d[i], d[j])
            print("".join(list(np.array(list(d[i]))[~(compare_strings(d[i], d[j])[1])])))
            
                                
