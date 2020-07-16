import random

from data_structures.linked_list.linked_list import LinkedList
from data_structures.linked_list.node import Node
"""
A linked list is a data structure made by a sequence of elements which are connected together via nodes.
Each element contains a connection to another element in form of a pointer.
"""

if __name__ == '__main__':
    my_node = Node("Monday")
    my_node.print_node()

    my_linked_list = LinkedList()
    my_linked_list.append_node("Tuesday")
    my_linked_list.append_node("Wednesday")
    my_linked_list.print_list()
    print(my_linked_list.return_list())
    # test all the methods
    print("\n\n")
    num_list = LinkedList()
    for i in range(0, 20):
        i = random.randint(1, 30)
        num_list.append_node(i)
    # num_list.print_list()
    print(num_list.return_list())
    num_list.search(random.randint(1, 30))
