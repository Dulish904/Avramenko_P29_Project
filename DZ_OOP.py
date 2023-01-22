from random import randint
class DasAuto():
  """Клас ДасАвто. З машинами я не сильно дружу фантазії на них не хватило("""
  def __init__(self,model, age, meiden):
    self.model = model
    self.age = age
    self.meiden = meiden

  def info_car(self):
    """Функція для вивидення основної інформація про авто"""
    print('='*25)
    print(f"Модель - {self.model}\nРік - {self.age}\nВиробник - {self.meiden}")
    print('='*25)

  def prohod_car(self,km):
    """Функція для вивидення проходумашини"""
    print('='*25)
    print(f"{self.model} була в вжитку і уже пройшла {km} кілометрів")
    print('='*25)

class Book():
  """Клас книга. Видід інформації і маленька гра на щастя"""
  def __init__(self,name,age,publisher,genre,author,price):
    self.name = name
    self.age = age
    self.publisher = publisher
    self.genre = genre
    self.author = author
    self.price = price

  def informationBook(self):
    """Функлія класу Книга. Виводить інформацію про книгу."""
    print('='*25)
    print(f"Назва книги - {self.name}\nРік видавництва - {self.age}\nВидавництво - {self.publisher}\nЖанр - {self.genre}\nАвтор -{self.author}\nЦіна - {self.price}")
    print('='*25)

  def visitor_book(self,used=0):
    """Функція для вивидення кількості читачів які володіли цією книгою"""
    print('='*25)
    print(f"{self.name} вже брало на прочитання {used} читачів.")
    print('='*25)

  def health_book(self,used):
    """Функція гра на везіння. Чи дожива книга якщо її будуть використовувати задана кількість читачів. Хай щастить"""
    health = 1000
    for i in range(used):
      damage = randint(1,15)#Генерую рандомне пошкодження
      health -= damage
      print(f"{self.name} читач наніс ушкоджень на {damage}")
      print(f"Життя - {health}")
      if health <= 0:#Вивід інформації після повернення книги
        print(f"{self.name} вже в дуже поганому стані, прочитати її вже неможливо")
        break
      elif health <= 25:
        print(f"{self.name} пошкодженна але ще можна читати")
      elif health <= 50:
        print(f"{self.name} дуже пошкодженна ледве можна прочитати")


class Stadium():
  """Клас стадіон. Може виводити інформацію а також бронювання стадіона"""
  def __init__(self,name,date_open,country,city,capacity):
    self.name = name
    self.date_open = date_open
    self.country = country
    self.city = city
    self.capacity = capacity

  def information_on_Stadium(self):
    print('='*25)
    print(f"Стадіон {self.name} знаходиться в {self.country} місто {self.city} був відкритий в {self.date_open} і може вмістити в собі {self.capacity}")
    print('='*25)

  def bronirovanie(self,data,time_bron,price,contest,team_1,team_2):
    """Бронювання стадіона.Виводить оголошення,хто проти кого яке змагання коли і о котрій й ціну входу відбудеться матч.
    Потрібно передати дату, час, ціна, вид змагання й двох участників"""
    print(f"{data} на стадіоні {self.name} в {time_bron} буде проходити матч по {contest}у між {team_1} і {team_2} ціна входу {price}грн")

