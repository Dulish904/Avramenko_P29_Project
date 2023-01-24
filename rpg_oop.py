import random

armor = {
    "Кожаний нагрудник": {
        'захист': 15,
        'ціна': 150
    },
    "Залізний нагрудник": {
        'захист': 25,
        'ціна': 300
    },
    "Адамантовий нагрудник": {
        'захист': 50,
        'ціна': 500
    }
}  # Список для магазина
sword = {
    "Тупий залізний меч": {
        'поріз': 15,
        'ціна': 250
    },
    "Меч закаленої сталі": {
        'поріз': 23,
        'ціна': 620
    },
    "Адамантовий меч": {
        'поріз': 35,
        'ціна': 800
    }
}  # Список для магазина

monster = {
    "Вовк": {
        "Життя": 100,
        "Сила": 9,
        "Спритність": 15,
        "Захист": 4
    },
    "Гоблін": {
        "Життя": 150,
        "Сила": 15,
        "Спритність": 12,
        "Захист": 9
    },
    "ХобГоблін": {
        "Життя": 250,
        "Сила": 24,
        "Спритність": 6,
        "Захист": 15
    },
}  # Список монстрів
bos = {
    "Громовий залізно зуб": {
        "Життя": 500,
        "Сила": 30,
        "Спритність": 15,
        "Захист": 10
    },
    "Арахна": {
        "Життя": 350,
        "Сила": 20,
        "Спритність": 30,
        "Захист": 9
    },
}  # Список босів


class Player():
    """Основний клас. В якому буде відбуватися симуляція"""

    def __init__(self, name="Player", armor=None, sword=None):
        self.name = name
        self.level = 1
        self.experience_points = 0
        self.next_level_point = 250
        self.hp = 100
        self.strength = 25
        self.dexterity = 10
        self.armor = armor
        self.defence = 0
        self.sword = sword
        self.money = 250

    def get_level(self):  # Додавання левелу
        if self.experience_points == self.next_level_point:
            self.level += 1

    def onster_info(self):
        print(f"{'Ліс':-^50}")
        enemy = Forest()
        print(f"{'Ваш супротвник'}:-^50")
        print(f"{enemy.monsters}:-^50")
        print(f"ХП - {enemy.hp}")
        print(f"Захист - {enemy.defence}")
        print(f"Сила - {enemy.strength}")
        print(f"Спритність - {enemy.dexterity}")

    def fight(self):
        pass

    def receiving_damage(self, damage):
        pass

    def ran(self):
        pass

    def go_shoping(self):  # Похід в магазин
        shop_list = Shoping.equment()
        if self.money < shop_list[2]:
            print('-' * 50)
            print("У мене недостатньо коштів для покупки цього")
            print('-' * 50)
        else:
            self.money - shop_list[2]
            if shop_list[3] == 'Armor':
                self.armor = shop_list[0]
                self.defence = shop_list[1]
            else:
                self.sword = shop_list[0]
                self.strength += shop_list[1]

    def go_bar(self):
        Shoping.bar()
        self.money -= 5

    def go_forest(self):
        pass

    def go_guild(self):
        pass

    def chill(self):
        print('-' * 50)
        print("Ви відпочили")
        print('-' * 50)
        self.hp = 100

    def status(self):
        print(f"{self.name:-^50}")
        print(f"Рівень - {self.level}")
        print(f"{'Характеристики':-^50}")
        print(f"Життя - {self.hp}")
        print(f"Захист - {self.defence}")
        print(f"Сила - {self.strength}")
        print(f"Спритність - {self.dexterity}")
        print(f"{'Речі':-^50}")
        print(f"Натільник - {self.armor}")
        print(f"Зброя - {self.sword}")
        print('-' * 50)


class Shoping:

    def equment():  # Магазин закупки спорядження
        print(f"{'Магазин спорядження':-^50}")
        print("Тут ви можете закупити собі спорядження")
        print(f"{'Захист':-^50}")
        point = 1
        for name in armor.keys():
            print(f"{point}.{name} - захист: {armor[name]['захист']} - ціна = {armor[name]['ціна']}")
            point += 1
        print(f"{'Меч':-^50}")
        for name in sword.keys():
            print(f"{point}.{name} - поріз: {sword[name]['поріз']} - ціна = {sword[name]['ціна']}")
            point += 1
            print(f"{point}.Вихід")
        print(f"{'Введіть':-^50}")
        buy = int(input("Номер товару - "))
        if buy == 1:
            return ['Кожаний нагрудник', 15, 150, 'Armor']
        elif buy == 2:
            return ['Залізний нагрудник', 25, 300, 'Armor']
        elif buy == 3:
            return ['Адамантовий нагрудник', 50, 500, 'Armor']
        elif buy == 4:
            return ['Тупий залізний меч', 15, 250, 'Sword']
        elif buy == 5:
            return ['Меч закаленої сталі', 23, 620, 'Sword']
        elif buy == 6:
            return ['Адамантовий меч', 35, 800, 'Sword']
        elif buy == 7:
            return None

    def bar():  # Бар. Просто добавив щоб був
        print(f"{'Бар':-^50}")
        print(f"Ви добре відпочили в барі і витратили 5 монет")
        print('-' * 50)


class Forest:
    def __init__(self):
        self.monster_gen = random.randint(1, 6)
        if self.monster_gen > 5:
            self.monsters = random.choice(list(bos))
            self.hp = bos[self.monsters]['Життя']
            self.strength = bos[self.monsters]['Сила']
            self.dexterity = bos[self.monsters]['Спритність']
            self.defence = bos[self.monsters]['Захист']
        else:
            self.monsters = random.choice(list(monster))
            self.hp = monster[self.monsters]['Життя']
            self.strength = monster[self.monsters]['Сила']
            self.dexterity = monster[self.monsters]['Спритність']
            self.defence = monster[self.monsters]['Захист']


class Guild:
    pass


