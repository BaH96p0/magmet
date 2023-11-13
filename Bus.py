class Bus:
    def __init__(self, capacity, max_speed):
        self.speed = 0
        self.capacity = capacity
        self.max_speed = max_speed
        self.passengers = []
        self.has_empty_seats = True
        self.seats = {i: None for i in range(1, capacity + 1)}

    def embark(self, *passenger_names):
        for name in passenger_names:
            if self.has_empty_seats:
                empty_seat = next(i for i, occupant in self.seats.items() if occupant is None)
                self.seats[empty_seat] = name
                self.passengers.append(name)
                if len(self.passengers) == self.capacity:
                    self.has_empty_seats = False
                print(f"{name} сел в автобус на место {empty_seat}.")
            else:
                print("Автобус полон. Посадка невозможна.")

    def disembark(self, *passenger_names):
        for name in passenger_names:
            if name in self.passengers:
                seat = next(i for i, occupant in self.seats.items() if occupant == name)
                self.seats[seat] = None
                self.passengers.remove(name)
                self.has_empty_seats = True
                print(f"{name} вышел из автобуса с места {seat}.")
            else:
                print(f"{name} не находится в автобусе.")

    def accelerate(self, speed_increase):
        self.speed = min(self.max_speed, self.speed + speed_increase)
        print(f"Скорость увеличена на {speed_increase} км/ч. Текущая скорость: {self.speed} км/ч.")

    def decelerate(self, speed_decrease):
        self.speed = max(0, self.speed - speed_decrease)
        print(f"Скорость уменьшена на {speed_decrease} км/ч. Текущая скорость: {self.speed} км/ч.")

    def __contains__(self, passenger_name):
        return passenger_name in self.passengers

    def __iadd__(self, passenger_name):
        self.embark(passenger_name)
        return self

    def __isub__(self, passenger_name):
        self.disembark(passenger_name)
        return self


bus = Bus(capacity=10, max_speed=60)

print("Текущая скорость автобуса:", bus.speed)
bus.accelerate(20)

bus.embark("Alice", "Bob", "Charlie")
print("Пассажиры в автобусе:", bus.passengers)

bus.decelerate(10)

if "Alice" in bus:
    print("Alice находится в автобусе.")
else:
    print("Alice не находится в автобусе.")

bus += "David"
bus.disembark("Bob")
print("Пассажиры в автобусе после высадки Bob:", bus.passengers)