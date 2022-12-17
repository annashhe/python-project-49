from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUMBER = 100  # maximum number


def generate_question_and_answer():
    number = randint(1, MAX_NUMBER)
    question = f'{number}'
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def is_prime(number):
    count = 0
    for n in range(2, number // 2 + 1):
        if (number % n == 0):
            count += 1
    if count == 0:
        return True
