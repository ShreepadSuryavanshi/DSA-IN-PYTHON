#. Reverse the Array: Write a program to accept N integers into an array and 
#display the elements in reverse order without changing the original array. 
n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))
print("Elements in reverse order:")
for i in range(n-1, -1, -1):
    print(arr[i], end=" ")  
