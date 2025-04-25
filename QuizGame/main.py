from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question = i['question']
    answer = i['correct_answer']
    new_q = Question(question, answer)
    question_bank.append(new_q)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    print('\n')
    quiz_brain.ask_question()
if quiz_brain.correct_answers == quiz_brain.q_num:
    print(f'Congratulations! You completed the quiz with a perfect score of: {quiz_brain.correct_answers}/{quiz_brain.q_num}')
else:
    print(f'You completed the quiz with a score of: {quiz_brain.correct_answers}/{quiz_brain.q_num}')
