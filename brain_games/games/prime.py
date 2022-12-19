from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUMBER = 100


def generate_question_and_answer():
    number = randint(1, MAX_NUMBER)
    question = f'{number}'
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def is_prime(number):
    if number <= 0:
        return False
    else:
        for divisor in range(2, number // 2 + 1):
            if number % divisor == 0:
                return False
        return True
