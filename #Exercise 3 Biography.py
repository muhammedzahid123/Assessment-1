#Exercise 3 Biography 
# Get user details: name, hometown, and age
name = input("Enter your name: ")
hometown = input("Enter your hometown: ")
# Validate the age input to ensure it is a valid number
while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():  # Check if the input is a valid integer
        age = int(age_input)  # Convert the input to an integer
        break
    else:
        print("Invalid input. Please enter a number.")

# Store the details in a dictionary
person_info = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Display the details
print(f"Name: {person_info['name']}")
print(f"Hometown: {person_info['hometown']}")
print(f"Age: {person_info['age']}")