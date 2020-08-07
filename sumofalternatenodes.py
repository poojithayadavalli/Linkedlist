"""

Given a linked list with n nodes, the task is to print the sum of the alternate nodes of the linked list.

Examples:

Input :
8
1 8 3 10 17 22 29 42

Output : 
50
Explanation:The alternate nodes are 1 -> 3 -> 17 -> 29

Input : 
5
10 17 33 38 73

Output :
116
Alternate nodes : 10 -> 33 -> 73
"""
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
def linkedlist(arr,n):
    head=temp=Node(arr[0])
    for i in range(1,n):
        temp.next=Node(arr[i])
        temp=temp.next
    return head
def alternate(head):
    count=0
    sum=0
    while head:
        if count%2==0:
            sum+=head.val
        count+=1
        head=head.next
    return sum
n=int(input())
arr=list(map(int,input().split()))
head=linkedlist(arr,n)
print(alternate(head))
