# num1=20
# num2=10
# result=num1/num2
# print(result)




# try:
#     num1=20
#     num2=10
#     result=num1/num
# except NameError as e:
#     print(e)
# try:
#     num1=20
#     num2=0
#     result=num1/num2
# except:
#     print("Can't devide by zero")

# try:
#     num1=20
#     num2=1
#     result=num1/num2
# except:
#     print("Can't devide by zero")
# else:
#     print("inside the else part")


# import os
# try:
#     num1=20
#     num2=0
#     result=num1/num2
# except:
#     print("Can't devide by zero")
# else:
#     print("inside the else part")
# finally:
#     os._exit(0)         ##  at this part not working finally 
#     print("inside the finally")




# import sys
# num1=45
# num2=0
# try:
#     num3=num1/num2
# except ZeroDivisionError as e:
#     print(e.__class__)
#     print(e)




# age=int(input("Enter the age:"))
# try:
#     if (age<18):
#         raise ValueError
#     else:
#         print("you are eligible ")
# except ValueError as ve:
#     print("you can not give vote ")



# age=int(input("Enter the age:"))
# try:
#     if (age<18):
#         raise ValueError("you can not vote")
#     else:
#         print("you are eligible ")
# except ValueError as ve:
#     print(ve)

##==========================================  Customized Exception  ===========================
##################            
# class Under_age_exception(Exception):
#     pass
# class Manish:
#     age=10
#     try:
#         if (age<18):
#             raise 
#         else:
#             print("eligible")
#     except Exception as e:
#         print(e)


# class Under_age_exception(Exception):
#     pass

# class Manish:
#     age=int(input("Enter your age"))
#     try:
#         if (age<18):
#             raise  Under_age_exception("You are under age")
#         else:
#             print(" you are eligible")
#     except Under_age_exception as uae:
#         print(uae)

##=======================  7 division ErrorSeven  ======================================

# class SevenDivisonError(Exception):
#     def __init__(self):
#         print("You can't divide by Seven")
#     pass
# class Main:
#     n1=int(input("Enter 1st the number: "))
#     n2=int(input("Enter the number: "))
#     try:
#         if n2==7:
#             raise SevenDivisonError
#         else:
#             result=n1/n2
#             print(f"Dividion is result : {result}")
#     except SevenDivisonError as sde:
#         print(sde)


# try:

#   num = int("42")

# except ValueError:

#   print("Invalid conversion.")

# else:

#   print("Conversion successful.")

# finally:

#   print("Finally block executed.")

# try: 

#  raise ValueError("This is a custom exception.") 

# except Exception as e: 

#  print(type(e).__name__)

x = 5 

if x > 0: 

 print("Positive") 
elif x < 0: 

 print("Negative") 

else: 

 print("Zero")