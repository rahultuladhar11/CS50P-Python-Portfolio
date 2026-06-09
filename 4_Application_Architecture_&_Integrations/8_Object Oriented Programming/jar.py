class Jar:
    def __init__(self, capacity=12):
        # Validate the capacity
        if not isinstance(capacity, int):
            raise ValueError("capacity must be an integer")
        if capacity < 0:
            raise ValueError("capacity must be non-negative")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        # Return “🍪” repeated self._size times
        return "🍪" * self._size

    def deposit(self, n):
        if not isinstance(n, int):
            raise ValueError("n must be an integer")
        if n < 0:
            raise ValueError("n must be non-negative")
        if self._size + n > self._capacity:
            raise ValueError("exceeds capacity")
        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int):
            raise ValueError("n must be an integer")
        if n < 0:
            raise ValueError("n must be non-negative")
        if n > self._size:
            raise ValueError("not enough cookies to withdraw")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

cookie = Jar(100)
print(cookie.capacity)
print(cookie.size)

cookie.deposit(50)
cookie.withdraw(2)

print(cookie)
print(cookie.size)

print(cookie.deposit)
