class Node:
    def __init__(self, data=None):
        '''Node class constructor method'''
        self.data = data #data point to be stored
        self.next = None

class LinkedList:
    def __init__(self):
        '''LinkedList class constructor'''
        self.head = Node() #head node with no data
    
    def appender(self,data):
        '''add a new node item to th elinked list'''
        new_node = Node()
        current = self.head
        #iterate over existing list
        while current.next != None:
            #traverse through the list
            current = current.next
        current.next = new_node #make the next node the new node