n = int(input("Enter marks:"))
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input("Enter name: ")

print("{0:.2f}".format(round(sum(student_marks[query_name]) / len(student_marks[query_name]), 2)))