class Stack:
    #EMPTY_SLOT = object()
    EMPTY_SLOT = None

    def __init__(self, size: int):
        self._size = size
        self._stack = [Stack.EMPTY_SLOT] * size
        self._nextFree = 0

    def push(self, item):
        new_item_index = self._nextFree

        if new_item_index >= self._size:
            raise RuntimeError(f"Stack is full ({self._size} items)")

        self._stack[new_item_index] = item
        self._nextFree += 1

        return new_item_index

    def pop(self):
        lastItemIndex = self._nextFree - 1
        removedItem = self._stack[lastItemIndex]

        self._stack[lastItemIndex] = self.EMPTY_SLOT
        self._nextFree -= 1

        return removedItem

    def isFull(self):
        return self._nextFree == self._size

    def isEmpty(self):
        return self._nextFree == 0


Mondeo = "Mondeo"
Golf = "Golf"
Fiesta = "Fiesta"
Punto = "Punto"
Civic = "Civic"
Porsche = "Porsche"

carStack = Stack(6)
print(carStack.push(Mondeo))
print(carStack._stack)
print()

print(carStack.push(Golf))
print(carStack._stack)
print()

print(carStack.isEmpty())
print(carStack._stack)
print()

print(carStack.push(Fiesta))
print(carStack._stack)
print()

print(carStack.push(Punto))
print(carStack._stack)
print()

print(carStack.pop())
print(carStack._stack)
print()

print(carStack.push(Civic))
print(carStack._stack)
print()

print(carStack.push(Porsche))
print(carStack._stack)
print()

print(carStack.isFull())
print(carStack._stack)
print()

print(carStack.pop())
print(carStack._stack)
print()

print(carStack.pop())
print(carStack._stack)
print()
