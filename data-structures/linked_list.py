class LinkedList:

    def __init__(self):
        self._list = [["Adam", 1], ["Badam", 2], ["Zadam", None]]

    def find_item_before(self, new_item):
        """Returns the index of the item that should be before the provided new item"""
        result = -1
        next_index = 0
        current_index = 0  # First entry is at self._list[0]
        while next_index is not None:
            current_item, next_index = self._list[current_index]
            if current_item > new_item:
                # We want to return the index of the previous item
                return result

            result = current_index
            current_index = next_index

        # We didn't find anything greater than the new item,
        # so return the final item in the list
        return len(self._list) - 1

    def append(self, new_item):
        previous_item_index = self.find_item_before(new_item)
        previous_item, old_next_item = self._list[previous_item_index]
        #print("Prev entry", self._list[previous_item_index])

        new_item_index = previous_item_index + 1

        # Update the item before the new one to point to the new item
        self._list[previous_item_index][1] = new_item_index

        new_entry = [new_item, old_next_item]
        self._list.insert(new_item_index, new_entry)

        return new_item_index


linked_list = LinkedList()
print(linked_list._list)
linked_list.append("Aadamn")
print(linked_list._list)
linked_list.append("Azdamn")
print(linked_list._list)
linked_list.append("Madamn")
print(linked_list._list)
linked_list.append("Zzdamn")
print(linked_list._list)
