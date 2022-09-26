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
lst.head = Node(1)  # Add the head node
second = Node(2)    # Add the second node
third = Node(3)     # Add the second node

lst.head.next = second  # link the head node to the second node
second.next = third     # link the second node to the third node

lst.printList() # Print the linked list


