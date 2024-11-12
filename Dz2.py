class Car:

    def __init__(self, label, model, year, speed):
        self.__label = label
        self.__mobel = model
        self.__year = year
        self.__speed = 0


    @property
    def label(self):
        return self.__label


    @label.setter
    def label(self, value):
        self.__label = value


    @property
    def model(self):
        return self.__mobel


    @model.setter
    def model(self, value):
        self.__mobel = value


    @property
    def year(self):
        return self.__year


    @year.setter
    def year(self, value):
        self.__year = value


    @property
    def speed(self):
        return self.__speed


    def accelerate(self):
        self.__speed += 5


    def decelerate(self):
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0


    def stop(self):
        self.__speed = 0


    def display_speed(self):
        return f"Текущая скорость автомобиля: {self.__speed} км/ч"


    def reverse(self):
        self.__speed = -self.__speed


if __name__ == "__main__":
    my_car = Car("Geely", "Atlas",2022, 45)
    print(f"Марка:{my_car.label},Модель:{my_car.model},Год выпуска:{my_car.year},Скорость:{my_car.speed}")

    my_car.accelerate()
    my_car.accelerate()
    my_car.accelerate()
    print(my_car.display_speed())

    my_car.decelerate()
    print(my_car.decelerate())

    my_car.stop()
    print(my_car.display_speed())

    my_car.reverse()
    print(my_car.display_speed())

    my_car.accelerate()
    print(my_car.display_speed())
