from math import gcd
from random import randint


TASK = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER = 30  # maximum number


def generate_question_and_answer():
    number1 = randint(1, MAX_NUMBER)
    number2 = randint(1, MAX_NUMBER)
    question = f'{number1} {number2}'
    correct_answer = gcd(number1, number2)
    return question, str(correct_answer)
