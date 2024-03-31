import random

class Game:
    def __init__(self):
        self.difficulty_levels = {
            'easy': {'min': 1, 'max': 10},
            'medium': {'min': 10, 'max': 100},
            'hard': {'min': 100, 'max': 1000}
        }
        self.current_problem = None
        self.score = 0
        self.total_questions = 5
        self.questions_answered = 0

    def start(self, difficulty):
        self.difficulty = difficulty
        self.score = 0
        self.questions_answered = 0

    def generate_problem(self):
        min_val = self.difficulty_levels[self.difficulty]['min']
        max_val = self.difficulty_levels[self.difficulty]['max']
        operand1 = random.randint(min_val, max_val)
        operand2 = random.randint(min_val, max_val)
        operator = random.choice(['+', '-', '*'])
        self.current_problem = f"{operand1} {operator} {operand2}"

    def check_answer(self, user_answer):
        self.questions_answered += 1
        if eval(self.current_problem) == user_answer:
            self.score += 1
        if self.questions_answered < self.total_questions:
            self.generate_problem()

    def is_game_over(self):
        return self.questions_answered >= self.total_questions

    def get_current_problem(self):
        if not self.current_problem:
            self.generate_problem()
        return self.current_problem

    def get_score(self):
        return self.score

    def get_total_questions(self):
        return self.total_questions
