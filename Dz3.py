from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str) -> Animal:
        animal_type = animal_type.lower()
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return  Cat()
        else:
            raise  ValueError(f"Неизвестное животное: {animal_type}")

try:
    dog = AnimalFactory.create_animal("Dog")
    cat = AnimalFactory.create_animal("Cat")
    print(f"Собака говорит: {dog.speak()}")
    print(f"Кошка говорит: {cat.speak()}")

    unknown_animal = AnimalFactory.create_animal("Penguin")

except ValueError as e:
    print(f"Ошибка: {e}")
