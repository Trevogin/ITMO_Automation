# Мои решения
# a = (1,2, 3,4)
# print(a[0])
#
#
# def arg(r, pi=3.14159):
#     return pi * r^2
#
# print(arg(3))


# Верные решения
def task_func(a = (1, 2, 3, 4)):
    return a[1]

print(task_func())

def compute_surface(radius, pi=3.14159):
    return pi * radius * radius # Также можно pi * radius ** 2

print(compute_surface(2))