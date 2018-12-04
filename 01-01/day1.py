# coding: utf-8
import pandas as pd
import numpy as np
with open("data.txt", "r") as f:
    d = f.read().split("\n")
    
len(d)
d[-1]
d[0]
y = [int(x.lstrip("+
y = [int(x.lstrip("+")) for x in d]
len(y)
np.array(y).sum()
np.cumsum(np.array(y))
np.repeat(np.array(y),10)
get_ipython().run_line_magic('pinfo', 'np.repeat')
get_ipython().run_line_magic('pinfo', 'np.tile')
np.tile(np.array(y),10)
np.array(y)[:10]
y = np.array(y)
y[:10]
long = np.tile(y,1000)
len(long)
long_running = np.cumsum(len(long))
i = 0
while long_running[i] not in long_running[:i-1]:
    i+=1
    
i = 1
while long_running[i] not in long_running[:i-1]:
    i+=1
    
long_running[i]
i
long_running.shape
long_running = np.cumsum(long)
long_running[i]
long_running[:i-1]
while long_running[i] not in np.unique(long_running[:i-1]):
    i+=1
    
i
while long_running[i] not in np.unique(long_running[:i-1]):
    i+=1
    
i
long_running[i]
import datetime
datetime.now()
datetime.datetime.now()
print(datetime.datetime.now())
