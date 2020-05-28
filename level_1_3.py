from collections import Counter

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

# Необходимо задать ключ, без него ошибка unhashable type: 'dict'. Можно ли как-то посчитать через Counter все?
count = Counter(name['first_name'] for name in students)
print(count)

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

count = Counter(name['first_name'] for name in students).most_common(1)
print(count)

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
for class_ in school_students:
    count = Counter(name['first_name'] for name in class_).most_common(1)
    print(count)

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'},{'first_name': 'Миша'},]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'},{'first_name': 'Оля'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for class_ in school:
    count = Counter(f'В классе {class_["class"]} мальчиков:' for name in class_['students'] if is_male.get(name['first_name']))
    count+= Counter(f'В классе {class_["class"]} девочек:' for name in class_['students'] if not is_male.get(name['first_name']))
    print(count)

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'},{'first_name': 'Миша'}, {'first_name': 'Оля'},]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'},{'first_name': 'Оля'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for class_ in school:
    count = Counter(f'В классе {class_["class"]} мальчиков:' for name in class_['students'] if is_male.get(name['first_name']))
    count+= Counter(f'В классе {class_["class"]} девочек:' for name in class_['students'] if not is_male.get(name['first_name']))
    print(count.most_common(1))
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a