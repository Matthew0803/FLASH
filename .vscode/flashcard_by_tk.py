import tkinter as tk
from tkinter import messagebox

# Define the quiz questions, choices, and answers
quiz = [
    {
        "question": "What is the capital of France?",
        "choices": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
        "answer": "C"
    },
    {
        "question": "Which function is used to get user input in Python?",
        "choices": ["A. get()", "B. input()", "C. gets()", "D. scan()"],
        "answer": "B"
    },
    {
        "question": "What is the largest planet in our Solar System?",
        "choices": ["A. Earth", "B. Jupiter", "C. Mars", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "choices": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "A"
    },
    {
        "question": "What is the chemical symbol for Gold?",
        "choices": ["A. Au", "B. Ag", "C. Go", "D. Gd"],
        "answer": "A"
    }
]

root = tk.Tk()
root.title("Python Quiz Game")
root.geometry("400x300")

question_label = tk.Label(root, text="Question will appear here")
question_label.pack(pady=20)

selected_option = tk.StringVar()

options = []
for option in ["A", "B", "C", "D"]:
    radio_button = tk.Radiobutton(root, text=option, variable=selected_option, value=option)
    radio_button.pack(anchor=tk.W)
    options.append(radio_button)

current_question = 0
score = 0

def next_question():
    global current_question
    if current_question < len(quiz):
        item = quiz[current_question]
        question_label.config(text=item["question"])
        for i, choice in enumerate(item["choices"]):
            options[i].config(text=choice)
        selected_option.set(None)
    else:
        messagebox.showinfo("Quiz Over", f"Your final score is {score} out of {len(quiz)}.")
        root.quit()

def check_answer():
    global current_question, score
    item = quiz[current_question]
    if selected_option.get() == item["answer"]:
        score += 1
    current_question += 1
    next_question()

next_button = tk.Button(root, text="Next", command=check_answer)
next_button.pack(pady=20)

next_question()
root.mainloop()
