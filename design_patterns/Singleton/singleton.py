class Singleton(object):
    ''' a singleton class example '''
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


print('Simple Singleton class Example...')
s = Singleton()
print('Object created', s)

s1 = Singleton()
print('Object created', s1)


class LazySingleton(object):
    ''' a lazy singleton class example '''
    __instance = None

    def __init__(self):
        if not LazySingleton.__instance:
            print(' __init__ method called..')
        else:
            print('Instance already created:', self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = LazySingleton()
            return cls.__instance


print('Simple LazySingleton class Example...')
s = LazySingleton()  # class initalized, but not created
print('Object created', LazySingleton.getInstance())  # object is created here
s1 = LazySingleton()
