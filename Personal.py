import json
print("Вас вітає інформаційна система співробітники")
sotrudniki = {}

def add_sotrudnik():
  "Функція додавання співробітника"
  print("Для виходу введіть Y")
  add_keys = ['Телефон', 'Пошта', 'Посада']#Зарезервовані ключі
  add_value = []#Список значень для рез.ключів
  sotr_key = input("Введіть ФІО співробітника - ").title()
  if sotr_key.lower() == "y":
    return
  telefon = str(input("Введіть номер телефону - "))
  if telefon.lower() == "y":
    return
  add_value.append(telefon)
  set_email = str(input("Введіть пошту - "))
  if set_email.lower() == "y":
    return
  add_value.append(set_email)
  positions = str(input("Введіть посаду - "))
  if positions.lower() == "y":
    return
  add_value.append(positions)

  keys = dict(zip(add_keys,add_value))#Формування ще одного словаря

  sotrudniki.update({sotr_key: keys})#Додавання ФІО як ключа і його значення словника keys
  kolo = input("Хочете добавити ще співробітника Y|N\n--> ")
  if kolo.lower() == 'Y':
    add_sotrudnik()

def update_sotrudnik():
  """Внесення мін співробітнику"""
  print("Для виходу введіть Y")
  sotr_key = input("Введіть ФІО співробітника для внесеня змін - ")
  if sotr_key.lower() == "y":
    return
  if sotr_key not in sotrudniki:
    return print("Не знайденно такого співробітника\n")
  def viborka():
    vibor = int(input('''Введіть цифру того що хочете змінити
  1.Телефон
  2.Пошту
  3.Посаду\n- '''))
    if vibor.lower() == "y":
      return
    if vibor > 3 or vibor < 1:
      print("Не правильно вказаний параметр\n")
      viborka()
    else:
      return vibor
  vibor = viborka()
  zmina = str(input("Введіть нове значення - "))
  if zmina.lower() == "y":
    return
  if vibor == 1:
    sotrudniki[sotr_key]['Телефон'] = zmina
  elif vibor == 2:
    sotrudniki[sotr_key]['Пошта'] = zmina
  elif vibor == 2:
    sotrudniki[sotr_key]['Посада'] = zmina

  print("Внесення змін виконано\n")

def udalenie_sotrudnik():
  """Функція видалення співробітника"""
  print("Для виходу введіть Y")
  vibor = input("Введіть ФІО співробітника - ")
  if vibor.lower() == "y":
    return
  if vibor not in sotrudniki:
    return print("Не знайденно такого співробітника\n")
  else:
    del sotrudniki[vibor]

def search_familia():
  "Функція пошуку по фамілії"
  print("Для виходу введіть Y")
  search = str(input("Введіть фамілію для пошуку - "))
  if search.lower() == "y":
    return
  for i in sotrudniki.keys():
    rozbitie = i.split()
    if rozbitie[0] == search:
      result = sotrudniki[i]

  if result == False:
    print("Нічого не знайденно")
  else:
    print(result)
    save = input("Бажаєте зберегти результат пошуку в файл Y|N\n- ")
    if save.lower() == "y":
      with open('result_poisk.json', 'w', encoding='utf-8') as file:
        json.dump(result, file)

def search_bukva():
  "Функція пошуку по букві"
  print("Для виходу введіть Y")
  result = {}
  search = str(input("Введіть букву для пошуку - ")).title()
  if search.lower() == "y":
    return
  for i in sotrudniki.keys():
    rozbitie = i.split()
    if rozbitie[0][0] == search:
      result.update({i:sotrudniki[i]})

  if result == False:
    print("Нічого не знайденно")
  else:
    print(result)
    save = input("Бажаєте зберегти результат пошуку в файл Y|N\n- ")
    if save.lower() == "y":
      with open('result_poisk.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=3)

try:
  with open('result_poisk.json', 'r', encoding='utf-8') as file:
    sotrudniki = json.load(file)
except:
  sotrudniki = {}
while True:

  print(sotrudniki)
  print("Для виходу введіть Y")
  try:
    kursor = int(input("""Введіть цифру потрібної вам функції
  1.Додавання до списку
  2.Видалення з списку
  3.Редагування співробітника
  4.Пошук по фамілії
  5.Пошук по букві
  6.Вихід\n---> """))
  except:
    continue
  if kursor > 6 or kursor < 1:
    print("Не правильно вказаний параметр\n")
  elif kursor == 1:
    add_sotrudnik()
  elif kursor == 2:
    udalenie_sotrudnik()
  elif kursor == 3:
    update_sotrudnik()
  elif kursor == 4:
    search_familia()
  elif kursor == 5:
    search_bukva()
  elif kursor == 6:
    with open('result_poisk.json', 'w', encoding='utf-8') as file:
      json.dump(sotrudniki, file, indent=3)
    break