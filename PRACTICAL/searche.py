#Search an Element: Write a program to accept N integers into an array and 
#search for a given number. Display an appropriate message indicating 
#whether the number is present in the array or not and also display its 
#position.

n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))
search_num = int(input("Enter the number to search: "))
found = False
for i in range(n):
    if arr[i] == search_num:
        found = True
        position = i + 1  # Position is index + 1
        break
if found:
    print(f"Number {search_num} is present in the array at position {position}.")       
else:
    print(f"Number {search_num} is not present in the array.")