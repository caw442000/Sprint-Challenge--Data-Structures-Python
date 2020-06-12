"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # create a new node from the value passed in
        new_node = ListNode(value)



        # if the head and tail are None
        if not self.head and not self.tail:
            # set the head and tail to the new node created
            self.head = new_node
            self.tail = new_node

        # else set the new node's next to the head
        else:
            new_node.next = self.head
            # set the head's prev to the new node
            self.head.prev = new_node
            # set the head to be the new node
            self.head = new_node

        # increment the length of the list by 1
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head:
            pop_head = self.head
            self.delete(self.head)
            return pop_head.value    
        else:
            return None

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # create a new node from the value passed in
        new_node = ListNode(value)



        # if the head and tail are None
        # empty DLL
        if not self.head and not self.tail:

            # set the head and tail to the new node created
            self.head = new_node
            self.tail = new_node

        # not empty
        else:
            # else set the prev node on the new node to the tail
            new_node.prev = self.tail

            # set the next on the tail to the new node
            self.tail.next = new_node

            # set the tail to be the new node
            self.tail = new_node

        # increment the length of the list by 1
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # if the tail is not None
        # if self.tail is not None:
            # grab tail node and assign to temp variable
            pop_tail = self.tail
            # delete tail node
            self.delete(self.tail)
            # return value of removed tail via temp variable
            return pop_tail.value
        # else:
        #     return None

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # if node is self.head it is already in the front
        if node is self.head:
            return None
        # grab the value from the node passed in
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            
            # delete the node passed in from the list
            node.delete()
            # decrement here (remove from tail decrements for the starter if statement)
            self.length -= 1
        # add node to the head of the list
        self.add_to_head(value)
            

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):

        # if node is self.tail it is already at the end
        if node is self.tail:
            return
        # grab the value from the node passed in
        value = node.value

        # delete the node passed in from the list
        self.delete(node)

        # add node to the end of the list
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # if DLL is empty, there is nothing to delete, we should return 
        if not self.head and not self.tail:
            return 

        # decrement length of the DLL
        self.length -= 1

        # if DLL has one element remove it by
        # setting head and tail pointers to None
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # if node to delete is head
        # set DLL head pointer to node.next
        # delete node connections
        elif self.head is node:
            self.head = node.next
            node.delete()

        # if node to delete is tail
        # reset DLL tail pointer 
        # delete node connections
        elif self.tail is node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
        
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # if we don't have a head, return None
        if not self.head:
            return None

        # set new variable max_value equal to the current head value
        current = self.head
        max_value = current.value

        # while head is not None
        while current:
            # if the current value is greater than the current max_value
            if current.value > max_value:
                # replace max_value with the current node's value
                max_value = current.value

            # move the current node to the next in the list and re-compare
            current = current.next

        # return maximum value in the list
        return max_value

    def get_all(self):
        DLL_contents = []
        current_node = self.head
        while current_node is not None:
            DLL_contents.append(current_node.value)
            current_node = current_node.next
        
        return DLL_contents