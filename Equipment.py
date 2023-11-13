class Equipment:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year


    def action(self):
        return 'не определено'


    def __str__(self):
        return f'{self.name}, {self.make}, {self.year}'


class Printer(Equipment):
    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series= series


    def action(self):
        return 'печатает'

    def __str__(self):
        return f'{self.series}, {self.name}, {self.make}, {self.year}'


class Xerox(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)


    def action(self):
        return 'копирует и печатает на листочек'


    def __str__(self):
        return f'{self.name}, {self.make}, {self.year}'

    def get_items(self, ename):
        for item in sklad:
            if isinstance(item, ename):
                print(item)


sklad = []
xerox = Xerox('Xerox','Phaser 3120', 2019)
sklad.append(xerox)
# создаем объект принтер и добавляем
printer = Printer("1200",'hp', 'Laser Jet', 2018)
sklad.append(printer)
# выводим склад
print("На складе имеются:")
for x in sklad:
     print(x,end=' ')
     print(x.action())
# забираем со склада все принтеры
for x in sklad:
     if isinstance(x,Printer):
 	    sklad.remove(x)
# выводим склад
print("\nНа складе осталось:")
for x in sklad:
      print(x,end=' ')
      print(x.action())


















