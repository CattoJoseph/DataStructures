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

    def getLengthOfList(self):
        '''Method that returns the length of the list'''
        current = self.head
        totalNodes = 0
        while current.next != None:
            totalNodes +=1
            current = current.next 
        return totalNodes

    def display(self):
        '''Displays the contents of the linked list'''
        listOfElements = []
        current = self.head
        while current.next !=None:
            current = current.next
            listOfElements.append(current.data)
        print (listOfElements)

    def extractor(self):
        '''Removes an item from the list given its index'''
        index = int(input('Enter the index of the item to remove: '))
        #check if the index passed is within the range
        if index >= self.getLengthOfList() or index <0:
            return None
        #if the item to be removed is the head node
        elif index == 0:
            self.head = self.head.next
        else:
            #starting from index 0 interate to the given index
            i=0
            current_node = self.head
            while i < index:
                previous = current_node
                current_node = current_node.next
                i+=1
            #update the pointers to remove the node at the index
            previous.next = current_node.next
            current_node.next = None



myList = LinkedList()
myList.appender(9)
myList.appender(5)
myList.appender(8)
myList.display()
print(myList.getLengthOfList())
myList.extractor()
myList.display()
print(myList.getLengthOfList())