from sympy import sqf_list


class QuizBrain:
    def __init__(self, q_list):
        self.q_num = 0
        self.correct_answers = 0
        self.q_list = q_list

    def check_answer(self, inp, answer):
        while True:
            if inp.lower() == answer.lower():
                return inp.lower() == answer.lower()
            elif inp.lower() == 'false' or inp.lower() == 'true':
                return False
            else:
                inp = input('Wrong input, please type \'True\' or \'False\'.')

    def still_has_questions(self):
        return self.q_num < len(self.q_list)

    def ask_question(self):
        inp = input(f'Q.{self.q_num+1} {self.q_list[self.q_num].text} (True/False)? ')
        if self.check_answer(inp, self.q_list[self.q_num].answer):
            self.correct_answers += 1
            print(f'The answer is: {self.q_list[self.q_num].answer}')
            print(f'Your current score is: {self.correct_answers}/{self.q_num+1}')
        else:
            print('Wrong answer.')
            print(f'The answer is: {self.q_list[self.q_num].answer}')
            print(f'Your current score is: {self.correct_answers}/{self.q_num+1}')
        self.q_num += 1
