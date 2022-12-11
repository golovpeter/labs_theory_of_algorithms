import tkinter as tk

from tkinter import filedialog as fd
from model.question import Question


class MainFrame(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)

        self.open_file_flag = False

        self.top_menu = tk.Menu(root)
        self.file_menu = tk.Menu(self.top_menu, tearoff=0)

        self.file_path = ""

        self.b1 = tk.Button(text="Готово", width=10, height=2, command=self.test)

        self.radio_val = tk.StringVar()

        self.questions = []
        self.radio_button_answers = []

    def menubar(self):
        self.top_menu.add_cascade(label="Файл", menu=self.file_menu)
        self.file_menu.add_command(label="Открыть файл", command=self.__open_file_dialog)

        self.top_menu.add_command(label="Выход", command=exit)
        return self.top_menu

    def __show_questions(self):
        row = 0

        for i in range(len(self.questions)):
            text_var = tk.StringVar()
            text_var.set(self.questions[i].question)

            textEntry = tk.Entry(textvariable=text_var, font='Arial 13', state="disabled", disabledbackground="white",
                                 disabledforeground="black")
            textEntry.grid(row=row, column=0, padx=12, pady=5)

            rad_val = tk.StringVar()
            for j in range(len(self.questions[i].answers_array)):

                answer = self.questions[i].answers_array[j]

                if answer[0] == "_":
                    answer = answer[1:]

                tk.Radiobutton(text=answer, variable=rad_val, value=answer).grid(row=row + j + 1,
                                                                                 column=0, padx=6,
                                                                                 pady=5)

                self.b1.grid(row=row + j + 2, column=0, padx=50, pady=10)
                row += 3

            self.radio_button_answers.append(rad_val)

    def __open_file_dialog(self):
        self.file_path = fd.askopenfilename(
            title="Open a file",
            initialdir="/home/golovpetr/algorihms_theory/electronic_workbook")

        self.__open_db()

    # TODO: сделать обработку кривого файла
    def __open_db(self):
        if self.file_path == () or self.file_path == '':
            return

        with open(self.file_path, "r") as my_file:
            self.open_file_flag = True

            questions = []

            while True:
                line = my_file.readline()

                if line == "":
                    break

                splt = line.split(";")

                answers_array = splt[2:len(splt)]
                correct_answer = ""

                for el in answers_array:
                    if el[0] == "_":
                        correct_answer = el[1:]
                        break

                question = Question(
                    splt[0],
                    splt[1],
                    answers_array,
                    correct_answer
                )

                questions.append(question)

            self.questions = questions

        self.__show_questions()

    def render(self):
        self.grid()
