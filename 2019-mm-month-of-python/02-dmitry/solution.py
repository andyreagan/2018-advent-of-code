# coding: utf-8
x = """There is a red house on the western most hill. There is a green house on the
eastern most hill. Adjacent to the red house on the western hill is a hospital.
Adjacent to the green house on the eastern most hill is an accountant. Nobody
wants to go to the hospital on the western most hill unless they have to.
Everybody has to go to the accountant on the eastern most hill, because how else
will they do their taxes. Samuel lives on the northern most hill and there is
nothing adjacent to him. Samuel enjoys going to the Gamestop. He buys many
games from Gamestop when he goes."""
import sys
import collections
x = x.replace(".","").replace(",","").replace("\n"," ")
words = dict()
for word, pos in zip(map(lambda y: y.lower(), x.split(" ")), range(len(x.split(" ")))):
    if word in words:
        words[word]["count"] += 1
    else:
        words[word] = {"count": 1, "length": len(word), "first_pos": pos}
list(map(lambda x: print(x), sorted([(word, values) for word, values in words.items()], key=lambda x: (-x[1]['count'], -x[1]['length'], x[1]['first_pos']))[:15]))
