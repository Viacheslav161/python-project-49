import prompt

ROUNDS = 3

def run_game(game):
    """
    Запускает игру, используя логику, определенную в модуле game.

    Args:
        game: Модуль, содержащий DESCRIPTION и generate_question_and_answer().
    """
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.DESCRIPTION)  # Выводим описание игры

    for _ in range(ROUNDS):
        question, correct_answer = game.generate_question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer == str(correct_answer):  # Преобразуем к строке для сравнения
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
