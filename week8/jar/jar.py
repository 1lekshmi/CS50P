class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid number")
        self._capacity = capacity
        self._size = 0
    
    def __str__(self):
        return "🍪" * self._size

    def deposit(self,n):
        if n > self._capacity or n < 0 or n + self._size > self._capacity:
            raise ValueError("Invalid number")
        self._size += n

    def withdraw(self,n):
        if n < 0 or self.size - n < 0:
            raise ValueError("Invalid number")
        self._size -=n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    cookie_jar = Jar(100)
    # cookies = 0
    
    cookie_jar.deposit(50)
    # cookies = 50

    cookie_jar.withdraw(6)
    # cookies = 44 = size

    print(cookie_jar.size)
    print(cookie_jar.capacity)
    

if __name__ == "__main__":
    main()

