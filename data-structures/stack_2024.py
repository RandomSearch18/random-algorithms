from typing import TypeVar, Generic

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self):
        self._data: list[T] = []

    def isEmpty(self) -> bool:
        return len(self._data) == 0

    def push(self, item: T):
        self._data.append(item)

    def pop(self) -> T:
        if self.isEmpty():
            raise IndexError("Cannot get item from an empty stack")
        return self._data.pop()

    def peek(self) -> T:
        if self.isEmpty():
            raise IndexError("Cannot get item from an empty stack")
        return self._data[-1]

    def __len__(self) -> int:
        return len(self._data)

    def __str__(self) -> str:
        return str(self._data)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Stack):
            return False
        return self._data == value._data  # type: ignore


def is_palindrome(word: str) -> bool:
    characters = Stack[str]()
    for character in word.lower():
        characters.push(character)
    reversed_characters = Stack[str]()
    while not characters.isEmpty():
        reversed_characters.push(characters.pop())
    return characters == reversed_characters


def is_palindrome_demo(word: str):
    print(f"Checked if '{word}' is a palindrome -> {is_palindrome(word)}")


is_palindrome_demo("racecar")
is_palindrome_demo("Hello world!")
is_palindrome_demo("Hannah")
is_palindrome_demo("python3.12")
