grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#переводим множество студенты в список и упорядочиваем его
students_sort=list(students)
students_sort.sort()
print(students_sort) #проверяем упорядоченность списка
#считаем количество элементов в какждом списке
#count_stud=len(students_sort)
#count_score=len(grades)
#вводим словарь
journal={}
#Запускаем цикл перебора всех элементов списка
for i in range(len(students_sort)):
#считаем среднее, используя операторы суммы, и вычисления "длины" списка, и закидываем пару в журнал
    journal[students_sort[i]]=sum(grades[i])/len(grades[i])

print('\n',journal)


