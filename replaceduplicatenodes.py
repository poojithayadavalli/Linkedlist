"""
Given a linked list that contains some random integers from 1 to n with many duplicates. 

Replace each duplicate element that is present in the linked list with the values n+1, n+2, n+3 and so on(starting from left to right in the given linked list).

Input:
Firstline indicates the integer n
Secondline indicates the nodes of the linkedlist

Output:
print the linkedlist after replacing duplicate elements

Examples:

Input :
7
1 3 1 4 4 2 1

Output :
1 3 5 4 6 2 7

Explanation:
Replace 2nd occurrence of 1 with 5 i.e. (4+1)
        2nd occurrence of 4 with 6 i.e. (4+2)
        3rd occurrence of 1 with 7 i.e. (4+3)

Input : 
7
1 1 1 4 3 2 2
Output :
1 5 6 4 3 2 7
"""
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList:
    def __init__(self): 
        self.head = None
        self.d={}

    def push(self, data): 
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node

    def printList(self):
        tmp = self.head 
        while tmp is not None: 
            print(tmp.data,end=" ") 
            tmp = tmp.next
    
    def solution(self,n):
        temp=self.head
        while temp is not None:
            if temp.data in self.d:
                temp.data=n+1
                n=n+1
            else:
                self.d[temp.data]=1
            temp=temp.next
            
        
n=int(input())
arr=list(map(int,input().split()))
llist=LinkedList()
for i in range(n-1,-1,-1):
    llist.push(arr[i])
llist.solution(max(arr))
llist.printList()
