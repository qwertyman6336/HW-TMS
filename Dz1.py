class MyTime:

    def __init__(self, *args):
        if len(args) == 0:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        elif len(args) == 1 and isinstance(args[0], str):
            time_parts = args[0].split(":")
            self.hours = int(time_parts[0])
            self.minutes = int(time_parts[1])
            self.seconds = int(time_parts[2])
        elif len(args) == 3:
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        elif len(args) == 1 and isinstance(args[0], MyTime):
            self.hours = args[0].hours
            self.minutes = args[0].minutes
            self.seconds = args[0].seconds
        else:
            raise ValueError("Неверный формат входных данных")

        self.normalize_time()

    def normalize_time(self):
        if self.seconds >= 60:
            self.minutes += self.seconds // 60
            self.seconds = self.seconds % 60
        if self.minutes >= 60:
            self.hours += self.minutes // 60
            self.minutes = self.minutes % 60
        if self.hours < 0:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"


    def __eq__(self, other):
        return (self.hours, self.minutes, self.seconds) == (other.hours, other.minutes, other.seconds)


    def __ne__(self, other):
        return not self.__eq__(other)


    def __lt__(self, other):
        return (self.hours, self.minutes, self.seconds) < (other.hours, other.minutes, other.seconds)


    def __le__(self, other):
        return (self.hours, self.minutes, self.seconds) <= (other.hours, other.minutes, other.seconds)


    def __gt__(self, other):
        return not self.__le__(other)


    def __ge__(self, other):
        return not self.__lt__(other)


    def __add__(self, other):
        if isinstance(other, MyTime):
            return MyTime(self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds)
        return MyTime(self.hours, self.minutes, self.seconds + other)


    def __sub__(self, other):
        if isinstance(other, MyTime):
            total_seconds_self = self.to_seconds()
            total_seconds_other = other.to_seconds()
            diff_seconds = total_seconds_self - total_seconds_other
            return MyTime.from_seconds(diff_seconds)
        return MyTime(self.hours, self.minutes, self.seconds - other)


    def __mul__(self, number):
        if isinstance(number, (int, float)):
            total_seconds = self.to_seconds() * number
            return MyTime.from_seconds(int(total_seconds))
        return NotImplemented


    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


    @classmethod
    def from_seconds(cls, total_seconds):
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return cls(hours, minutes, seconds)


if __name__ == "__main__":
    time1 = MyTime("18:54:36")
    time2 = MyTime(00, 53, 00)
    time3 = MyTime(time1)

    print("Time 1:", time1)
    print("Time 2:", time2)
    print("Time 3 (copy of Time 1):", time3)

    print("Time 1 == Time 2:", time1 == time2)
    print("Time 1 != Time 2:", time1 != time2)
    print("Time 1 < Time 2:", time1 < time2)
    print("Time 1 > Time 2:", time1 > time2)

    time4 = time1 + time2
    print("Time 1 + Time 2:", time4)

    time5 = time1 - time2
    print("Time 1 - Time 2:", time5)

    time6 = time1 * 2
    print("Time 1 * 2:", time6)

    time7 = MyTime(25, 61, 61)
    print("Normalized Time 7:", time7)
