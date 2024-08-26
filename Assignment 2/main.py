'''
1.  Add two numbers

Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

Prompt the user to enter the first number.
Read the input and convert it to an integer.
Prompt the user to enter the second number.
Read the input and convert it to an integer.
Calculate the sum of the two numbers.
Print the total sum with an appropriate message.
'''

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

print(f"{first_number}  +  {second_number} = {first_number+second_number}")  

'''
2. Agreement Boot

Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

What's your favorite animal? cow

My favorite animal is also cow!
'''

animal:str = input("What's your favorite animal? ")

print(f"My favorite animal is also {animal}!")

'''
3. Fahrenheit to Celsius Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!

The equation you should use for converting from Fahrenheit to Celsius is the following:

degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

(Note. The .0 after the 5 and 9 matters in the line above!!!)

Here's a sample run of the program (user input is in bold italics):

Enter temperature in Fahrenheit: 76

Temperature: 76.0F = 24.444444444444443C
'''

fahrenheit:float = float(input("Enter temperature in Fahrenheit: "))

celsius:float = (fahrenheit - 32) * 5.0 / 9.0

print(f"Temperature: {fahrenheit}F = {celsius:.4f}C")

'''
4. Triangle Perimeters Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

Here's a sample run of the program (user input is in bold italics):

What is the length of side 1? 3

What is the length of side 2? 4

What is the length of side 3? 5.5

The perimeter of the triangle is 12.5
'''

side1:float = float(input("What is the length of side 1? "))

side2:float = float(input("What is the length of side 2? "))

side3:float = float(input("What is the length of side 3? "))

perimeter:float = side1 + side2 + side3 

print(f"The perimeter of the triangle is {perimeter}")

'''
5. Square Number Ask the user for a number and print its square (the product of the number times itself).

Here's a sample run of the program (user input is in bold italics):
'''

number:float = float(input("Type a number to see its square: "))

square:float = number * number

print(f"{number} squared is {square:.1f}")

'''
6. Delete a number Consider a list named numbers with the elements [1, 2, 3, 4, 5]. 
Use list method to delete the number 3?
'''

numbers: list = [1, 2, 3, 4, 5]

numbers.remove(3)

print(numbers)

'''
7. Creating a list You have two lists:

list1 with elements [1, 2, 3]
list2 with elements [4, 5, 6].
Create a program using list method to add the elements of list2 to list1.
'''

list1: list = [1, 2, 3]

list2: list = [4, 5, 6]

list1.extend(list2)

print(list1)

'''
8. Pop method You have a list named items with the elements [10, 20, 30, 40].
If you use the pop method without any arguments, what will the list look like and what value will be removed?
'''

items: list = [10, 20, 30, 40]

removed_value: int = items.pop()

print(items)

print(removed_value)

'''
9. Index Method You have a list called colors with the elements ['red', 'blue', 'green', 'yellow'].
If you use the index method to find the position of 'green', what will the index be?
'''

colors: list = ['red', 'blue', 'green', 'yellow']

index: int = colors.index('green')

print(index)

'''
10.Challenge Question
Get last element Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. 
The list is guaranteed to be non-empty, but there are no guarantees on its length.
'''

def get_last_element(lst: list):
    print(lst[-1])

   
    get_last_element(['apple', 'banana', 'cherry'])  # prints: cherry
    get_last_element(['1', '2', '3'])  # prints: 3








'''
11. Get a List Write a program which continuously asks the user to enter values which are added one by one into a list. 
When the user presses enter without typing anything, print the list. 
'''

values: list = []

while True:
    value: str = input("Enter a value: ")
    
    if value == "":
        break
    values.append(value)

print(f"Here's the list: {values}")








    





