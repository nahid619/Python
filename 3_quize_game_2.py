# Simple Quiz Game in Python

# Questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) Berlin", "C) Madrid", "D) Rome"],
        "answer": "A"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["A) 10", "B) 12", "C) 14", "D) 15"],
        "answer": "B"
    },
    {
        "question": "Which language is primarily used for web development?",
        "options": ["A) Python", "B) Java", "C) HTML", "D) C++"],
        "answer": "C"
    },
    {
        "question": "What is the smallest planet in our solar system?",
        "options": ["A) Earth", "B) Jupiter", "C) Mars", "D) Mercury"],
        "answer": "D"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A) Gold", "B) Oxygen", "C) Iron", "D) Silver"],
        "answer": "B"
    }
]

# Variables to store the score
score = 0

# Function to run the quiz
def run_quiz():
    global score
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A, B, C, or D): ").upper()
        
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer.")
    
    # Final score
    print(f"\nQuiz complete! Your score is {score} out of {len(questions)}.")

# Start the quiz
run_quiz()
