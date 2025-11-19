num_float = 3.4

# Также попробуйте варианты
# num_float = 0
# num_float = -4.5

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')


permit_print = True

if num_float > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')