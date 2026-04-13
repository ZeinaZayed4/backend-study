def merge_the_tools(string, k):
    n = len(string)

    for i in range(0, n, k):
        seen = set()
        result = ""

        for c in string[i:i+k]:
            if c not in seen:
                seen.add(c)
                result += c

        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)