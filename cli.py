import prompt

def welcome_user():
    """Приветствует пользователя и спрашивает его имя."""
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
