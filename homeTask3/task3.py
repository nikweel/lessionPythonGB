# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов
elements = [1.1, 1.2, 3.1, 5, 10.01]
elements2 = []
for i in range(len(elements)):
    if elements[i] % 1 != 0:
        elements2.append(elements[i])
resp = [round(elements2[i] % 1, 2) for i in range(len(elements2))]
print(f"{resp} => {max(resp) - min(resp)}")