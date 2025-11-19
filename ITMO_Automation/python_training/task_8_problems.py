# Задача 1

# Бакалавр - 1-4 курс (включительно)
# Магистр - 5-6 курс (включительно)
# Аспирант - 7-9 курс (включительно)

def student_rank(grade):
    if grade == 1 or grade == 2 or grade == 3 or grade == 4:
        print('Бакалавр')
    elif grade in range(5, 7):
        print('Магистр')
    elif 7 <= grade <= 9:
        print('Аспирант')
    else:
        print('Введите корректный год обучения')

student_rank(9)


# Задача 2
def number(num):
    if num > 100 or num < -100:
        print('-')
    else:
        print('+')

number(500)