"""
Given a linked list of n nodes.The task is to arrange the linked list in manner of alternate first and last elements.

Input:
Firstline indicates the integer n
Secondline indicates the nodes of linked list

Output:
print the linked list after rearranging

Examples:

Input : 
8
1->2->3->4->5->6->7->8
Output :
1->8->2->7->3->6->4->5

Input :
4
10->11->15->13
Output :
10->13->11->15

"""

class Node:   
    def __init__(self, data):  
        self.data = data  
        self.next = None
def arrange(head):
    temp = head
    d = []
    while (temp != None) : 
        d.append(temp.data) 
        temp = temp.next
    i = 0
    temp = head 
    while (len(d) > 0) : 
        if (i % 2 == 0) : 
            temp.data = d[0] 
            d.pop(0)
        else : 
            temp.data = d[-1]  
            d.pop()  
        i = i + 1
        temp = temp.next
          
    return head 
def push( head, data):
    new_node = Node(0) 
    new_node.data = data
    new_node.next = head
    head = new_node 
    return head 
def printList( head):
    temp = head 
    while (temp.next != None) : 
        print( temp.data,end="->") 
        temp = temp.next
    print(temp.data)

n=int(input())
arr=list(map(int,input().split("->")))
head=None
for i in range(n-1,-1,-1):
    head=push(head,arr[i])
head=arrange(head)
printList(head)
