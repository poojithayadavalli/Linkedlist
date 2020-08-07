"""
Given two linked list of equal sizes with n nodes, the task is to create new linked list using those linked lists 

where at every step, the maximum of the two elements from both the linked lists is chosen and the other is skipped.

Input:
First line indicates size of linkedlists n
Nextline contains nodes of 1st linkedlist
Nextline contains nodes of second linkedlist

Output:
print the linked list obtained from max nodes at each index

Examples:

Input:
4
5->2->3->8
1->7->4->5

Output:
5->7->4->8

Input:
4
2->8->9->3
5->3->6->4

Output: 
5->8->9->4

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
        while tmp.next is not None: 
            print(tmp.data,end="->") 
            tmp = tmp.next
        print(tmp.data)

n=int(input())
arr1=list(map(int,input().split("->")))
arr2=list(map(int,input().split("->")))
llist=LinkedList()
for i in range(n-1,-1,-1):
    llist.push(max(arr1[i],arr2[i]))
llist.printList()
