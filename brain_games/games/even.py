from random import randint


task = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_NUMBER = 100  # maximum number


def generate_question_and_get_answer():
    number = randint(1, MAX_NUMBER)
    question = f"Question: {number}"
    correct_answer = is_even(number)
    return question, correct_answer


def is_even(number):
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer
