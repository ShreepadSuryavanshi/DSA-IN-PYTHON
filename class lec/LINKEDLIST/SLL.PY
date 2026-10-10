# singly linear linked list
# class Node:
#     def __init__(self, value):
#         self.data = value
#         self.next = None 


# class SLL :
#     def __init__(self):
#         self.head = None
#     def append(self, new_node):
#         if self.head is None:
#             self.head = new_node
#         else:
#             temp=self.head
#             while(temp.next):
#                 temp=temp.next
#             temp.next = new_node

#     def insert(self,new_node, pos):
#         if pos ==1:
#             new_node.next = self.head
#             self.head = new_node    
#         else:
#             p=1
#             while(p!=pos-1):
#                 temp= temp.next
#                 p+=1
#             new_node.next = temp.next
#             temp.next = new_node

            


    
 
#     def print(self):
#         temp=self.head
#         while(temp):
#             print(temp.data,end=" ")
#             temp=temp.next

# list1 = SLL()

# n1= Node(10)
# n2= Node(20)

# list1.append(n1)
# list1.append(n2)

# list1.append(Node(30))
# list1.append(Node(40))

# #list1.print()
# list1.insert(Node(5),1)
# list1.insert(Node(15),2)
# list1.print()
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            p = 1

            while p < pos - 1 and temp is not None:
                temp = temp.next
                p += 1

            if temp is None:
                print("Invalid position")
                return

            new_node.next = temp.next
            temp.next = new_node


    def delete(self, value ):
        temp = self.head
        if temp is not None and temp.data == value:
            self.head = temp.next
            return
        while temp is not None and temp.data != value:
            prev = temp
            temp = temp.next
        if temp is None:
            print("Value not found")
            return
        prev.next = temp.next

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


list1 = SLL()

n1 = Node(10)
n2 = Node(20)

list1.append(n1)
list1.append(n2)
list1.append(Node(30))
list1.append(Node(40))

list1.insert(Node(5), 1)
list1.insert(Node(15), 2)

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