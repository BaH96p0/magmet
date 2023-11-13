class Passport:
    def __init__(self, first_name, last_name, date_of_birth, country, passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.date_of_birth = date_of_birth
        self.passport_number = passport_number

    def print_info(self):
        print(f'''
Full name: {self.first_name} {self.last_name}
Date of birth: {self.date_of_birth}
Country: {self.country}
Passport: {self.passport_number}
''')


class ForeignPassport(Passport):
    def __init__(self, first_name, last_name, country, date_ot_birth, passport_number, visa):
        super().__init__(first_name, last_name, country, date_ot_birth, passport_number)
        self.visa = visa

    def print_info(self):
        super().print_info()
        print(f'Visa: {self.visa}')


p = Passport('Vanya', 'Loxov', '14.12.1244', 'Rusiya', 121343)
print(p.print_info())
fp = ForeignPassport('Sasha', 'Durakov', '14.12.1488', 'omerika', 131343, 'kitay')
print(fp.print_info())
