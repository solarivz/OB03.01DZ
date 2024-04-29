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
import pickle
class Animal():
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

class Zoo():
    def __init__(self):
        self.animals = []
        self.staffs = []


    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff):
        self.staffs.append(staff)

    def view_animals(self):
        print("Животные в зоопарке:")
        for a in self.animals:
            print(a.name)
    def view_staffs(self):
        print("Служащие в зоопарке:")
        for s in self.staffs:
            print(s.name)
    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f"{animal.name} удален из зоопарка.")
        else:
            print(f"{animal.name} не найден в зоопарке.")

    def remove_staff(self, staff):
        if staff in self.staffs:
            self.staffs.remove(staff)
            print(f"{staff.name} удален из списка сотрудников зоопарка.")
        else:
            print(f"{staff.name} не найден в списке сотрудников зоопарка.")


class Employee():
    def __init__(self, name, age):
        self.name = name
        self.age = age
class ZooKeeper(Employee):

    def feed_animal(self, animal):
        print(f"Смотритель зоопарка кормит {animal.name}.")


class Veterinarian(Employee):
    def heal_animal(self, animal):
        print(f"Ветеринар лечит {animal.name}.")


# Демонстрация полиморфизма - через функцию
# `animal_sound(animals)`, которая принимает список животных и
# вызывает метод `make_sound()` для каждого животного.


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Функция для сохранения объекта зоопарка в файл
def save_zoo(zoo):
    filename = 'zoo_data.pkl'
    with open(filename, 'wb') as file:
        pickle.dump(zoo, file)
    print(f"Объекты зоопарка сохранены в файл {filename}.")

# Функция для загрузки объекта зоопарка из файла
def load_zoo():
    try:
        with open('zoo_data.pkl', 'rb') as file:
            zoo = pickle.load(file)
            print("Объекты зоопарка загружены из файла.")
            return zoo
    except FileNotFoundError:
        print("Файл с данными зоопарка не найден.")
        return None

# Пример использования функции animal_sound с использованием списка обьектов животных:
animals = [Bird("Воробей", 2), Mammal("Собака", 3), Reptile("Змея", 1)]
animal_sound(animals)


# Создаем обьект Зоопарк
zoo = Zoo()
# Добавим обьекты животных в Зоопарк из списка
for animal in animals:
    zoo.add_animal(animal)
# Посмотрим обьекты животных в Зоопарке
zoo.view_animals()

# Создаем объекты сотрудников
employee1 = ZooKeeper("Иван", 30)
employee2 = ZooKeeper("Мария", 25)
employee3 = Veterinarian("Петр", 35)

# Добавляем сотрудников в зоопарк
zoo.add_staff(employee1)
zoo.add_staff(employee2)
zoo.add_staff(employee3)

# Проверяем, что сотрудники добавлены
zoo.view_staffs()

# Кормим и лечим животных
zoo.staffs[0].feed_animal(animals[0])
zoo.staffs[2].heal_animal(animals[2])

# Основной цикл программы
while True:
    print("\nВыберите действие:")
    print("1. Просмотреть животных в зоопарке")
    print("2. Просмотреть сотрудников зоопарка")
    print("3. Добавить животное в зоопарк")
    print("4. Удалить животное из зоопарка")
    print("5. Добавить сотрудника в зоопарк")
    print("6. Удалить сотрудника из зоопарка")
    print("7. Сохранить объекты зоопарка в файл")
    print("8. Загрузить объекты зоопарка из файла")
    print("9. Выйти из программы")

    choice = input("Введите номер действия: ")

    if choice == '1':
        zoo.view_animals()
    elif choice == '2':
        zoo.view_staffs()
    elif choice == '3':
        name = input("Введите имя животного: ")
        age = int(input("Введите возраст животного: "))
        animal = Animal(name, age)
        zoo.add_animal(animal)
        print(f"{animal.name} добавлен в зоопарк.")
    elif choice == '4':
        name = input("Введите имя животного для удаления: ")
        animal = next((a for a in zoo.animals if a.name == name), None)
        if animal:
            zoo.remove_animal(animal)
        else:
            print(f"{name} не найден в зоопарке.")
    elif choice == '5':
        name = input("Введите имя сотрудника: ")
        age = int(input("Введите возраст сотрудника: "))
        staff_type = input("Введите тип сотрудника (zookeeper/veterinarian): ").lower()
        if staff_type == 'zookeeper':
            staff = ZooKeeper(name, age)
        elif staff_type == 'veterinarian':
            staff = Veterinarian(name, age)
        else:
            print("Некорректный тип сотрудника.")
            continue
        zoo.add_staff(staff)
        print(f"{staff.name} добавлен в список сотрудников зоопарка.")
    elif choice == '6':
        name = input("Введите имя сотрудника для удаления: ")
        staff = next((s for s in zoo.staffs if s.name == name), None)
        if staff:
            zoo.remove_staff(staff)
        else:
            print(f"{name} не найден в списке сотрудников зоопарка.")
    elif choice == '7':
        save_zoo(zoo)
    elif choice == '8':
        zoo = load_zoo()
    elif choice == '9':
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор. Пожалуйста, введите номер от 1 до 9.")