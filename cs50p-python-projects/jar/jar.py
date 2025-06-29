def main():
    jar = Jar()
    jar.deposit(5)
    print(jar)
    jar.withdraw(2)
    print(jar)


class Jar:
    def __init__(self, capacity=12):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot deposit negative number of cookies")
        if self._size + n > self._capacity:
            raise ValueError("Jar will overflow")
        self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw negative number of cookies")
        if n > self._size:
            raise ValueError("Nom nom nom")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


main()
