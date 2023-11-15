class Queue:
    EMPTY_SLOT = None

    def __init__(self, length: int):
        self._length = length
        self._queue = [self.EMPTY_SLOT] * length
        self._next_free_slot = 0

    def calculate_next_free_slot(self, start_from: int) -> int:
        current_index = start_from + 1
        while current_index != self._length:
            if self._queue[current_index] == self.EMPTY_SLOT:
                return current_index
            current_index += 1

        # Couldn't find a free slot before the end of the array,
        # so check for empty slots at the start
        return self.calculate_next_free_slot(0)

    def enqueue(self, item):
        current_slot = self._next_free_slot
        self._queue[current_slot] = item

        self._next_free_slot = self.calculate_next_free_slot(current_slot)
        return current_slot


queue = Queue(4)
print(queue.enqueue("ABS"))
print(queue.enqueue("AAA"))
print(queue.enqueue("BBB"))
print(queue.enqueue("ABS"))
print(queue.enqueue("ABS"))
