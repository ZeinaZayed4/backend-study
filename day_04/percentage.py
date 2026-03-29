if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    total = 0
    query_values = student_marks[query_name]

    for val in query_values:
        total += val

    print(f'{(total / 3):.2f}')
    