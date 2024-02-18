from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    que_text = question['text']
    que_ans = question['answer']
    new_question = Question(que_text, que_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while not quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed the quiz.\nYour final score was: {quiz.score}/{quiz.question_number}.")
