"""
Given a circular linkedlist with n nodes.The task is two split the circular linkedlist into two halves.That is two equal length singly linkedlists.

Note: The circular linked list must contain even number of nodes

Input:
Firstline indicates integer n
Secondline consists of nodes of circular linkedlists

Output:
print the two singly linked lists formed after splitting

Example:
Input:
4
10 12 13 17

Output:
10 12
13 17

Explanation:
The linkedlist 10 12 13 17 can be split into two halves as 10 12  an 13 17

Input:
2
1 2

Output:
1
2
"""
class Node:
    def __init__(self, data): 
        self.data = data 
        self.next = None

class CircularLinkedList:
    def __init__(self): 
        self.head = None
    def push(self, data): 
        ptr1 = Node(data) 
        temp = self.head 
          
        ptr1.next = self.head 
        if self.head is not None: 
            while(temp.next != self.head): 
                temp = temp.next 
            temp.next = ptr1 
  
        else: 
            ptr1.next = ptr1
  
        self.head = ptr1
    def printList(self): 
        temp = self.head 
        if self.head is not None: 
            while(True): 
                print(temp.data,end=" ") 
                temp = temp.next
                if (temp == self.head): 
                    break
            print()
    def splitList(self, head1, head2): 
        slow_ptr = self.head  
        fast_ptr = self.head 
      
        if self.head is None: 
            return 
        while(fast_ptr.next != self.head and 
            fast_ptr.next.next != self.head ): 
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        if fast_ptr.next.next == self.head: 
            fast_ptr = fast_ptr.next 
        head1.head = self.head
        if self.head.next != self.head: 
            head2.head = slow_ptr.next
        fast_ptr.next = slow_ptr.next
        slow_ptr.next = self.head
head = CircularLinkedList()  
head1 = CircularLinkedList() 
head2 = CircularLinkedList()
n=int(input())
llist=list(map(int,input().split()))
llist=llist[::-1]
for i in llist:
    head.push(i)
head.splitList(head1 , head2)
head1.printList()
head2.printList()
