from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def do_pay(self):
        pass


class CreditCardPayment(Payment):
    def __init__(self):
        print('Creating creditCard Payment method')

    def do_pay(self):
        print('Payment with credit card')


if __name__ == '__main__':
    '''if you do not implement abstractmethods you cannot instantiate the
    class properly'''
    p = CreditCardPayment()
    p.do_pay()
