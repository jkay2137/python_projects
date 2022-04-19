
class QuizBrain():

    def __init__(self, list):
        self.question_number = 0
        self.score = 0
        self.question_list = list

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {question.text} (True/False)?: ")
        if self.check_answer(user_answer, question.answer):
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"Correct answer was: {question.answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def still_has_questions(self):
        if self.question_number > self.question_list.__len__() - 1:
            return False
        else:
            return True

    def check_answer(self, answer, correct_answer):
        return answer.lower() == correct_answer.lower()