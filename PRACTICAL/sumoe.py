#1. Calculate Array Sum: Write a program to accept N integers into an array 
#and calculate and display the sum of all the elements. 

n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))
sum = 0
for i in arr:
    sum += i
print("Sum of all elements:", sum)
