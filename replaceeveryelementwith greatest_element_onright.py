"""
Given a linked list of n nodes, the task is to find the Next Greater Element for every node of the linked list.

Note: For nodes with no next greater element, store -1 in the result.

Input:
Firstline indicates the integer n
Secondline consists of nodes of linkedlist

Output:
print the next greater node of each node

Examples:

Input:
2 1 5

Output:
5 5 -1

Input:
2 7 4 3 5

Output:
7 -1 5 5 -1

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

    def solution(self):
        l=[]
        temp=self.head
        while temp and temp.next:
            temp1=temp.next
            res=temp.data
            while temp1 is not None:
                if temp1.data > res:
                    res=temp1.data
                    break
                temp1=temp1.next
            if res==temp.data:
                l.append(-1)
            else:
                l.append(res)
            temp=temp.next
        l.append(-1)
        return l
n=int(input())
arr=list(map(int,input().split()))
llist=LinkedList()
for i in range(n-1,-1,-1):
    llist.push(arr[i])
#llist.printList()
l=llist.solution()
print(*l)
