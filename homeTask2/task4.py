# Задайте список из N элементов, заполненных числами из промежутка [-N, N] 
# (например, [-3, -2, 1, 0, 1, 2, 3]. Найдите произведение элементов на указанных позициях. 

n = int(input("Введите число N: "))
lst_number = [i for i in range(-n, n+1)]
a = int(input("Позиция А: "))
b = int(input("Позиция B: "))
for i in range(len(lst_number)):
    mult = lst_number[a -1]*lst_number[b - 1]
print(mult)
