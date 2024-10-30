import streamlit as st
import random

# Define question sets
vocabulary_questions = [
    {
        "question": "What is a synonym for 'happy'?",
        "options": ["Sad", "Joyful", "Angry", "Tired"],
        "answer": "Joyful"
    },
    {
        "question": "Choose the correct word: 'He is very _____ in the morning.'",
        "options": ["tired", "awake", "sleepy", "hungry"],
        "answer": "sleepy"
    },
]

grammar_questions = [
    {
        "question": "Which one is correct: 'She have a dog' or 'She has a dog'?",
        "answer": "She has a dog"
    },
    {
        "question": "Fill in the blank: 'I _____ to the market yesterday.' (go)",
        "answer": "went"
    }
]

comprehension_questions = [
    {
        "question": "Translate this sentence to English: 'Elle mange une pomme.'",
        "answer": "She is eating an apple"
    }
]

# Helper function to ask questions
def ask_question(question_set):
    question = random.choice(question_set)
    return question

# Initialize session state for user input and chatbot mode
if "mode" not in st.session_state:
    st.session_state.mode = None
if "question" not in st.session_state:
    st.session_state.question = None
if "feedback" not in st.session_state:
    st.session_state.feedback = None

# Title and description
st.title("English Skill Chatbot")
st.write("Hello! I can help you improve your English skills. Choose a category to get started: Vocabulary, Grammar, or Comprehension.")

# User selection for the type of question
st.session_state.mode = st.selectbox("Choose a category:", ["Select", "Vocabulary", "Grammar", "Comprehension"])

# Generate a question based on the selected mode
if st.session_state.mode == "Vocabulary":
    st.session_state.question = ask_question(vocabulary_questions)
elif st.session_state.mode == "Grammar":
    st.session_state.question = ask_question(grammar_questions)
elif st.session_state.mode == "Comprehension":
    st.session_state.question = ask_question(comprehension_questions)

# Display the question and get user input
if st.session_state.mode != "Select" and st.session_state.question:
    st.write("Question:", st.session_state.question["question"])

    # For questions with options, display them
    if "options" in st.session_state.question:
        user_answer = st.radio("Choose an answer:", st.session_state.question["options"])
    else:
        user_answer = st.text_input("Your answer:")

    # Check answer and provide feedback when user submits
    if st.button("Submit Answer"):
        if user_answer.lower() == st.session_state.question["answer"].lower():
            st.session_state.feedback = "Correct! Well done."
        else:
            st.session_state.feedback = f"Oops! The correct answer is '{st.session_state.question['answer']}'. Keep practicing!"

# Display feedback
if st.session_state.feedback:
    st.write(st.session_state.feedback)
    # Reset question and feedback after showing the result
    st.session_state.question = None
    st.session_state.feedback = None

