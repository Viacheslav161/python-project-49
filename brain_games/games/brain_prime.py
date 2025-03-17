import random
from brain_games import engine
import sys


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Определяет, является ли число простым."""
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_question_and_answer():
    """Генерирует вопрос и правильный ответ для игры."""
    number = random.randint(1, 100)
    question = number
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer


def main():
    """Запускает игру."""
    engine.run_game(this_module)




this_module = sys.modules[__name__]

if __name__ == "__main__":
    main()
