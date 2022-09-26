class Node:
    def __init__(self,data):    # Initialise the node
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):    # Print the linked list
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

lst = LinkedList()
lst.head = Node(1)
second = Node(2)
third = Node(3)

lst.head.next = second
second.next = third

lst.printList() 


