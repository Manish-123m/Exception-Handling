# ############   python IO -------------
# f = open("practical.txt", "r")
# data=f.read()
# print(data)
# print(type(data))


# # ################        Open the file in append mode to add content without overwriting
# f = open("practical.txt", "a")
# f.write("\nThis is new text added at the end of the file.")
# f.close()
# print(f)


# f=open('practical.txt','+a')
# f.write("hello jhon")
# f.close()

# f=open("practical.txt",'w')
# f.write("Hey Bro i wish you are fine")
# f.close()


# f=open("test.txt",'w')
# f.write("Hello Bro!")


# f=open("d:\\New Text Document.txt",'r')
# line=f.readline()
# print(line)

# line2=f.readline()
# print(line2)

# # Open the PDF file in binary mode and read its content
# with open(r"d:\Cincooni System Pvt_.pdf", "rb") as file:
#     binary_data = file.read()

# # Print the first 100 bytes to see the raw binary data
# print(binary_data[:100])  # Only showing first 100 bytes for brevity


# with open("d:\\Python\exception handling.py","rb")as f:
#     line=f.readline()
# print(line)


# import os
# os.remove("test.txt")

# with open("d:\\New Text Document.txt","a")as f:
#     data=f.write("manish kumar")
#     data=f.write("\nmanish kumar")
# print(data)


# with open("task.txt","w") as f:
#     data=f.write("Hello Everyone\nWe are learning python\nand python in easy language")
    
# with open("task.txt","r") as f:
#     data=f.read()
#     print(data)
 
# newdata = data.replace("python", "java")

# with open("task.txt", "w") as f:
#     f.write(newdata)



# ###########------------ For finding learning           -------------
# posi="learning" 
# with open("task.txt","r") as f:
#     data=f.read()
#     if(data.find(posi)!=-1):
#         print("yes")
#     else:
#         print("no")


# ###########----- For writing it's auto make a text file    
# with open(".practice.txt",'w') as f:
#     data=f.write("In Python, Input and Output (I/O)\n operations refer to reading data from and \nwriting data to various sources, such as files, \nthe console, or other devices. \nHere's a breakdown of different types of I/O operations and some examples for practice.")
#     print(data)
        
# ###############          -----  Reading the entire file           -------
# with open(".practice.txt",'r') as f:
#     data=f.read()
#     print(data)



# ###################---------Reading line by line----------
# with open(".practice.txt",'r') as f:
#     data=f.readline()
#     print(data)


# guests = "Alice Smith<alice@example.com>; Bob Stone<bob@example.com>; Cara Wins<cara@example.com>"

# # Split the guest string by semicolon to get individual guests
# guest_list = guests.split(';')

# # Loop through each guest and extract the name and email
# for guest in guest_list:
#     # Find the position of '<' and '>'
#     name, email = guest.split('<')
#     email = email.strip('>')  # Remove the closing '>'
    
#     # Print the result in the desired format
#     print(f"Name: {name.strip()}, Email: {email}")




# def is_even(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# # Example usage:
# print(is_even(10))  # Expected Output: "Even"
# print(is_even(11))  # Expected Output: "Odd"



# from datetime import datetime

# def convert_date_format(input_date):
#     # Parse the input date string into a datetime object
#     date_obj = datetime.strptime(input_date, "%m/%d/%Y")
#     # Format the datetime object to the desired output format
#     output_date = date_obj.strftime("%d %B %Y")
#     return output_date
# # Example usage
# input_date = "02/19/2023"
# output_date = convert_date_format(input_date)
# print(output_date)



# text = "Python is fun!"
# corrected_text = text.replace("Python", "Java")
# print(corrected_text)







# import random

# # Generate a random number between 0 and 20
# magic_number = random.randint(0, 20)

# # Start the guessing game
# while True:
#     # Prompt the user to guess the number
#     guess = int(input("Guess the magic number (between 0 and 20): "))
    
#     # Check if the guess is correct
#     if guess == magic_number:
#         print("Congratulations! You've guessed the magic number.")
#         break  # Exit the while loop if the guess is correct
#     else:
#         print("Wrong guess. Try again!")






# import random

# # Generate a random number between 0 and 20
# magic_number = random.randint(0, 20)

# # Start the guessing game
# while True:
#     try:
#         # Prompt the user to guess the number
#         guess = int(input("Guess the magic number (between 0 and 20): "))
        
#         # Check if the guess is correct
#         if guess == magic_number:
#             print("Congratulations! You've guessed the magic number.")
#             break  # Exit the while loop if the guess is correct
#         else:
#             print("Wrong guess. Try again!")
    
#     except ValueError:
#         # Handle the case when the user doesn't enter a valid number
#         print("Invalid input. Please enter a whole number between 0 and 20.")



############ Use a while loop to generate and print the first 100 odd numbers. 
############ Also, print the sum of the first 100 odd numbers.
# try:
#     # Initialize variables
#     count = 0  # To count how many odd numbers we've printed
#     odd_number = 1  # The first odd number
#     total_sum = 0  # To store the sum of the odd numbers
#     # Use a while loop to print the first 100 odd numbers
#     while count < 100:
#         print(odd_number)
#         total_sum += odd_number  # Add the odd number to the total sum
#         odd_number += 2  # Move to the next odd number
#         count += 1  # Increment the counter
#     # Print the total sum of the first 100 odd numbers
#     print(f"The sum of the first 100 odd numbers is: {total_sum}")
# except Exception as e:
#     print(f"An error occurred: {e}")





