from random import randint


GAME_RULE = 'What number is missing in the progression?'
MAX_STEP = 10
LENGTH = 10  # number of numbers in progression
MAX_NUMBER = 50  # maximum number to start list with


def generate_question_and_answer():
    start_number = randint(1, MAX_NUMBER)
    step = randint(1, MAX_STEP)
    progression = generate_progression(start_number, step, LENGTH)
    missing_index = randint(0, len(progression) - 1)
    correct_answer = progression[missing_index]
    progression[missing_index] = '..'
    progression = list(map(str, progression))
    question = f'{" ".join(progression)}'
    return question, str(correct_answer)


def generate_progression(start_number, step, LENGTH):
    finish_number = start_number + step * LENGTH
    progression = list(range(start_number, finish_number, step))
    return progression
