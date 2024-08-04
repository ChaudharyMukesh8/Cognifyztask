
#  Level 1 Task 1
def reverse_str(str1):
   rev_string = str1[::-1]
   return rev_string
str1 = input("Enter the string :")
rev = reverse_str(str1)
print (rev)





#Level 1 task 2

 # convert temperature from fahrenheit to celsius
# fahrenheit = float(input("enter the temperature :"))
# celsius = (fahrenheit - 32)*5/9
# print("%.2f Fahrenheit is : %0.2f Celsius" %(fahrenheit, celsius))

# #Convert Temperature from celsius to fahrenheit
# fahrenheit = (celsius * 9/5) + 32
# print("%.2f Celsius is : %0.2f Fahrenheit" %(celsius, fahrenheit))

# Level 1 Task 3
# Email validation

# import re
# email_conditions = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
# user_email = input("Enter your Email :")
# if re.search(email_conditions,user_email):
#         print("Valid Email")
# else:
#         print("Invalid Email")


#Level 1 Task 4
#Calculator

# def add(a,b):
#    return a + b
# def sub(a,b):
#       return a-b
# def mul(a,b):
#       return a*b
# def div(a,b):
#       return a/b
# def mod(a,b):
#       return a%b
# print("---------Simple calculator--------------")
# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the second number:"))
# print("Press 1 for Addition \n Press 2 for Subtraction \n Press 3 for Multiplication \n Press 4 for Division")
# option = int (input("Enter your choice from 1-4:"))
# if option == 1:
#   print("Sum of two number is ",add(num1,num2))
# elif option == 2:
#   print("Subtraction  of two number is",sub(num1,num2))
# elif option == 3:
#   print("Multiplication of two number is ",mul(num1,num2))
# elif option == 4:
#   print( "Division of two number is ",div(num1,num2))
# else:
#     print("Invalid input")



# Level 1 Task 5
# String is Palindrome or not

# def isPalindrome(str1):
#    if (str1 == str1[::-1]):
#        return "String is palindrome"
#    else: 
#        return "String is not palindrome"

# str1 = input("Enter the string:")
# print(isPalindrome(str1))
    

