class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.questions_list)
    
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q. {self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(ans, current_question.answer)
    
    def check_answer(self, u_ans, c_ans):
        
        if u_ans.lower() == c_ans.lower():
            print("You got it right!")
            self.score += 1
            print(f" Your current score is : ")
        else:
            print("That's wrong. ")
        print(f"The correct answer was: {c_ans}")
        print(f" Your current score is {self.score}/{self.question_number}")
        

    
