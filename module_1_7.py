grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades1 = []
students1 = list(students)
students1.sort()
a = len(grades)
for i in range(a):
    i_grades = grades[i]
    b = len(i_grades)
    sum = 0
    for j in range(b):
        sum = sum + i_grades[j]
    sum = sum/b
    grades1.append(sum)
students_dict = dict(zip(students1, grades1))
print(students_dict)

