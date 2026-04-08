import itertools

n = int(input())
letters = input().split()
k = int(input())

combs = list(itertools.combinations(letters, k))
count = sum(1 for c in combs if "a" in c)

print(f"{count / len(combs):.4f}")
