filename = 'Sotrudniki.txt'
personal = {}

def add_personal():
  """Функція додавання персоналу"""
  bufer = {}#Для тимчасового зберігання перед додаванням
  fio = input("Введіть ФІО працівника - ")
  bufer.setdefault(fio)#Додавання в буфер
  flag = True
  print("--Для виходу введіть 'Esc'--")
  while flag:
    print()
    key_a = input("Введіть ключ - ")
    if 'esc' == key_a.lower():
      break
    valua_a = input("Введіть значення - ")
    if 'esc' == valua_a.lower():
      break
    bufer[fio][key_a,valua_a]
  personal.update(bufer)
  
add_personal()
print(personal)
  