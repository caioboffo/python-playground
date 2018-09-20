class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return 'Date({}, {}, {})'.format(self.year, self.month, self.day)

    def set_date(self, y, m, d):
        self.year = y
        self.month = m
        self.day = d

    @classmethod
    def from_str(cls, date_str):
        '''creates an abstract method that can be used as
        a static factory method for the date class'''
        year, month, day = map(int, date_str.split('-'))
        return cls(year, month, day)


class A(object):
    def foo(self, x):
        print("executing foo(%s, %s)" % (self, x))

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s, %s)" % (cls, x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)


a = A()
