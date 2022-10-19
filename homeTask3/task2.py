# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д
elements = [2, 3, 4, 5, 6]
import math 
size = math.ceil(len(elements)/2)
print(size)
elements2 = []
for i in range(size):
    elements2.append(elements[i]*elements[-i - 1])
print(elements2)