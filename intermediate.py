# 1. Check if Two Strings are Anagrams
str1 = input("Enter first string:")
str2 = input("Enter second string:")

str1 = str1.lower()
str2 = str2.lower()

if len(str1) == len(str2):

    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if sorted_str1 == sorted_str2:
        print(str1 + ' and ' + str2 + " are anagram")
    else:
        print(str1 + ' and ' + str2 + " are not anagram")

else:
    print(str1 + ' and ' + str2 + " are not anagram")       
            
# 2. Print all prime numbers in a range
lower = int(input("Enter minimum value:"))
upper = int(input("Enter maximum value:"))

print(f"The prime numbers between {lower} and {upper} :")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2,num):
            if(num%i) == 0:
                break
        else:
            print(num)    

# 3. Find second largest number in a list
a = [10,20,30,5,56,78,45]

a.sort(reverse=True)
print("second largest number in the list:", a[1])

# 4. Transpose of a matrix
import numpy as np
arr = np.array([[1,2,3],
                [4,5,6]])
arr1 = np.transpose(arr)
print(arr1)

# 5. Sum of all elements in a matrix
matrix = ([[1,2],
           [4,5]])
total = 0
for row in matrix:
    total += sum(row)

print('sum:', total)

# 6. Check if a matrix is symmetric
matrix = ([[1,2], [3,4]])
symmetry = True

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] != matrix[j][i]:
            symmetry = False

print("symmetric", symmetry)            


