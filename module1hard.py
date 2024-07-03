grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_ = sorted(students)

a = grades[0]   #Aaron
b = grades[1]   #Bilbo
j = grades[2]   #Johnny
k = grades[3]   #Khendrik
s = grades[4]   #Steve

grades = list((sum(a) / len(a), sum(b) / len(b), sum(j) / len(j), sum(k) / len(k), sum(s) / len(s)))
dictionary = dict(zip(students_, grades))
print(dictionary)