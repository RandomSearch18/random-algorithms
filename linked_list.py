class LinkedList:

    def __init__(self):
        self._list = [["Adam", 1], ["Badam", 2], ["Zadam", None]]

    def find_item_before(self, new_item):
        """Returns the index of the item that should be before the provided new item"""
        result = -1
        next_index = 0
        current_index = 0
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

    def append(self):
        pass


linked_list = LinkedList()
print(linked_list.find_item_before("Aadamn"))
print(linked_list.find_item_before("Azdamn"))
print(linked_list.find_item_before("Madamn"))
print(linked_list.find_item_before("Zzdamn"))
