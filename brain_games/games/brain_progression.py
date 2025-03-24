import random

DESCRIPTION = "What number is missing in the progression?"

def generate_question_and_answer():
    start = random.randint(1, 10)
    step = random.randint(2, 5)
    length = random.randint(5, 10)  # Длина прогрессии от 5 до 10

    progression = [start + step * i for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'  # Скрываем элемент

    question = ' '.join(map(str, progression))
    return question, correct_answer
