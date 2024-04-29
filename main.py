'''
1. Создайте базовый класс `Animal`, который будет содержать
общие атрибуты (например, `name`, `age`) и методы (`make_sound()`,
`eat()`) для всех животных.

2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и
`Reptile`, которые наследуют от класса `Animal`. Добавьте
специфические атрибуты и переопределите методы, если требуется
(например, различный звук для `make_sound()`).

3. Продемонстрируйте полиморфизм: создайте функцию
`animal_sound(animals)`, которая принимает список животных и
вызывает метод `make_sound()` для каждого животного.

4. Используйте композицию для создания класса `Zoo`, который будет
содержать информацию о животных и сотрудниках. Должны быть методы
для добавления животных и сотрудников в зоопарк.

5. Создайте классы для сотрудников, например, `ZooKeeper`,
`Veterinarian`, которые могут иметь специфические методы (например,
`feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

Дополнительно:
Попробуйте добавить дополнительные функции в вашу программу, такие
как сохранение информации о зоопарке в файл и возможность её загрузки,
чтобы у вашего зоопарка было "постоянное состояние" между запусками
программы.'''

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass  # этот метод будет переопределен в подклассах

    def eat(self):
        print(f"Животное {self.name} ест")


class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print("Фью-фью")


class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print("Муу!")


class Reptile(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print("Шшш!")


# Демонстрация полиморфизма - через функцию
# `animal_sound(animals)`, которая принимает список животных и
# вызывает метод `make_sound()` для каждого животного.

bird = Bird("Воробей", 2)
bird.make_sound()
bird.eat()

mammal = Mammal("Собака", 3)
mammal.make_sound()
mammal.eat()

reptile = Reptile("Змея", 1)
reptile.make_sound()
reptile.eat()

