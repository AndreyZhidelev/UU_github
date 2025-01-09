# Список
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

# Студенты:
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

Journal = {}
sorted_students_list = sorted(students)
N = len(students)

for i in range(N):
    everage_mark = sum(grades[i]) / len(grades[i])
    Journal[sorted_students_list[i]] = everage_mark

print(Journal)
