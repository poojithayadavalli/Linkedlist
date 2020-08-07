"""
Given a sorted linked list of n nodes, delete all nodes that have duplicate numbers (all occurrences), leaving only numbers that appear once in the original list.

Input:
Firstline indicates integer n
Second line contains nodes of linked list

Output:
print the linkedlist with unique nodes

Examples:

Input :
8
23->28->28->35->49->49->53->53
Output : 
23->35

Input :
6
11->11->11->11->75->75
Output : 
No output

"""
class Node:
    def __init__(self, data):  
        self.data = data  
        self.next = None
  
class LinkedList:
    def __init__(self):  
        self.head = None
        self.d={}
    def push(self, new_data):  
        new_node = Node(new_data)
        if new_node.data in self.d:
            self.d[new_node.data]+=1
        else:
            self.d[new_node.data]=1
        new_node.next = self.head  
        self.head = new_node
    
    def deleteNode(self, key):
        temp = self.head 
        if (temp is not None): 
            if (temp.data == key):  
                self.head = temp.next
                temp = None
                return  
        while(temp is not None):
            if temp.data == key:  
                break
            prev = temp  
            temp = temp.next
        if(temp == None):  
            return
        prev.next = temp.next
        temp = None 
    def printList(self):  
        temp = self.head  
        while(temp.next):
            print(temp.data , end = '->') 
            temp = temp.next
        print(temp.data)
    def solution(self):
        for i,j in self.d.items():
            if j>1:
                for k in range(j):
                    self.deleteNode(i)

        
n=int(input())
arr=list(map(int,input().split('->')))
llist=LinkedList()
for i in range(n-1,-1,-1):
    llist.push(arr[i])
llist.solution()
llist.printList()

