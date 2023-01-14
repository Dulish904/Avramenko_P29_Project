import json
print("Вас вітає інформаційна система співробітники")
sotrudniki = {'Avramenko Bogdan Vitaliyovich': {'Телефон':'0973112810', 'Пошта':'eli@gmail.com', 'Посада':'Operator'},
              'Calbonar Bogdan Vitaliyovich': {'Телефон':'0973112810', 'Пошта':'eli@gmail.com', 'Посада':'Operator'},
              'Avramenko Vitaliy Vitaliyovich': {'Телефон':'0973112810', 'Пошта':'eli@gmail.com', 'Посада':'Operator'}}

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
  kolo = input("Хочете добавити ще співробітника Y|N")
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

def seach_familia():
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

seach_familia()
print(sotrudniki)