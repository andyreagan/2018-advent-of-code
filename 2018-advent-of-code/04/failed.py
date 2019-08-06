# coding: utf-8
import re
import numpy as np
import pandas as pd
d = open("data.txt","r").read().rstrip().split("\n")
len(d)
d[-1]
re.match('[1518-([0-9][0-9])-([0-9][0-9]) ([0-9][0-9]):([0-9][0-9])] (.*)', d[0]).groups()
re.match('\[1518-([0-9][0-9])-([0-9][0-9]) ([0-9][0-9]):([0-9][0-9])\] (.*)', d[0]).groups()
pd.DataFame(re.match('\[1518-([0-9][0-9])-([0-9][0-9]) ([0-9][0-9]):([0-9][0-9])\] (.*)', d[0]).groups())
pd.DataFrame(re.match('\[1518-([0-9][0-9])-([0-9][0-9]) ([0-9][0-9]):([0-9][0-9])\] (.*)', d[0]).groups())
pd.DataFrame({k: v for k,v in zip(["month", "day", "hour", "minute", "note"], re.match('\[1518-([0-9][0-9])-([0-9][0-9]) ([0-9][0-9]):([0-9][0-9])\] (.*)', d[0]).groups())})
pd.DataFrame({k: [v] for k,v in zip(["month", "day", "hour", "minute", "note"], re.match('\[1518-([0-9][0-9])-([0-9][0-9]) ([0-9][0-9]):([0-9][0-9])\] (.*)', d[0]).groups())})
df = pd.concat([pd.DataFrame({k: [v] for k,v in zip(["month", "day", "hour", "minute", "note"], re.match('\[1518-([0-9][0-9])-([0-9][0-9]) ([0-9][0-9]):([0-9][0-9])\] (.*)', x).groups())}) for x in d])
df.shape
len(d)
df.head()
get_ipython().run_line_magic('pinfo', 'df.sort_values')
df.month.astype('int')
for k in ["month", "day", "hour", "minute"]:
    df[k] = df[k].astype('int')
    
df.loc[df.hour == 23, 'day'] += 1
df.head()
df.sort_values(["month", "day", "minute"])
df = df.sort_values(["month", "day", "minute"])
df.shape
df.head()
df.groupby(["month", "day"]).apply(lambda x: x.note.values["Gaurd" in x.note])
df.groupby(["month", "day"]).apply(lambda x: x.note.values[x.note.apply(lambda y: "Gaurd" in y)])
df.groupby(["month", "day"]).apply(lambda x: x.note.values[x.note.apply(lambda y: "Gaurd" in y)])
df.groupby(["month", "day"]).apply(lambda x: x.note.values[x.note.max()])
df.groupby(["month", "day"]).apply(lambda x: x.note.values[0])
df["Guard"] = df.note.apply(lambda x: "Guard" in x)
df.head()
df.groupby(["month", "day"]).apply(lambda x: x.note.values[x.note.apply(lambda y: "Guard" in y)])
df["Guard_ID"] = df.loc[df.Guard, :].apply(lambda x: re.match('Guard #([0-9]+?).*', x.Guard).groups()[0])
df.head()
df["Guard_ID"] = df.loc[df.Guard, :].apply(lambda x: re.match('Guard #([0-9]+?).*', x.note).groups()[0])
df["Guard_ID"] = df.loc[df.Guard, 'note'].apply(lambda x: re.match('Guard #([0-9]+?).*', x).groups()[0])
df["Guard_ID"] = df.loc[df.Guard, 'note']
df.Guard
df.shape
df.head()
df["Guard_ID"] = df.loc[df.Guard, ['note']]
df["Guard_ID"] = df.loc[df.Guard, :].note
df["Guard_ID"] = df.loc[df.Guard, :]['note']
df.drop(['Guard_ID'})
df.drop(['Guard_ID'])
df.drop(columns=['Guard_ID'])
df.head()
df = pd.concat([pd.DataFrame({k: [v] for k,v in zip(["month", "day", "hour", "minute", "note"], re.match('\[1518-([0-9][0-9])-([0-9][0-9]) ([0-9][0-9]):([0-9][0-9])\] (.*)', x).groups())}) for x in d], ignore_index=True)
df.head()
df = df.sort_values(["month", "day", "minute"])
df.reset_index(inplace=True)
df.head()
df["Guard"] = df.note.apply(lambda x: "Guard" in x)
df["Guard_ID"] = df.loc[df.Guard, 'note'].apply(lambda x: re.match('Guard #([0-9]+?).*', x).groups()[0])
df.head()
df["Guard_ID"] = df.loc[df.Guard, 'note'].apply(lambda x: re.match('Guard #([0-9]+).*', x).groups()[0])
df.head()
df.join(df.groupby(['month','day']).apply(lambda x: x.Gaurd_ID.values[x.Guard]))
df.join(df.groupby(['month','day']).apply(lambda x: x.Guard_ID.values[x.Guard]))
df.groupby(['month','day']).apply(lambda x: x.Guard_ID.values[x.Guard])
df.head()
df.head(30)
