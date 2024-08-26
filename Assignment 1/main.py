'''1. Age Assignments Based on the Riddle

Problem Statement: Write a program to solve this age-related riddle! Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
Anton is 21 years old.
Beth is 6 years older than Anton.
Chen is 20 years older than Beth.
Drew is as old as Chen's age plus Anton's age.
Ethan is the same age as Chen.'''

# Solution

anton_age:int = 21

beth_age:int = anton_age + 6

chenn_age:int = beth_age + 20

drew_age:int = chenn_age + anton_age

ethan_age = chenn_age

print("Anton's age: ", anton_age)

print("Beth's age: ", beth_age)

print("Chen's age: ", chenn_age)

print("Drew's age: ", drew_age)

print("Ethan's age: ", ethan_age)

'''
2.Formatted String Interpolation

Task: Given the variables name, age, and city, use f-strings to construct a sentence that describes a person using these variables.

name:str = "Alice"
age:int = 30
city:str = "New York"

'''
name:str="Alice"
age:int=30
city:str="New York"

print(f"{name} is {age} years old and lives in {city}")

'''
3. String Manipulation

Task: Given the string s, use string methods to:
Capitalize the first letter: make the first character uppercase and the rest of the string lowercase.
Convert to uppercase: change all characters in the string to uppercase.
Convert to lowercase: change all characters in the string to lowercase.
s:str = "hElLo WoRlD" 
'''

s:str="hElLo WoRlD"

print(s.capitalize()) # Outputs: Hello world

print(s.upper()) # Outputs: HELLO WORLD

print(s.lower()) # Outputs: hello world

'''
4. Substring Search

Task: Given the string s, use string methods to:
Find the index of "fox": get the starting index of the substring "fox". If "fox" is not found, it should return -1.
Count occurrences of "the": Use the string's built-in method to count how many times the substring "the" appears in the string.
s:str ="the quick brown fox jumps over the lazy dog"
'''

s:str="the quick brown fox jumps over the lazy dog"

print(s.index("fox")) # Outputs: 28

print(s.count("the")) # Outputs: 3

'''
5. String Replacement

Task: Given the string s, use string methods to:
Replace "Python" with "Java": substitute "Python" with "Java".
s:str ="I love programming in Python"
'''

s:str="I love programming in Python"

print(s.replace("Python", "Java")) # Outputs: I love programming in Java

'''
6. String Splitting and Joining

Task: Given the string s, use string methods to:
Split into a list: break the string into a list of substrings based on the delimiter ,.
Join with spaces: combine the list of substrings back into a single string, with each element separated by a space.
s:str ="apple,banana,cherry,dates"
'''

s:str="apple,banana,cherry,dates"

print(s.split(",")) # Outputs: ['apple', 'banana', 'cherry', 'dates']

print(" ".join(s.split(","))) # Outputs: apple banana cherry dates

'''
7. String Stripping and Justifying

Task: Given the string s, use string methods to:
Remove leading/trailing spaces: remove all leading and trailing whitespace characters from the string.
Left justify with '*': left justify the string within a field of width 20, using * as the fill character.
Right justify with '*': right justify the string within a field of width 20, using * as the fill character.
s:str ="   Python is fun!   "
'''
s:str="   Python is fun!   "

print(s.strip()) # Outputs: Python is fun!

print("*" + s.ljust(20) + "*") # Outputs: *   Python is fun!   *

print("*" + s.rjust(20) + "*") # Outputs: *Python is fun!   *

'''
8. Convert an integer to its binary representation

Task: Given an integer num
Obtain the binary representation of num
num:int = 45
'''

num:int = 45

print(f"Binary representation : {bin(num)}") # Outputs: Binary representation : 0b101101

'''
9. Calculate Powers of Numbers.

Task: Given two integers base and exponent
Compute base raised to the power of exponent.
base:int = 3
exponent:int = 4
'''

base:int = 3

exponent:int = 4

print(f"{base}^{exponent} = {base**exponent}") # Outputs: 3^4 = 81

'''
10. Round floating-point numbers

Task: Given a floating-point number value
Round value to the nearest integer.
Round value to two decimal places.
value:float = 12.34567
Expected Output:
Rounded to nearest integer: 12
Rounded to two decimal places: 12.35
'''

value:float = 12.34567

rounded_integer:int = round(value)

rounded_decimal:float = round(value, 2)

print(f"Rounded to nearest integer: {rounded_integer}")

print(f"Rounded to two decimal places: {rounded_decimal}") # Outputs: Rounded to nearest integer: 12, Rounded to two decimal places: 12.35



