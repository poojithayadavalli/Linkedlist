"""
Given a Linked List with n nodes. Write a function that moves the last element to the front in a given Singly Linked List. 

For example, if the given Linked List is 1->2->3->4->5, then the function should change the list to 5->1->2->3->4

Input:
Firstline indicates integer n
Secondline indicates the nodes of linkedlist

Output:
print the linkedlist after moving last node to first node

Example:

Input:
6
2 4 8 10 11 5

Output:
5 2 4 8 10 11 

Explantion:
The last node 5 is moved to front

Input:
5
1 2 3 4 5

Output:
5 1 2 3 4 

"""
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
    def __init__(self): 
        self.head = None

    def push(self, data): 
        new_node = Node(data) 
        new_node.next = self.head 
        self.head = new_node

    def printList(self): 
        tmp = self.head 
        while tmp is not None: 
            print(tmp.data,end=" ") 
            tmp = tmp.next
    
    def moveToFront(self): 
        tmp = self.head 
        sec_last = None 
        if not tmp or not tmp.next:  
            return
 
        while tmp and tmp.next : 
            sec_last = tmp 
            tmp = tmp.next
        sec_last.next = None 
        tmp.next = self.head 
        self.head = tmp 
n=int(input())
arr=list(map(int,input().split()))
llist=LinkedList()
for i in range(n-1,-1,-1):
    llist.push(arr[i])
llist.moveToFront()
llist.printList()
