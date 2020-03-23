from python_structure.data_structures.linked_list.node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, data):
        """
        Add a Node to the Linked List
        :param data:
        :return:
        """
        if not self.head:
            self.head = Node(data)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        """
        Print all the Nodes in the list
        :return: string in the built-in 'print()' method
        """
        node = self.head
        while node is not None:
            print(node.data, " ")
            node = node.next
        print("\n")

    def return_list(self):
        """
        Save all the Nodes of the linked list to a list and return it
        :return: Nodes' list
        """
        result = []
        node = self.head
        while node is not None:
            result.append(node.data)
            node = node.next
        return result

    def search(self, target):
        """
        Search 'target' in the linked list.
        :param target:
        :return:
        """
        current = self.head
        while current is not None:
            if current.data == target:
                print("'{}' found!".format(target))
                return True
            else:
                current = current.next
        print("'{}' NOT found.".format(target))
        return False
