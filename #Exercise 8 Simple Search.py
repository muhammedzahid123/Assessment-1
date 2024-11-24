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