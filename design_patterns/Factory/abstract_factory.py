from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def createVegPizza(self):
        pass

    @abstractmethod
    def createNonVegPizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return DeluxVeggiePizza()

    def createNonVegPizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return MexicanVegPizza()

    def createNonVegPizza(self):
        return HamPizza()


class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self, Pizza):
        pass


class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, Pizza):
        pass


class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print('Prepare ', type(self).__name__)


class ChickenPizza(NonVegPizza):
    def serve(self, Pizza):
        print(type(self).__name__,
              ' is served with Chicken on ',
              type(Pizza).__name__)


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print('Prepare ', type(self).__name__)


class HamPizza(NonVegPizza):
    def serve(self, Pizza):
        print(type(self).__name__, ' is server with ham on ',
              type(Pizza).__name__)


class PizzaStore:
    def __init__(self):
        pass

    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)


pizza = PizzaStore()
pizza.makePizzas()
