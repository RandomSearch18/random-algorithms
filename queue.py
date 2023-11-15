class Queue:
    EMPTY_SLOT = None

    def __init__(self, length: int):
        self._length = length
        self._queue = [self.EMPTY_SLOT] * length
        self._next_free_slot = 0
        self._start = 0
        self._end = 0

    def is_full(self):
        if self._start == 0 and self._end == self._length + 1:
            # The queue is full with no wrap-around
            print("end", self._end, self._queue)
            return True

        if self._end == self._start - 1:
            # The queue has wrapped around and the end pointer is just before the start
            return True

        # At least 1 free space should be available
        return False

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
        if self.is_full():
            raise RuntimeError(f"Queue is full! (Max {self._length} items)")

        current_slot = self._next_free_slot
        self._queue[current_slot] = item
        self._end += 1

        self._next_free_slot = self.calculate_next_free_slot(current_slot)
        return current_slot

    def dequeue(self):
        first_item = self._queue[self._start]
        self._start += 1
        return first_item


queue = Queue(4)
print(queue.enqueue("ABS"))
print(queue.enqueue("AAA"))
print(queue.enqueue("BBB"))
print(queue.enqueue("ABS"))
print(queue.dequeue())
print(queue.enqueue("ABS"))
