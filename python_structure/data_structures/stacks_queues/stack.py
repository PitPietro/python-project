"""
The stack is a LIFO (Last In, First Out) data structure
Behaves like a list but it is allowed to add or remove only the last item.
- push: add a element
- pop: remove a element
"""


class Stack:
    def __init__(self):
        """
        The 'items' list store data
        """
        self.items = []

    def is_empty(self):
        """
        :return: if the list is empty or not
        """
        return self.items == []

    def push(self, item):
        """
        :param item: element that will be added to the list
        :return: append the parameter to the list
        """
        self.items.append(item)

    def pop(self):
        """
        :return: last item in the stack and remove it
        """
        return self.items.pop()

    def peek(self):
        """
        :return: last item in the stack without removing it
        """
        last_e = len(self.items)-1

    def size(self):
        """
        :return: length of the list
        """
        return len(self.items)

