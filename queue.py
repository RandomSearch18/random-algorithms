class Queue:
    #EMPTY_SLOT = object()
    EMPTY_SLOT = None

    def __init__(self, size: int):
        self._size = size
        self._queue = [Queue.EMPTY_SLOT] * size
        self._nextFree = 0
        self._start = 0

    def push(self, item):
        new_item_index = self._nextFree

        if self.isFull():
            raise RuntimeError(f"Queue is full! ({self._size} items)")

        self._queue[new_item_index] = item
        self._nextFree += 1

        return new_item_index

    def pop(self):
        if self.isEmpty():
            raise RuntimeError("Queue is empty!")

        firstItemIndex = self._start
        removedItem = self._queue[firstItemIndex]

        self._queue[firstItemIndex] = self.EMPTY_SLOT
        self._start += 1

        return removedItem

    def isFull(self):
        return self._nextFree == self._size

    def isEmpty(self):
        return self._start == self._nextFree


queue = Queue(4)
queue.push("A")
queue.push("B")
queue.push("C")
queue.push("D")
print(queue._queue)

while not queue.isEmpty():
    print(queue.pop())
