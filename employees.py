class Employee:
    'Documentation for Employee'


    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        print(self.name, "does sutff")

    def __str__(self):
        return "<Employee: name=%s, salary=%s>" % (self.name, self.salary)


class Chef(Employee):
    """Documentation for Chef

    """
    def __init__(self, name):
        Employee.__init__(self, name, 50000)

    def work(self):
        print(self.name, "makes food")


class Server(Employee):
    """Documentation for Server

    """
    def __init__(self, name):
        Employee.__init__(self, name, 40000)

    def work(self):
        print(self.name, "interfaces with customer")


class PizzaRobot(Chef):
    """Documentation for PizzaRobot

    """
    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        print(self.name, "makes pizza")


if __name__ == "__main__":
    bob = PizzaRobot('bob')
    print(bob)
    bob.work()
    bob.giveRaise(0.20)
    print(bob); print()

    for klass in Employee, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__)
        obj.work()
