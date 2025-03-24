import random

DESCRIPTION = 'Answer "yes" if the number is even. Otherwise answer "no".'

def generate_question_and_answer():
    number = random.randint(1, 100)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return number, correct_answer
