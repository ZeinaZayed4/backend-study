if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    scores = sorted(set(s[1] for s in records))
    second_lowest_score = scores[1]

    second_lowest_scores = [s for s in records if s[1] == second_lowest_score]
    second_lowest_scores.sort()

    for score in second_lowest_scores:
        print(score[0])
