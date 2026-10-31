class human:
    def __init__(self, name='Human'):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers=[]

    def add_passanger(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passengers(self):
        if self.passengers != []:
            print(f'Names of {self.brand} passengers:')
            for passenger in self.passengers:
                print(passenger.name)

        else:
            print(f'There are no passengers in {self.brand}')

nick=human('Nick')
kate=human('Kate')
car=Auto('Car')

car.add_passanger(nick)
car.add_passanger(kate)
car.print_passengers()