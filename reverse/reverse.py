class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):

        # error for empty
        if node is None:
            return
        # Base case: when node.next_node is None swap rolls and return
        if node.next_node is None:
            self.head = node
            node.next_node = prev
            return

        # (if Node is 1 Next node 2 it should pass revList (2, 1))
        # need variables to hold node to pass

        rev_node = node.next_node
        # point node next node to prev which turns it around when code is hit
        node.next_node = prev
        self.reverse_list(rev_node, node)
