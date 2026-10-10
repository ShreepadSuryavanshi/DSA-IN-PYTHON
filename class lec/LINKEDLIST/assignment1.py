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
    def __init__(self,value):
        self.data=value
        self.next=None

# Create Linked List
class SLL:
    def __init__(self):
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

    #Traverse
    def print(self):
        temp=self.head
        while temp:
            print(temp.data, end=" -> ")
            temp=temp.next 

        print("Null")

    #Insert at specific position
    def insert(self, new_node, pos):
        if pos<1:
            print("Invalid position!")
            return
        if pos==1:
            new_node.next=self.head
            self.head=new_node
            return
        
        temp=self.head
        p=1

        #Reach node before required position
        while temp!=None and p<pos-1:
            temp=temp.next
            p+=1

        #Check whether the position is valid 
        if temp==None:
            print("Invalid Position!")
            return

        new_node.next=temp.next
        temp.next=new_node

    #Find and print middle node
    def middle(self):
        if self.head==None:
            print("List is Empty!")
            return

        slow=self.head  # it moves one step
        fast=self.head  # it moves two steps
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next

        print("Middle node: ",slow.data)

    # Delete a node
    def delete(self,value):
        temp=self.head

        if temp==None:
            print("List is empty")
            return

        # delete first node if value matches
        if temp.data==value:
            self.head=self.head.next
            return
        
        prev=temp
        temp=temp.next

        # Search a node to delete
        while temp!=None and temp.data!=value:
            prev=temp
            temp=temp.next

        if temp == None:
            print("Value is not present in the list!")
            return

        #skip the node being delete
        prev.next=temp.next



    # Reverse
    def reverse(self):
        prev=None
        temp=self.head

        while temp!=None:
            next_node=temp.next
            temp.next=prev
            prev=temp
            temp=next_node

        self.head=prev

    # Sum of two every 2 consecutive node values
    def consecutive_sum(self):
        if self.head==None or self.head.next==None:
            print("At least two nodes are required!")
            return

        temp=self.head
        while temp!=None and temp.next!=None:
            total=temp.data+temp.next.data
            print(temp.data," + ",temp.next.data," = ",total)
            temp=temp.next

l = SLL()
l.append(Node(10))
l.append(Node(20))
l.append(Node(30))
l.append(Node(40))
l.append(Node(50))
print("Original Linked List:")
l.print()
print("After inserting 25 at poition 3:")
l.insert(Node(25),3)
l.print()
l.middle()
print("After deleting 30:")
l.delete(30)
l.print()
print("Reversed Linked List:")
l.reverse()
l.print()
print("Two consecutive node sums:")
l.consecutive_sum()






# #creating a singly linked list
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# #1. create linked list
# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self,data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#         else:
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = new_node

#     #2. traverse and print
#     def print(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print("None")

#     # 3.insert at a specific position
#     def insert(self,data,pos):
#         new_node = Node(data)

#         if pos < 1:
#             print("Invalid Position")
#             return

#         if pos == 1:
#             new_node.next = self.head 
#             self.head = new_node
#             return
        
#         temp = self.head
#         for i in range(pos-2):
#             if temp is None:
#                 print("Invalid position")
#                 return
#             temp = temp.next

#         if temp is None:
#             print("Invalid position")
#             return
        
#         new_node.next = temp.next
#         temp.next = new_node

#     #4. Find middle node

#     def middle(self):
#         slow = self.head
#         fast = self.head

#         if self.head is None:
#             print("List is empty")
#             return

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#         print("Middle node:",slow.data)


#     # 5.delete node by value
#     def delete(self,key):
#         temp = self.head
    
#         if temp and temp.data == key:
#             self.head = temp.next
#             return
    
#         while temp and temp.next:
#             if temp.next.data == key:
#                 temp.next = temp.next.next 
#                 return
#             temp = temp.next

#     # 6.reverse linked list
#     def reverse(self):
#         prev = None
#         curr = self.head

#         while curr:
#             next_node = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next_node

#         self.head = prev

#     # 7.sum of every two consecutive nodes
#     def sum(self):
#         temp = self.head

#         while temp and temp.next:
#             print(temp.data + temp.next.data)
#             temp = temp.next
            
# #main 
# list = LinkedList()

# #create 
# list.append(10)
# list.append(20) 
# list.append(30)
# list.append(40)
# list.append(50)      

# print("Singly Linked List created")
# list.print()

# #insert a node at a specific position
# list.insert(24,2)
# print("After insertion:")
# list.print()

# #middle node
# list.middle()

# #delete
# list.delete(40)
# print("After deletion:")
# list.print()

# #reverse
# list.reverse()
# print("After reversing:")
# list.print()

# #sum of two consecutive nodes
# print("Sum of every two consecutive nodes:")
# list.sum()