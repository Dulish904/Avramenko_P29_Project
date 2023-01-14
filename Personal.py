print("Вас вітає інформаційна система співробітники")
sotrudniki = {}

def add_sotrudnik():
  add_keys = ['Telephone', 'Email', 'Position']
  add_value = []
  sotr_key = input("Введіть ФІО співробітника - ")
  keys = dict.fromkeys(add_keys, None)

  telefon = str(input("Введіть номер телефону - "))
  sotrudniki.setdefault(sotrudniki[sotr_key]['Telephone'], telefon)
  set_email = str(input("Введіть емайл - "))
  sotrudniki.setdefault(sotrudniki[sotr_key]['Email'], set_email)
  positions = str(input("Введіть посаду - "))
  sotrudniki.setdefault(sotrudniki[sotr_key]['Position'], positions)

  sotrudniki.update({sotr_key: keys})


add_sotrudnik()
print(sotrudniki)