"""
The queue is a FIFO (First In, First Out) data structure
- enqueue: add a element
- dequeue: remove a element
"""


class Queue:
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

    def enqueue(self, item):
        """
        :param item: element that will be added to the list
        :return: insert the parameter into the list at index 0
        """
        self.items.insert(0, item)

    def dequeue(self):
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
