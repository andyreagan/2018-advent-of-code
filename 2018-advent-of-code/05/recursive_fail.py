# coding: utf-8
def crispr(left, right):
    if len(left) = 0:
        crispr(right[0],right[1])
    elif ((left[-1].lower() == right[0].lower()) and (((left[-1].upper() == left[-1]) and (right[0].lower() == right[0])) or ((left[-1].lower() == left[-1]) and (right[0].upper() == right[0]))):
        crispr(left[:-1],right[1:])
    elif len(right) = 0
        return left
def crispr(left, right):
    if len(left) = 0:
        crispr(right[0],right[1])
    elif ((left[-1].lower() == right[0].lower()) and (((left[-1].upper() == left[-1]) and (right[0].lower() == right[0])) or ((left[-1].lower() == left[-1]) and (right[0].upper() == right[0]))):
        crispr(left[:-1],right[1:])
    elif len(right) = 0
        return left
def crispr(left, right):
    if len(left) = 0:
        crispr(right[0],right[1])
    elif ((left[-1].lower() == right[0].lower()) and (((left[-1].upper() == left[-1]) and (right[0].lower() == right[0])) or ((left[-1].lower() == left[-1]) and (right[0].upper() == right[0]))):
        crispr(left[:-1],right[1:])
    elif len(right) = 0:
        return left
def crispr(left, right):
    # start
    if len(left) == 0:
        crispr(right[0],right[1])
    # delete
    elif ((left[-1].lower() == right[0].lower()) and (((left[-1].upper() == left[-1]) and (right[0].lower() == right[0])) or ((left[-1].lower() == left[-1]) and (right[0].upper() == right[0])))):
        crispr(left[:-1],right[1:])
    # done!
    elif len(right) == 0:
        return left
    # march ahead
    else:
        crispr(left+[right[0]], right[1:])

                
crispr("aAbbbB")
crispr("", "aAbbbB")
x = "A"
x[-1]
crispr("", "aAbbbB")
x
x[:-1]
def crispr(left, right):
    print(left, right)
    # start
    if len(left) == 0:
        crispr(right[0],right[1])
    # delete
    elif ((left[-1].lower() == right[0].lower()) and (((left[-1].upper() == left[-1]) and (right[0].lower() == right[0])) or ((left[-1].lower() == left[-1]) and (right[0].upper() == right[0])))):
        crispr(left[:-1],right[1:])
    # done!
    elif len(right) == 0:
        return left
    # march ahead
    else:
        crispr(left+[right[0]], right[1:])
        

                
crispr("", "aAbbbB")
def crispr(left, right):
    print(left, right)
    # start
    if len(left) == 0:
        crispr(right[0],right[1:])
    # delete
    elif ((left[-1].lower() == right[0].lower()) and (((left[-1].upper() == left[-1]) and (right[0].lower() == right[0])) or ((left[-1].lower() == left[-1]) and (right[0].upper() == right[0])))):
        crispr(left[:-1],right[1:])
    # done!
    elif len(right) == 0:
        return left
    # march ahead
    else:
        crispr(left+[right[0]], right[1:])
        

                
crispr("", "aAbbbB")
def crispr(left, right):
    print(left, right)
    # start
    if len(left) == 0:
        crispr(right[0],right[1:])
    # delete
    elif ((left[-1].lower() == right[0].lower()) and (((left[-1].upper() == left[-1]) and (right[0].lower() == right[0])) or ((left[-1].lower() == left[-1]) and (right[0].upper() == right[0])))):
        crispr(left[:-1],right[1:])
    # done!
    elif len(right) == 0:
        return left
    # march ahead
    else:
        crispr(left+right[0], right[1:])
        

                
crispr("", "aAbbbB")
def crispr(left, right):
    print(left, right)
    # done
    if len(right) == 0:
        return left
    # start    
    if len(left) == 0:
        crispr(right[0],right[1:])
    # delete
    elif ((left[-1].lower() == right[0].lower()) and (((left[-1].upper() == left[-1]) and (right[0].lower() == right[0])) or ((left[-1].lower() == left[-1]) and (right[0].upper() == right[0])))):
        crispr(left[:-1],right[1:])
    # march ahead
    else:
        crispr(left+right[0], right[1:])
        
crispr("", "aAbbbB")
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('less', 'test.txt')
get_ipython().run_line_magic('less', 'test.txt')
crispr("", "dabAcCaCBAcCcaDA")
get_ipython().run_line_magic('cat', 'result.txt')
s = open("data.txt","r").read().rstrip()
crispr("", s)
def crispr(left, right):
    # print(left, right)
    # done
    if len(right) == 0:
        return left
    # start    
    if len(left) == 0:
        crispr(right[0],right[1:])
    # delete
    elif ((left[-1].lower() == right[0].lower()) and (((left[-1].upper() == left[-1]) and (right[0].lower() == right[0])) or ((left[-1].lower() == left[-1]) and (right[0].upper() == right[0])))):
        crispr(left[:-1],right[1:])
    # march ahead
    else:
        crispr(left+right[0], right[1:])
        
crispr("", s)
len(s)
