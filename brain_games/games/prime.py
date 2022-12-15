from random import randint


task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUMBER = 100  # maximum number


def generate_question_and_get_answer():
    number = randint(1, MAX_NUMBER)
    question = f'''Question: {number}'''
    i = 0
    for n in range(2, number // 2 + 1):
        if (number % n == 0):
            i += 1
    correct_answer = is_prime(number, i)
    return question, correct_answer


def is_prime(number, i):
    if i > 0:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return correct_answer
