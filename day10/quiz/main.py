from question_model import Question
from data import question_data
from brain import QuizBrain

questions = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    questions.append(new_question)

quiz = QuizBrain(questions)

quiz.next_question()
