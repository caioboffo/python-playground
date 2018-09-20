class Me:
    def __init__(self, name):
        self.name = name # unique to each instance
        self.kind = 'canine'
        self.tricks = []

    def change_kind(self, k):
        self.kind = k

    def add_trick(self, trick):
        self.tricks.append(trick)

    def __repr__(self):
        return "I'm %s" % (self.kind)


a = Me('a')
print(a)
b = Me('b')
b.change_kind('feline')
print(b)
c = Me('c')
print(c)
a.add_trick('roll over')
print(a.tricks)
b.add_trick('play dead')
print(c.tricks)
