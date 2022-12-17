import prompt


ROUNDS = 3  # number of rounds


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def run_game(game):
    name = welcome_user()
    print(game.TASK)
    round_count = 1
    while round_count <= ROUNDS:
        question, correct_answer = game.generate_question_and_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            round_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'."
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
