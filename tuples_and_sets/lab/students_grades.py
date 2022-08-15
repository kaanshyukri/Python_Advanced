n = int(input())
students_grades = {}
for _ in range(n):
    name, grade = input().split()
    if name not in students_grades:
        students_grades[name] = []
    students_grades[name].append(float(grade))

for key, value in students_grades.items():
    print(f"{key} -> {' '.join([f'{v:.2f}' for v in value])} (avg: {sum(value)/len(value):.2f})")
