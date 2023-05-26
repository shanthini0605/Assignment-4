# Write a Python program to square the elements of a list using map() function

def square_num(n):
    return n*n
lst = (4,8,7,9)
print("Original List: ",lst)
result = map(square_num, lst)
print("Square the elements of said list using map: ")
print(list(result))
