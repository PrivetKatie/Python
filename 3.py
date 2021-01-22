class Worker:

    name = 'Kate'
    surname = 'Lobanova'
    position = 'Sales Manager'
    _income = {'wage': 30000, 'bonus': 15000}


class Position(Worker):

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])


worker_1 = Position()
worker_1.get_full_name()
worker_1.get_total_income()