class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    # Using that ADT to save all the game movements.

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def append(self, item):
        node = Node(item)  # Creating the node.
        appendCheck = None
        if self.first is None:  # If the Linked List is empty, we just add the node.
            self.first = node  # The first and the last node are the same.
            self.last = node
            appendCheck = True
        else:  # If the Linked List is not empty, we go to the last node.
            self.last.next = node  # The element next to the old last node, is the new node.
            self.last = node  # Changing the information about the last node.
            appendCheck = True

        if appendCheck is True:
            self.size += 1  # Adding one to the size.

    def clear(self):
        self.first = None
        self.last = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        aux = self.first
        stringList = []

        while aux is not None:
            stringList.append(aux.data)
            aux = aux.next
        return str(stringList)