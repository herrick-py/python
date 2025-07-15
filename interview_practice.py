# 1. Reverse a string
s = "python"
print("reversed string:", s[::-1])

# 2. Check if a number is prime or not
n = int(input("Enter a integer:"))
if n%2 != 0:
    print(n, "is a prime number")

else:
    print(n, "is not a prime number")

# 3. Find the factorial of a number
import math
n = int(input("Enter a number:"))
result = math.factorial(n)
print(f"The factorial of {n} is {result}")

# 4. Count vowels in a string
s = input("Enter a string:")
count = 0
s = s.lower()   # lower() helps to trasnform the given string in lowercase
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count += 1
if count == 0:
    print('No vowels found')
else:
    print("Total vowels are:", count)  

 # 5. Remove duplicates from a list
lst = [1,2,2,3,3,3,34,56,76,7,88,88]   
print("list after removing duplicates", list(set(lst))) 

# 6. Check if a string is palindrome
s = (input("Enter a string:"))
if s == s[::-1]:
    print("The given string is palindrome")
else:
    print("The given string is not palindrome") 

# 7. Sum of digits in a number
n = int(input("Enter a number:"))
result = sum(int(digit) for digit in str(n))

print("Sum of Digits:", result) 

# 8. Find the largest number in a list
lst = [21,45,67,89,23,45]
print("Largest number:", max(lst))

# 9. Swap two numbers without using a temporary variable
a = int(input("Enter value a ="))
b = int(input("Enter value b ="))
a,b = b,a
print(a,b)

# 10. Find the Fibonacci sequence upto N terms
nterms = int(input("Enter no.of.terms:"))
n1,n2 = 0,1
count = 0
if nterms < count:
    print("Please enter a positive integer")
elif nterms == count:
    print(count)
else:
    print("Fibonacci sequence:")
    while nterms > count:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

# 11. Count occurences of each character in a string

# 12. Multiplication table of a number
n = int(input("Enter a number:"))
for i in range(1,11):
    result = n * i
    print(f"{n} x {i} = {result}")

# 13. Reverse a list
my_lst = [3,4,5,6,7]
my_lst.reverse()
print("reversed list", my_lst) 

# 14. Merge Two Lists Without Duplicates
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
result = list(set(list1 + list2))
print("Merged lists", result)

# 15. Check Even or Odd Without Using %
n = int(input("Enter a number:"))
if n&1==0:
    print("Number is Even")
else:
    print("Number is Odd")    