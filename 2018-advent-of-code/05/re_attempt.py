# coding: utf-8
d = open("test.txt", "r").read()
len(d)
d
d = open("test.txt", "r").rstrip().read()
d = open("test.txt", "r").read().rstrip()
d
len(d)
import re
re.match('', d)
re.match('', d).groups()
''.join(re.match('', d).groups())
''.join(re.match('([A-Za-z])', d).groups())
''.join(re.match('([A-Za-z]*)', d).groups())
''.join(re.match('([A-Za-z]*?[A-Za-z]*?)', d).groups())
''.join(re.match('([A-Za-z]*?[a-z][A-Z][A-Za-z]*?)', d).groups())
''.join(re.match('([A-Za-z]*[a-z][A-Z][A-Za-z]*?)', d).groups())
''.join(re.match('([A-Za-z]*?[a-z][A-Z][A-Za-z]*)', d).groups())
''.join(re.match('([A-Za-z]*?)[a-z][A-Z]([A-Za-z]*)', d).groups())
