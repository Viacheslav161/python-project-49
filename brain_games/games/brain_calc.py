import random
import operator

DESCRIPTION = "What is the result of the expression?"

def generate_question_and_answer():
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)
    operations = ["+", "-", "*"]
    operation = random.choice(operations)
    question = f"{number1} {operation} {number2}"
    
    operations_dict = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    
    correct_answer = operations_dict[operation](number1, number2)
    return question, correct_answer
