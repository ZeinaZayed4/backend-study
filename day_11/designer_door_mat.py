n = int(input())
m = int(input())

pattern = ".|."

for i in range(1, n - 1, 2):
    pattern_width = len(pattern * i)
    remaining = (m - pattern_width) // 2
    print("-" * remaining + pattern * i + "-" * remaining)
remaining = (m - len("WELCOME")) // 2

print("-" * remaining + "WELCOME" + "-" * remaining)

for i in range(n - 2, 0, -2):
    pattern_width = len(pattern * i)
    remaining = (m - pattern_width) // 2
    print("-" * remaining + pattern * i + "-" * remaining)
