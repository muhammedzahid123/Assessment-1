#Exercise 6 Brute Force Attack

# Password settings
CORRECT_PASSWORD = "12345"
MAX_ATTEMPTS = 5

# Initialize attempt counter
attempts = 0

# Allow user to enter the password up to the maximum number of attempts
while attempts < MAX_ATTEMPTS:
    user_input = input("Enter the password: ")

    if user_input == CORRECT_PASSWORD:
        print("Access granted. Welcome!")
        break
    else:
        attempts += 1
        remaining_attempts = MAX_ATTEMPTS - attempts

        if remaining_attempts > 0:
            print(f"Wrong password. You have {remaining_attempts} attempt(s) left.")
        else:
            print("Wrong password. You are out of attempts.")
            #Exercise 7 some Counting

# Count up from 0 to 50
print("Counting from 0 to 50:")
for i in range(51):
    print(i)
print("-" * 40)

# Count down from 50 to 0
print("Counting from 50 to 0:")
for i in range(50, -1, -1):
    print(i)
print("-" * 40)

# Count up from 30 to 50
print("Counting from 30 to 50:")
for i in range(30, 51):
    print(i)
print("-" * 40)

# Count down from 50 to 10, steps of 2
print("Counting from 50 to 10 by 2s:")
for i in range(50, 9, -2):
    print(i)
print("-" * 40)

# Count up from 100 to 200, steps of 5
print("Counting from 100 to 200 by 5s:")
for i in range(100, 201, 5):
    print(i)
print("-" * 40)
#Exercise 8 Simple Search 

# List of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Prompt the user to enter a name to search
search_term = input("Enter a name to search: ")

# Check if the name is in the list
if search_term in names:
    print(f"{search_term} is in the list.")
else:
    print(f"{search_term} is not in the list.")
    #Exercise 9 Hello

# Define a function to print a greeting
def hello():
    print("Hello")

# Main function to execute program logic
def main():
    hello()  # Call the hello function

# Entry point of the script
if 'name' == "main":
    main()
    #Exercise 10 Is it even?

def check_even_or_odd(number):
    # Check if the number is even or odd
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

def main():
    # Get a number from the user
    try:
        user_input = int(input("Enter a number: "))
        print(check_even_or_odd(user_input))
    except ValueError:
        print("Invalid input. Please enter an integer.")

if 'name'== "main":
    main()