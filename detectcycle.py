"""

Given a linked list with n nodes, check if the linked list has loop or not.

loop in a linked list is defined as a node connecting with another node from which it has a path.

Input:
Firstline indicates integer n
Next line consists of linkedlist nodes

Output:
Print if there exits a loop

Example:

Input:
5
1 2 3 4 2

Output:
Yes

"""

n=int(input())
arr=list(map(int,input()))
flag=True
for i in arr:
  if arr.count(i)>1:
    flag=False
    break
print("Yes" if flag else "No")
