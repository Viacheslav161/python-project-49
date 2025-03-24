from brain_games.engine import run_game
from brain_games.games.brain_progression import generate_question_and_answer, DESCRIPTION

def main():
    run_game(DESCRIPTION, generate_question_and_answer)

if __name__ == "__main__":
    main()
