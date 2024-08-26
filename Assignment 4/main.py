'''
You are tasked with creating a Python program that serves as an interactive tool for a friend who enjoys
 exploring numbers. The program should begin by prompting the user to enter their name and then ask them for
three of their favorite numbers. After gathering this information, the program should greet the user with a 
personalized message that includes their name. The three numbers provided by the user should be stored in a 
list. The program should then check if any of the numbers are even or odd, and store this information in a
separate list of tuples, where each tuple contains the number and a string indicating whether it is "even" 
or "odd". Following this, the program should use a for loop to iterate over the list of numbers, and for 
each number, it should create a tuple containing the number and its square. These tuples should be printed 
in a creative and engaging format. Additionally, the program should calculate the sum of the three numbers 
and print the result, accompanied by an encouraging message. Finally, the program should determine if the 
sum is a prime number and notify the user with an appropriate message. The goal is to make the tool both 
enjoyable and informative, allowing the user to explore their favorite numbers in a fun and interactive way,
while also introducing some interesting logical checks.
'''

print("Have fun with the number exploration tool 😄")
print("<-------------------------------------->")

# Prompt the user to enter their name

name = input("Enter your name: ")

# Prompt the user to enter their three favorite numbers

number1 = int(input("Enter your first favorite number: "))
number2 = int(input("Enter your second favorite number: "))
number3 = int(input("Enter your third favorite number: "))

# Greet the user with a personalized message

print(f"Hello, {name}! Welcome to the number exploration tool!")

# Store the favorite numbers in a list

numbers = [number1, number2, number3]

# Check if any of the numbers are even or odd and store this information in a separate list of tuples

even_odd_numbers = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]    


print("Here are the squared numbers:")

for num, status in even_odd_numbers:
    print(f"{num}^2 = {num**2} ({status})")

# Calculate the sum of the three numbers

sum_numbers = sum(numbers)

# Print the sum and an encouraging message

print(f"\nThe sum of your favorite numbers is {sum_numbers}.")

# Determine if the sum is a prime number

is_prime = True

if sum_numbers < 2:
    is_prime = False
else:
    for i in range(2, int(sum_numbers**0.5) + 1):
        if sum_numbers % i == 0:
            is_prime = False
            break

if is_prime:
    print("The sum is a prime number!")
    print("Congratulations! You found a prime number.")

else:
    print("The sum is not a prime number.")
    print("You might like to try again with different numbers.")
    print("Good luck!")









