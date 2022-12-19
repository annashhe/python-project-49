import prompt


ROUNDS_COUNT = 3  # number of rounds


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_RULE)
    round_count = 1
    while round_count <= ROUNDS_COUNT:
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
