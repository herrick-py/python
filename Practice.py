#if-else-elif
'''
age = 25
income = 50000

if age<18:
    print('You are too young to work')
elif (age>=18 and age<=25):
    if income<30000:
        print('You are eligible for a student discount')
    else:
        print('You are eligible for a regular discount')
else:
    print('You are eligible for a regular discount') 
'''

#Looping or Iterative Statements
'''
for i in range(2,6):
    print('code')
'''

#range function (start, stop, step_value)
'''
for i in range(10, 50, 5):
    print(i)
'''

#reverse order looping
'''
for i in range(100, 50, -5):
    print(i)
'''

#while loop
'''
count = 0 #start
while(count < 5): #range
    print(count)
    count+=1  #stop
'''

#jump statement
'''
for i in range(1,10):
    if (i==5):
        continue #skips the iteration and moves on to next iteration
    print(i)
'''

#break statement
'''
for i in range(1,10):
    if (i==5): 
        break #breaks the iteration and stops it
    print(i)
'''
# To break the infinite output press ctrl+c

# Nested loops
'''
n=int(input('Enter no.of rows:'))
for j in range(1,n+1):
    for i in range(1,j+1):
        print('*',end=' ')  #end is used to get output in the same line
    print() #empty print() statement automatically moves on to next line
'''
# Lists
'''
a=[1,2,3]
b=[4,5,6]
a.append(4)
a.insert(0,0)
print(a)
'''
#tuple
'''
num=("apple","Banana","strawberry","kiwi","mango")
print(num)
num+=("grapefruit",)
print(num)
'''
# Traversal
'''
num=("apple","Banana","strawberry","kiwi","mango")
for i in num:
    print(i)
'''
#Slicing
'''
a=[2,5,1,8,4]
print(a[1:4])
a[2:4]=[3,7] #replacing values in the lists
print(a)
'''

#dictionaries
'''
map={1:"one",2:"two"} # 1-> KEY and "one"-> VALUE
print(map)
print(type(map))
'''
'''
a={5:{'P':{5:"P"},6:"Q"},7:"R",'Q':"S","S":'T'}
print(a[a[a[5][6]]])
'''
#Functions
'''
def add():
    a=int(input('Enter a Number:'))
    b=int(input('Enter a Number:'))
    print(a+b)   #To display the output
add()    #calling the given function name 
'''
'''
def greet():
    name=str(input("Enter your Name:"))
    print("Good Morning", name)
greet()
'''
# OOPs
'''
no_of_wheels = 4
mileage = 20.6
no_of_airbags = 5

def moveforward():
    print("The car is moving forward")

def movebackward():
    print("The car is moving backward")   
'''
'''
class car:
    no_of_wheels = 4
    mileage = 20.9
    no_of_airbags = 5

    def moveforward(self):
           print("The car is moving forward")

    def movebackwars(self):
          print("The car is moving backword")

car1 = car()
print(car1.no_of_wheels)
print(car1.mileage)

car2 = car()
print(car2.mileage)
print(car2.no_of_airbags)

car3 = car()
car3.moveforward()
'''

class bank_account:
      customer_name = "Herrick"
      balance = 50000
      account_number = 8743658026

      def user_account(self):
            print('bank amount credentials')

      def user_account1(self):
            print('bank details')

user1 = bank_account()
print(user1.customer_name)

user2 = bank_account()
print(user2.balance)
print(user2.account_number)

user3 = bank_account()
user3.user_account