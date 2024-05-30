import streamlit as st
import os

# Define questions, choices, and correct answers
questions = [
    "What should young ones prioritize when making decisions about their future after high school?",
    "According to Matthew 6:32-33, what will happen if young ones seek first the Kingdom and righteousness?",
    "What is the purpose of relating Jehovah's praiseworthy deeds to the next generation, as mentioned in Psalms 78:4-7?",
    "How does Proverbs 23:4 warn against pursuing wealth?",
    "Which of the following is incompatible with spiritual growth and success?",
    "What should young ones consider when choosing education and future employment options?",
    "According to 1 John 2:15-17, what should young ones avoid?",
    "Why is it important not to wear oneself out to gain wealth, as mentioned in Proverbs 23:4?",
    "What can make it difficult for a person to accept the Kingdom message, according to Luke 18:24-27?",
    "What should young ones observe, as mentioned in Psalms 78:7?"
]

choices = [
    ["A) Financial security", "B) Pleasing others", "C) Seeking first the Kingdom and righteousness", "D) Pursuing material wealth"],
    ["A) They will gain financial prosperity", "B) They will please others", "C) All other things will be added to them", "D) They will find real job opportunities"],
    ["A) To gain prestige", "B) To please others", "C) To put confidence in God", "D) To pursue material wealth"],
    ["A) By emphasizing the importance of financial security", "B) By encouraging practical and flexible choices", "C) By comparing wealth to an eagle that flies away", "D) By promoting material success"],
    ["A) Pursuing material wealth", "B) Setting short-term goals", "C) Please others", "D) Seeking first the Kingdom"],
    ["A) Real job opportunities in the chosen field", "B) Pleasing their parents", "C) Pursuing material wealth", "D) Setting long-term spiritual goals"],
    ["A) Seeking first the Kingdom", "B) Pursuing material wealth", "C) Pleasing others", "D) Setting spiritual goals"],
    ["A) Wealth can sprout wings and fly away", "B) Wealth leads to spiritual growth", "C) Wealth pleases others", "D) Wealth ensures real job opportunities"],
    ["A) Pursuing material wealth", "B) Setting spiritual goals", "C) Pleasing others", "D) Seeking first the Kingdom"],
    ["A) God's commandments", "B) Material wealth", "C) Real job opportunities", "D) Their own desires"]
]

correct_answers = ["C", "C", "C", "C", "A", "A", "B", "A", "A", "A"]

# Get the current working directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the video file in the repository
# video_file = os.path.join(current_dir, r"C:\Users\dmpta\OneDrive\Documents\DISC-MAIN\Education\Git\Git Kid JW Exam decide\Decide.mp4")
video_file = os.path.join(current_dir, "Decide.mp4")

# Display the video
st.video(video_file) 

# Display questions and collect answers
answers = []
for i, question in enumerate(questions):
    st.write(f"**{i+1}. {question}**")
    user_answer = st.radio("", choices[i], key=f"{question}_answer")
    answers.append(user_answer.split(")")[0])

# Calculate grade
if st.button("Submit"):
    grade = sum([1 if a == c else 0 for a, c in zip(answers, correct_answers)])
    total_questions = len(questions)
    percentage = (grade / total_questions) * 100

    # Display grade
    st.write(f"## Your Grade: {grade}/{total_questions} ({percentage:.2f}%)")
