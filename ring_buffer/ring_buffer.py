from doubly_linked_list import DoublyLinkedList
class RingBuffer:
    def __init__(self, capacity):
    #     self.capacity = capacity
    #     self.replace_location = None
    #     self.storage = DoublyLinkedList()
        

    # def append(self, item):
    #     # if storage length is less than capacity add item to tail
    #     # replace location is tail
    #     if self.storage.length < self.capacity:
    #         self.storage.add_to_tail(item)
    #         self.replace_location = self.storage.tail
    #     # else
    #         # if replace location is storage tail 
    #         # replace location is storage head
    #     else:
    #         if self.replace_location is self.storage.tail:
    #             self.replace_location = self.storage.head
            
    #         # else replace location is replace loaction.next
    #         else:
    #             self.replace_location = self.replace_location.next
    #         self.replace_location.value = item

    # def get(self):
    #     # add function to 
    #     return self.storage.get_all()

        self.capacity = capacity
        self.storage = []
        self.cur = 0
        

    def append(self,item):
        # if length of storage is less than capacity
        # append item and add 1 to the current spot to where the next element will be
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            # 0 to 1... 1 to 2... 2 to 3...etc
            self.cur +=1
        else:
            # if current number is equal to  capacity if capacity is 5 
            # current item is 4 which means storage len is 5 so it comes into else statement
            # at 4 it will skip this if and add the item to storage[4] making it the fifth element
            # after that the current will go up 1 to 5 so next time around it will
            # hit this if resetting the current back to 0 and then adding item as the 0 element
            if self.cur == self.capacity:
                self.cur = 0

            self.storage[self.cur] = item
            self.cur +=1
            

    def get(self):
        return self.storage

