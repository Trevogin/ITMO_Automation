# задача 1
print('задача 1')

def task_1(a: int, b: float, c: str, d: list, e: bool) -> str:
    return a, b, c, d, e

print(task_1(1, 2.5, 'word', [1,2], True))


# Задача 2
print('задача 2')
a = [1, 2, 3, 5, 8, 13, 21]
def task_2(a: int) -> int:
    return a[0:3]

print (task_2(a))
print ('Последовательность Фибоначчи' + '\n')


# Задача 3
print('задача 3')
def task_3(x: int) -> int:
    return x ** 2

print (task_3(5))