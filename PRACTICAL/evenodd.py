#Count Even and Odd Numbers: Write a program to accept N integers into 
#an array and count and display the number of even and odd elements 
#present in the array. 

n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))
even_count = 0
odd_count = 0
for num in arr:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Number of even elements:", even_count)
print("Number of odd elements:", odd_count)