#Exercise 4 Primitive Quiz

# Define the quiz questions and their correct answers
quiz = {
    "What is the capital of France?": "Paris",
    "What is the capital of Germany?": "Berlin",
    "What is the capital of Italy?": "Rome",
    "What is the capital of Spain?": "Madrid",
    "What is the capital of Portugal?": "Lisbon",
    "What is the capital of INDIA?": "New delhi",
    "What is the capital of the Netherlands?": "Amsterdam",
    "What is the capital of Pakistan?": "islamabad",
    "What is the capital of Bangladesh?": "dhaka",
    "What is the capital of Kerala?": "Kasaragod",
}

# Start the quiz
print("Welcome to the European Capitals Quiz!")
print("Try to answer as many questions as you can. Good luck!\n")

# Keep track of the player's score
score = 0

# Loop through the questions and get the user's answers
for question, answer in quiz.items():
    user_answer = input(question + " ").strip()
    if user_answer.lower() == answer.lower():
        print("That's correct!\n")
        score += 1
    else:
        print(f"Oops, the correct answer is {answer}.\n")

# Show the final score
print(f"Quiz complete! You scored {score} out of {len(quiz)}.")