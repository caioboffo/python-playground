class A(object):
    def a1(self):
        print("a1")


class B(object):
    def b(self):
        print("b")
        A().a1()


objectB = B()
objectB.b()
