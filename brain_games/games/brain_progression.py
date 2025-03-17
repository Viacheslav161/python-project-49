import random
from brain_games import engine
import sys


DESCRIPTION = "What number is missing in the progression?"


def generate_progression(start, step, length):
    """Генерирует арифметическую прогрессию."""
    return [start + i * step for i in range(length)]


def generate_question_and_answer():
    """Генерирует вопрос и правильный ответ для игры."""
    start = random.randint(1, 20)  # Начальное число
    step = random.randint(2, 5)  # Шаг прогрессии
    length = 10  # Длина прогрессии (фиксированная)
    progression = generate_progression(start, step, length)

    hidden_index = random.randint(0, length - 1)  # Индекс скрытого элемента
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."  # Заменяем элемент на ".."

    question = " ".join(map(str, progression))  # Преобразуем в строку
    return question, correct_answer


def main():
    """Запускает игру."""
    engine.run_game(this_module)




this_module = sys.modules[__name__]

if __name__ == "__main__":
    main()
