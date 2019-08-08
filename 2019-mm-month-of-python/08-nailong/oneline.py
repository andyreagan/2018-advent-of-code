# doesn't work?
import sys; x = sys.stdin.read(); print(max([m-p for m, p in [(p, max(list(map(float, x.split(","))[i:]))) for i, p in enumerate(list(map(float, x.split(","))))]]))
