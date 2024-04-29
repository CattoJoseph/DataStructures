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
            print("This input was invalid")
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

    def searcher(self, index):
        '''Allows the position of an item in the list to be searched for'''
        if index >= self.getLengthOfList():
            print("Error! Given index is out of range")
            return None
        current_index = 0
        current = self.head
        while True:
            current = current.next
            if current_index == index:
                return current.data
            


#"Object of type 'LinkedList' has no len()"
#could use the method getlengthoglist in the for loop but the method now doesn't work
#no errors appear but it just doesn't print the number of items (length)

myList = LinkedList()
myList.appender(33)
myList.appender(43)
myList.appender(44)
myList.appender(22)
myList.appender(56)
myList.display()
print(myList.getLengthOfList())
print(myList.searcher(0))
#print(myList[2])
#print(myList.getLengthOfList())
#myList.extractor()
#myList.display()
#print(myList.getLengthOfList())
