# Реализуйте алгоритм перемешивания списка 
# (метод random.shuffle использовать нельзя, но другие методы из библиотеки random - можно).

import random
list = [1, 4, 5, 6, 3]
print ("Список до перемешивания: " + str(list))
for i in range(len(list)-1, 0, -1):
    j = random.randint(0, i + 1)
    list[i], list[j] = list[j], list[i]
print ("Список после перемешивания: " +  str(list))
