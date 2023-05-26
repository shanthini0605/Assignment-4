# Write a Python program to triple all numbers of a given list of integers. Use Python map

lst = (1,2,3,4,5,6,7,8,9,10)
print("Original List: ",lst)
result = map(lambda x : x + x + x, lst)
print("Triple of said list numbers: ")
print(list(result))

