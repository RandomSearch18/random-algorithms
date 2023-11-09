class Stack:
    EMPTY_SLOT = object()

    def __init__(self, size: int):
        self._size = size
        self._stack = [Stack.EMPTY_SLOT] * size
        self._top = 0

    def push(self, item):
        if self._top == self._size:
            raise RuntimeError(f"Stack is full ({self._size} items)")

        self._stack[self._top] = item
        self._top += 1

    def pop(self):
        self._stack[self._top] = self.EMPTY_SLOT
        self._top -= 1

    def isFull(self):
        return self._top == self._size

    def isEmpty(self):
        return self._top == 0


Mondeo = "Mondeo"
Golf = "Golf"
Fiesta = "Fiesta"
Punto = "Punto"
Civic = "Civic"
Porsche = "Porsche"

carStack = Stack(6)
carStack.push(Mondeo)
carStack.push(Golf)
carStack.isEmpty()
carStack.push(Fiesta)
carStack.push(Punto)
carStack.pop()
carStack.push(Civic)
carStack.push(Porsche)
carStack.isFull()
carStack.pop()
carStack.pop()
