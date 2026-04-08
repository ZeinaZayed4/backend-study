import itertools

s = input()

result = []
for k, g in itertools.groupby(s):
    result.append(f"({len(list(g))}, {k})")

print(*result)
