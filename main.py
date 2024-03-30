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