if __name__ == '__main__':
    N = int(input())
    arr = []

    for _ in range(N):
        command, *values = input().split()
        if command == 'insert':
            i, e = int(values[0]), int(values[1])
            arr.insert(i, e)
        if command == 'print':
            print(arr)
        if command == 'remove':
            arr.remove(int(values[0]))
        if command == 'append':
            arr.append(int(values[0]))
        if command == 'sort':
            arr.sort()
        if command == 'pop':
            arr.pop()
        if command == 'reverse':
            arr.reverse()
