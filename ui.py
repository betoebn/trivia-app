from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some QuestionText",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
            width=280
        )

        self.check_button_image = PhotoImage(file="./images/true.png")
        self.check_button = Button(image=self.check_button_image,
                                   highlightthickness=0,
                                   command=self.is_true)
        self.check_button.grid(column=0, row=2)

        self.wrong_button_image = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=self.wrong_button_image,
                                   highlightthickness=0,
                                   command=self.is_false)

        self.wrong_button.grid(column=1, row=2)

        self.label = Label(text=f"Score: ", bg=THEME_COLOR, font=("Arial", 18, "bold"))
        self.label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def is_true(self):
        user = "True"
        if self.quiz.question_number == 10:
            self.canvas.itemconfig(self.question_text,
                                   text=f"Game Over, your score is {self.quiz.score}/{self.quiz.question_number}")
        if self.quiz.check_answer(user):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.window.after(1000, self.get_next_question)

    def is_false(self):
        user = "False"
        if self.quiz.question_number == 10:
            self.canvas.itemconfig(self.question_text,
                                   text=f"Game Over, your score is {self.quiz.score}/{self.quiz.question_number}")
        if self.quiz.check_answer(user):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.window.after(1000, self.get_next_question)
