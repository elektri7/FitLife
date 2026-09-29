import sys

sys.stdout.reconfigure(encoding='utf-8')

# Вывод на экран приветствия
print('FitLife приветствует Вас!')

# Запросы на ввод пользовательских данных
user_name = input('Введите ваше имя: ').capitalize()
user_age = int(input('Сколько вам полных лет? '))
user_weight = float(input('Введите ваш вес в килограммах (например 65.7): '))
user_height = float(input('Введите ваш рост в метрах (например 1.75): '))

# Рассчет индекса массы тела
bmi = round(user_weight / (user_height ** 2), 1)

# Рассчитываем норму воды в миллилитрах
NORM_PER_KILOGRAM = 30  # Средняя норма воды на 1 кг веса
water_ml = user_weight * NORM_PER_KILOGRAM

# Переводим полученный результат в литры
ML_PER_LITRE = 1000  # Кол - милилитров в литре
water_l = round(water_ml / 1000, 1)

# Вывод на экран отчета для пользователя
print(f"\n{'*' * 50}")
print('ОТЧЁТ ДЛЯ ПОЛЬЗОВАТЕЛЯ')
print(f'{user_name} ({user_age} г.)')
print(f'Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l} л. в день')
print(f'\n{user_name}, будьте здоровы!')
print('*' * 50)
