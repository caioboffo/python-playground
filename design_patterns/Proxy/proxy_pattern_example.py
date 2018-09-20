from abc import ABCMeta, abstractmethod


class You:
    def __init__(self):
        print("You:: lets buy the Denim shirt")
        self.debitCard = DebitCard()
        self.isPurchased = None

    def make_payment(self):
        self.isPurchased = self.debitCard.do_pay()

    def __del__(self):
        if self.isPurchased:
            print("You:: Wow! Denim shirt is mine :-)")
        else:
            print("You:: I should earn more:(")


class Payment(metaclass=ABCMeta):
    """Documentation for Payment"""
    @abstractmethod
    def do_pay(self):
        pass


class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None

    def __getAccount(self):
        self.account = self.card
        return self.account

    def __hasFunds(self):
        print("Bank:: CHecking if Account", self.__getAccount(),
              "has enough funds")
        return True

    def setCard(self, card):
        self.card = card

    def do_pay(self):
        if self.__hasFunds():
            print("Bank:: Paying the merchant")
            return True
        else:
            print("Bank:: Sorry, not enough funds")
            return False


class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input("Proxy:: Punch in Card Number")
        self.bank.setCard(card)
        return self.bank.do_pay()


if __name__ == '__main__':
    you = You()
    you.make_payment()
