from random import randint


task = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_answer():
    number = randint(1, 100)
    question = f"Question: {number}"
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer