import random
from brain_games import engine
import math  # Импортируем модуль math для функции gcd
import sys

DESCRIPTION = "Find the greatest common divisor of given numbers."


def generate_question_and_answer():
    """Генерирует вопрос и правильный ответ для игры."""
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f"{number1} {number2}"
    correct_answer = math.gcd(number1, number2)  # Используем math.gcd()
    return question, correct_answer


def main():
    """Запускает игру."""
    engine.run_game(this_module)




this_module = sys.modules[__name__]

if __name__ == "__main__":
    main()
