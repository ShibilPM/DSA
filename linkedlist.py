#Creating Linked List Class
class Node:
    '''
    Specific class for creating new node
    '''
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    '''
    Linked list operations
    '''

    #Constructor
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    #Adding value at the end
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    #Deleting the value fropm the end
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value  

    #Adding the valte at start
    def prepend(self, value):
        new_node = Node(value)
        temp = self.head
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.head.next = temp
        self.length += 1
        return True
    
    #Deleting the first value
    def pop_first(self):
        temp = self.head
        if self.length == 0:
            return None
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    #Get the value of n th index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    #Set the value of n th index
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    #Insert value in the n th index
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length -1:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    #Remove value from the n th index
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index -1)
        temp = pre.next
        pre.next = temp.next  
        temp.next = None
        self.length -= 1
        return temp
    
    #Reverse the linked list
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
                      

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next



        
    