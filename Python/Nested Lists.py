if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    second_lowest_grade = sorted(list(set([record[1] for record in records])))[1]
    out = sorted([student[0] for student in records if student[1] == second_lowest_grade])
    for item in out:
        print(item)
