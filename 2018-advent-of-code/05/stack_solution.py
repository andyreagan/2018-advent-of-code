# coding: utf-8
def crispr(left, right):
    # print(left, right)
    # start    
    if len(left) == 0:
        return right[0],right[1:]
    # delete
    elif ((left[-1].lower() == right[0].lower()) and (((left[-1].upper() == left[-1]) and (right[0].lower() == right[0])) or ((left[-1].lower() == left[-1]) and (right[0].upper() == right[0])))):
        return left[:-1],right[1:]
    # march ahead
    else:
        return left+right[0], right[1:]
    
d = open("test.txt", "r").read().rstrip()
left = ""
right = d
while len(right) > 0:
    left, right = crispr(left, right)
    
left
right
get_ipython().run_line_magic('cat', 'result.txt')
d = open("data.txt","r").read().rstrip()
left = ""
right = d
while len(right) > 0:
    left, right = crispr(left, right)
    
len(left)
len(right)
