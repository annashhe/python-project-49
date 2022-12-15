import prompt
from brain_games.cli import welcome_user


ROUNDS = 3  # number of rounds


def answer_comparison(game):
    name = welcome_user()
    print(game.task)
    i = 0
    while i < ROUNDS:
        question, correct_answer = game.generate_question_and_get_answer()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f''''{answer}' is wrong answer ;(.
Correct answer was '{correct_answer}'.
Let's try again, {name}!''')
            break
        i += 1
        if i == ROUNDS:
            print(f'Congratulations, {name}!')
