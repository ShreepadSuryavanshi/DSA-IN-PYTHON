#2. Find the smallest and Largest Element: Write a program to accept N 
#integers into an array and find and display the largest element, second largest 
#element, smallest element, second smallest element present in the array. 

n = int(input("Enter the number of elements: "))
arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))
print("elements:", arr)
min = arr[0]
max = arr[0]
smin = arr[0]
smax = arr[0]
for num in arr:
    if num<min:
        smin=min # store the previous minimum value in smin
        min=num 
    if num> max:
        smax = max
        max = num
print("Largest element:", max)
print("Second largest element:", smax)
print("Smallest element:", min)
print("Second smallest element:", smin)
