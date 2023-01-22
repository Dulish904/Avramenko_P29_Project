import random


class Human:

    def __init__(self, name='Human',job=None,home=None,car=None):
        self.name=name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home =home

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self,mange):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                mange = 'fuel'
            else:
                self.to_repair()
                return
        if mange == 'fuel':
            print('I bought fuel')
            self.money -= 100
            self.car.fuel += 100
        elif mange == 'food':
            print('Bought food')
            self.money -= 50
            self.home.food += 50
        elif mange == 'delicacies':
            print('Hooray! Delicacies')
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -=5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -=50

    def kazino(self):
        stavka = int(input("Введіть суму ставки - "))
        if Kazino(stavka).stavka == True:
            print("You win!")
            self.money += stavka
        else:
            print("You lose! LOL")
            self.money -= stavka

    def days_indexes(self, day):
        day = f"Today the {day}of {self.name}'s life"
        print(f"{day:=^50}","\n")
        human_indexes = self.name+"'s indexes"
        print(f'{human_indexes:^50}','\n')
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        home_indexes = 'Home indexes'
        print(f"{home_indexes:=^50}",'\n')
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:=^50}",'\n')
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")

    def in_alive(self):
        if self.gladness < 0:
            print('Depression...')
            return False
        if self.satiety < 0:
            print('Dead...')
            return False
        if self.money < -500:
            print("Bankrupt...")
            return False

    def live(self, day):
        if self.in_alive() == False:
            return False
        if self.home is None:
            print("Settlend in house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car{self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I dont have a job, i'm going get a job {self.job} with salary {self.job}")
        self.days_indexes(day)
        dice = int(input('Enter 1 for chill, enter 2 for work, 3 for Clean, 4 for treats, 5 for eat, 6 to repair car, 7 go kazino = '))
        if dice == 5:
            print("I ll go eat")
            self.eat()
        elif dice == 1:
            print("Lets chill")
            self.chill()
        elif dice == 2:
            print("Go to work")
            self.work()
        elif dice == 3:
            print("Cleaning time")
            self.clean_home()
        elif dice == 4:
            print("Time for treats")
            self.shopping(mange='delicacies')
        elif dice == 6:
            print("I ned to repair my car")
            self.to_repair()
        elif dice == 7:
            print("I go play kazino")
            self.kazino()

class Auto:

    def __init__(self, brend_list):
        self.brand = random.choice(list(brend_list))
        self.fuel = brend_list[self.brand]['fuel']
        self.strength = brend_list[self.brand]['strength']
        self.consuption = brend_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consuption:
            self.fuel -= self.consuption
            self.strength -= 1
        else:
            print('The car connot move')
            return False

class House:

    def __init__(self):
        self.food = 0
        self.mess = 0

class Job:

    def __init__(self, job_list1):
        self.job = random.choice(list(job_list1))
        self.salary = job_list1[self.job]['salary']
        self.gladness_less = job_list1[self.job]['gladness_less']

class Kazino:

    def __init__(self, stavka):
        self.stavka = stavka

    def udacha(self):
        baraban = random.randint(1,2)
        if baraban == 1:

            return True
        else:
            return False


brands_of_car={'BMW':{'fuel':100,'strength':100,'consumption':6},
               "Peugeot":{'fuel':50,'strength':40,'consumption':10},
               "Volvo":{'fuel':70,'strength':150,'consumption':8},
               "Ferrari":{'fuel': 80,'strength': 120,'consumption': 14}
               }

job_list = {"Java developer":{'salary':50,'gladness_less':10},
            "Python developer":{'salary':45,'gladness_less':3},
            "C++ developer":{'salary':40,'gladness_less':15},
            "Rust developer":{'salary':44,'gladness_less':5}
            }

nick = Human(name='Nick')
for day in range(1, 8):
    if nick.live(day) == False:
        break

