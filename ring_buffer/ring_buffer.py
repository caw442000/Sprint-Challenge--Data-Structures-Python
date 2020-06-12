from doubly_linked_list import DoublyLinkedList
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.replace_location = None
        self.storage = DoublyLinkedList()
        

    def append(self, item):
        # if storage length is less than capacity add item to tail
        # replace location is tail
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.replace_location = self.storage.tail
        # else
            # if replace location is storage tail 
            # replace location is storage head
        else:
            if self.replace_location is self.storage.tail:
                self.replace_location = self.storage.head
            
            # else replace location is replace loaction.next
            else:
                self.replace_location = self.replace_location.next
            self.replace_location.value = item




    def get(self):
        # add function to 
        return self.storage.get_all()