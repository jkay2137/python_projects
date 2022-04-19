
class QuizBrain():

    def __init__(self, list):
        self.question_number = 0
        self.question_list = list

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number} {question.text} (True/False)?: ")

    def still_have_questions(self):
        if self.question_number > self.question_list.__len__():
            return False
        else:
            return True
