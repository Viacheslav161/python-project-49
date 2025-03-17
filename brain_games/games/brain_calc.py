import prompt
import random
import operator


def calculate(number1, number2, operation):
    """Вычисляет результат выражения."""
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    return operations[operation](number1, number2)


def main():
    """Основная функция игры."""
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    correct_answers_count = 0
    while correct_answers_count < 3:
        number1 = random.randint(1, 20)
        number2 = random.randint(1, 20)
        operations = ["+", "-", "*"]
        operation = random.choice(operations)
        question = f"{number1} {operation} {number2}"
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a number.")
            return  # Завершаем игру при неправильном вводе

        correct_answer = calculate(number1, number2, operation)

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
