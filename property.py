class C(object):
    """Documentation for C"""
    def __init__(self):
        self._voltage = 100

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage

    @voltage.setter
    def voltage(self, value):
        """Set the current voltage"""
        if self._voltage + value > 100000:
            self._voltage = 100000
        else:
            self._voltage += value


if __name__ == '__main__':
    a = C()
    print(a.voltage)
    a.voltage = 140
    print(a.voltage)
    a.voltage = 140128093
    print(a.voltage)
