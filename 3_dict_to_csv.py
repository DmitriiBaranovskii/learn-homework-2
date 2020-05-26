"""
Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

example = [
    {'name' :'John','age': 25, 'job': 'clerk'},
    {'name' :'Bob','age': 35, 'job': 'manager'},
    {'name' :'Bond','age': 39, 'job': 'secret agent'},
    {'name' :'Daniel','age': 30 , 'job': 'driver'}
]

def main():
    with open('example.csv', 'w', encoding='utf-8') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f,fields,delimiter = ';')
        writer.writeheader()
        for person in example:
            writer.writerow(person)


if __name__ == "__main__":
    main()
