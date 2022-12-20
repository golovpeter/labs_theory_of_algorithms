class Question:  # Класс вопроса
    def __init__(self, question_number, question, answers_array, correct_answers):  # Конструктор вопроса
        self.question_number = question_number
        self.question = question
        self.answers_array = answers_array
        self.correct_answers = correct_answers
