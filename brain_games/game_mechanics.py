import prompt
from brain_games.cli import welcome_user


def answer_comparison(game):
    name = welcome_user()
    print(game.task)
    i = 0
    while i < 3:
        question, correct_answer = game.question_answer()
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
        if i == 3:
            print(f'Congratulations, {name}!')
