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
        '''add a new node item to the linked list'''
        new_node = Node(data)
        current = self.head
        #iterate over existing list
        while current.next != None:
            #traverse through the list
            current = current.next
        current.next = new_node #make the next node the new node

    def getter(self):
        '''Method that returns the length of the list'''
        current = self.head
        totalNodes = 0
        while current.next != None:
            totalNodes +=1
            current = current.next 
        print(totalNodes)

    def display(self):
        '''Displays the contents of the linked list'''
        listOfElements = []
        current = self.head
        while current.next !=None:
            current = current.next
            listOfElements.append(current.data)
        print(listOfElements)




myList = LinkedList()
myList.appender(9)
myList.appender(5)
myList.display()
myList.getter()