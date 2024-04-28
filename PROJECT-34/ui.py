THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text='Score: 0', fg='white', font=('Times New Roman', 15, 'italic'))
        self.score_label.config(bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300)
        self.canvas.grid(row=1,  column=0, columnspan=2, pady=30)

        self.question_text = self.canvas.create_text(150,125,width=280,text='Some Question Text', fill=THEME_COLOR, font=('Arial',20,'italic'))

        right_button_image = PhotoImage(file='../python-projects/PROJECT-34/images/true.png')
        self.right_button = Button(image=right_button_image, highlightthickness=0, command=self.right_button_func)
        self.right_button.grid(row=2, column=0)

        
        wrong_button_image = PhotoImage(file='../python-projects/PROJECT-34/images/false.png')
        self.wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=self.wrong_button_func)
        self.wrong_button.grid(row=2,column=1)


        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text="You've reached end of the quiz.")
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def right_button_func(self):
        self.give_feedback(self.quiz.check_answer('True'))
        
    def wrong_button_func(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
            self.score_label.config(text=f'Score: {self.quiz.score}')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question )