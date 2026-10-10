# Singly Linked List
# Medium
# Linear Linked List
# Module: ASSIGNMENT
# Ass1: Create a Singly Linear Linked List with following operations
# Create Linked List
# Traverse and print the node values
# Insert node at a specific position
# Find Middle node and print its value
# Delete node
# Reverse list
# Calculate the sum of every two consecutive node values.
# Constraints:
# Time limit: 2000 ms
# Memory limit: 256 MB

# Create
class Node:
    def _init_(self,value):
        self.data=value
        self.next=None

class SLL:
    def _init_(self):
        self.head=None

        
# Append
    def append(self, new_node):
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
