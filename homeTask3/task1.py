# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
elements = [2, 3, 6, 10, 12, 16, 5]
summ = 0
for i in range(1, len(elements), 2):
    #if i % 2 == 1:
        summ += elements[i]       
print(f"{elements} -> сумма элементов на нечётных позициях {summ}")