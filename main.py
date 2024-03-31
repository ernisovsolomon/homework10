'''
Задача 1: Инкапсуляция - Класс Счет
Создайте класс Account с приватным атрибутом balance (баланс)
и методами для депозита и снятия средств, а также для получения текущего баланса.
'''
# class Account:
#     def __init__(self, start_balance) -> None:
#         self.balance = start_balance
#     def deposit(self, amount):
#         if 0 < amount:
#             self.balance += amount
#             print(f'Вы внесли {amount} сом')
#         else:
#             print('Сумма должна быть положительной')
#     def withdraw(self, amount):
#         if 0 < amount and amount <= self.balance:
#             self.balance = self.balance - amount
#             print(f'Вы сняли со счета {amount} сом')
#         else:
#             print('Ошибка операции!')
#     def balance_info(self):
#         print(f'Текущий баланс: {self.balance} сом')
    
# solomon_acc = Account(75000)
# solomon_acc.balance_info()

# solomon_acc.deposit(25000)
# solomon_acc.balance_info()

# solomon_acc.withdraw(74000)
# solomon_acc.balance_info()
'''
Задача 2: Полиморфизм - Классы Животных
Создайте классы Dog и Cat, оба наследуют от класса Animal.
Каждый из классов должен иметь метод speak, который возвращает разные звуки для собаки и кошки.
'''
# class Animails:
#     def __init__(self, animal, name, voice) -> None:
#         self.animal = animal
#         self.name = name
#         self.voice = voice
#     def speak(self):
#         print(f'{self.name} ({self.animal}): {self.voice}')

# cat = Animails('Кошка', 'Маруся', 'МЯУ! МЯУ!')
# dog = Animails('Собака', 'Рекс', 'ГАВ! ГАВ!')
# chicken = Animails('Петух', 'Садыр', 'КУКАРИКУУ!')

# chicken.speak()
'''
Задача 3: Класс Фигура
Создайте класс Shape с методом area, который возвращает площадь.
Создайте производные классы, такие как Rectangle и Circle, переопределяющие метод area.
'''
# class Shape:
#     def area(self):
#         pass

# class Rectangle:
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y
#     def area(self):
#         return self.x * self.y
    
# class Circle:
#     def __init__(self, radius) -> None:
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius ** 2
    
# d_earth = Circle(10)
# print(d_earth.area())

# hd = Rectangle(1920, 1080)
# print(hd.area())
'''
Задача 4: Композиция - Класс Комната
Создайте класс Room с атрибутами, представляющими список мебели.
Используйте композицию, создав отдельные классы для разных типов мебели,
и добавьте их в класс Room.
'''
# class Furniture:
#     def __init__(self, name):
#         self.name = name
    


# class Chair(Furniture):
#     pass

# class Table(Furniture):
#     pass

# class Bed(Furniture):
#     pass


# class Room:
#     def __init__(self, roomname):
#         self.roomname = roomname
#         self.furniture = []

#     def add_furniture(self, item):
#         if isinstance(item, Furniture):
#             self.furniture.append(item)
#         else:
#             pass

#     def remove_furniture(self, item):
#         if item in self.furniture:
#             self.furniture.remove(item)
#         else:
#             print('Такой мебели нет')

#     def room_info(self):
#         print('Список мебели в спальне: ')
#         for item in living_room.furniture:
#             print(f'\t {item.name}')


# bedroom = Room('Спальная комната')
# chair1 = Chair('Кресло AeroCool')
# chair2 = Chair('Кресло Anda Seat')
# table1 = Table('Длинный рабочий стол')
# bed1 = Bed('Кровать на двоих')

# bedroom.add_furniture(chair1)
# bedroom.add_furniture(chair2)
# bedroom.add_furniture(table1)
# bedroom.add_furniture(bed1)


# bedroom.room_info()

# bedroom.remove_furniture(chair1)

# bedroom.room_info()
'''
Задача 5: Абстрактный Класс - Устройство
Создайте абстрактный класс Device с абстрактным методом turn_on.
Создайте производные классы, такие как Laptop и Smartphone, реализующие метод turn_on.
'''
# class Device:
#     def __init__(self, name) -> None:
#         self.name = name
    
# class Laptop(Device):
#     def turn_on(self):
#         print(f'Ваш {self.name} включился!')
# class Smartphone(Device):
#     def turn_on(self):
#         print(f'Ваш {self.name} включился!')

# laptop = Laptop('Macbook')
# phone = Smartphone('iPhone')

# laptop.turn_on()
# phone.turn_on()