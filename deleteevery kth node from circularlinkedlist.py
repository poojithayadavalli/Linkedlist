"""
Delete every kth Node from a circular linked list containing n nodes until only one node is left. Also print the intermediate lists.

Input:
Firstline contains integer n and integer k
Secondline contains nodes of linked list

Output:
Print the linkedlist after deletion

Examples:

Input : 
4 2
1->2->3->4
Output : 
2->2
Explanation: Every kth node is deleted as follows.
1->2->3->4->1
1->2->4->1
2->4->2
2->2

Input :
9 4
1->2->3->4->5->6->7->8->9
Output :
2->2

Explanation:The deletion goes as follows
1->2->3->4->5->6->7->8->9->1
1->2->3->4->6->7->8->9->1
1->2->3->4->6->7->8->1
1->2->3->6->7->8->1
2->3->6->7->8->2
2->3->6->8->2
2->3->8->2
2->3->2
2->2
"""
import math  
class Node:  
    def __init__(self, data):  
        self.data = data  
        self.next = None
 
def prList(head): 
    if (head == None): 
        return
    temp = head 
      
    print(temp.data, end = "->") 
    temp = temp.next
    while (temp != head): 
        print(temp.data, end = "->") 
        temp = temp.next
    print(head.data) 

def deleteK(head_ref, k): 
    head = head_ref
    if (head == None): 
        return
    curr = head 
    prev = None
    while True:
        if (curr.next == head and curr == head): 
            break
        for i in range(k): 
            prev = curr 
            curr = curr.next
        if (curr == head): 
            prev = head 
            while (prev.next != head): 
                prev = prev.next
            head = curr.next
            prev.next = head 
            head_ref = head 
        elif (curr.next == head) : 
            prev.next = head 
              
        else : 
            prev.next = curr.next
    prList(head)
def insertNode(head_ref, x):
    head = head_ref 
    temp = Node(x) 
    if (head == None): 
        temp.next = temp 
        head_ref = temp 
        return head_ref
    else : 
        temp1 = head 
        while (temp1.next != head): 
            temp1 = temp1.next
        temp1.next = temp 
        temp.next = head 
    return head
n,k=map(int,input().split())
clist=list(map(int,input().split('->')))
head = None
for i in range(n):
    head=insertNode(head,clist[i])

deleteK(head,k)
