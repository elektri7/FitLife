import sys

sys.stdout.reconfigure(encoding='utf-8')

# Вывод на экран приветствия
print('\nFitLife приветствует Вас!')

# Запросы на ввод пользовательских данных

# Убираем лишние пробелы, делаем первую букву - заглавной
user_name = input('Введите ваше имя: ').strip().capitalize()

# Цикл для выявления ошибок при вводе возраста
while True:
    try:
        user_age = int(input('Сколько вам полных лет? '))
        if user_age <= 0:
            print('Введите корректное значение возраста.')
            continue
        break
    except ValueError:
        print('Пожалуйста, введите целое число (например, 25).')

# Цикл для выявления ошибок при вводе веса
while True:
    try:
        user_weight = float(input('Введите ваш вес в килограммах '
                                  '(например 65.7): '))
        if user_weight <= 0:
            print('Введите корректное значение веса.')
            continue
        break
    except ValueError:
        print('Пожалуйста, введите значение веса дробным числом с точкой '
              '(например, 65.7).')

# Цикл для выявления ошибок при вводе роста
while True:
    try:
        user_height = float(input('Введите ваш рост в метрах '
                                  '(например 1.75): '))
        if user_height <= 0:
            print('Введите корректное значение веса.')
            continue
        break
    except ValueError:
        print('Пожалуйста, введите значение роста дробным числом с точкой '
              '(например, 1.75).')

# Рассчет индекса массы тела
bmi = round(user_weight / (user_height ** 2), 1)

# Рассчитываем норму воды в миллилитрах
NORM_PER_KILOGRAM = 30  # Средняя норма воды на 1 кг веса
water_ml = user_weight * NORM_PER_KILOGRAM

# Переводим полученный результат в литры
ML_PER_LITRE = 1000  # Кол - милилитров в литре
water_litres = round(water_ml / ML_PER_LITRE, 1)

# Вывод на экран отчета для пользователя
print(f'\n{"*" * 50}\nОТЧЁТ ДЛЯ ПОЛЬЗОВАТЕЛЯ\n{user_name} ({user_age} г.)')
print(f'Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_litres:.1f} л. в день')
print(f'\n{user_name}, будьте здоровы!\n{"*" * 50}')
