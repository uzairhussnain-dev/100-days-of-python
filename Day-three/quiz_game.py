questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["A. Lahore", "B. Islamabad", "C. Karachi", "D. Quetta"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. Java", "C. JavaScript", "D. C++"],
        "answer": "C"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
        "answer": "C"
    }
]

score = 0

print("🎮 Welcome to the Quiz Game!\n")

for q in questions:
    print(q["question"])
    
    for option in q["options"]:
        print(option)
    
    user_answer = input("Enter your answer (A/B/C/D): ").upper()
    
    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer was {q['answer']}\n")

print(f"🏁 Final Score: {score}/{len(questions)}")