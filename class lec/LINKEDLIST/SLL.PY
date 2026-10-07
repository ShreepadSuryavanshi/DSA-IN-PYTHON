# singly linear linked list
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None 


class SLL :
    def __init__(self):
        self.head = None
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node
    def print(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next

list1 = SLL()

n1= Node(10)
n2= Node(20)

list1.append(n1)
list1.append(n2)

list1.append(Node(30))
list1.append(Node(40))

list1.print()


















    # def insert_at_end(self, value):
    #     new_node = Node(value)
    #     if self.head is None:
    #         self.head = new_node
    #         return
    #     current = self.head
    #     while current.next:
    #         current = current.next
    #     current.next = new_node




    # def display(self):
    #     current = self.head
    #     while current:
    #         print(current.data, end=" -> ")
    #         current = current.next
    #     print("None")