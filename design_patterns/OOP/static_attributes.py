class MyClass:
    i = 3

    def __init__(self):
        self.name = None


if __name__ == '__main__':
    a = MyClass()
    b = MyClass()
    c = MyClass()
    a.name = 'A'
    b.name = 'B'
    c.name = 'C'

    a.i = 4
    print(a.i, MyClass.i, c.i)
