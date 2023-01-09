import json
# Задание 1
# Напишите информационную систему «Сотрудники».
# Программа должна обеспечивать ввод данных, редактирование данных сотрудника, удаление сотрудника, поиск
# сотрудника по фамилии, вывод информации обо всех
# сотрудниках, указанного возраста, или фамилия которых
# начинается на указанную букву. Организуйте возможность
# сохранения найденной информации в файл. Также весь
# список сотрудников сохраняется в файл (при выходе из
# программы — автоматически, в процессе исполнения
# программы — по команде пользователя). При старте
# программы происходит загрузка списка сотрудников из
# указанного пользователем файла.І
filename = 'person.json'
# firma = {
#   "Devidenko Dmitriy Grigorovich": {
#     'telephone': '0972587412',
#     'email': 'olegkozuh@gmail.com',
#     'position': 'Sales Manager',
#     'cabinet number': 25,
#     'skype': 'bobylab'
# },
#  "Tkachenko Nina Grigorovna": {
#     'telephone': '0972917412',
#     'email': 'ninatkachenko@gmail.com',
#     'position': 'Manager`s assistant',
#     'cabinet number': 10,
#     'skype': 'ninaolina'
# },
# "Boyko Oksana Volodimirovna": {
#     'telephone': '0972588924',
#     'email': 'oksanaboyko@gmail.com',
#     'position': 'Guild master',
#     'cabinet number': 100,
#     'skype': 'urubaroska'
# }
# }
def load(file_user):
    with open(file_user, 'r', encoding='utf-8') as file:
        person = json.load(file)
        return person

def seve(file_user, slowar):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(slowar, file, indent=1)

