from math import gcd
from random import randint


task = 'Find the greatest common divisor of given numbers.'


def question_answer():
    number1 = randint(1, 30)
    number2 = randint(1, 30)
    question = f"Question: {number1} {number2}"
    correct_answer = gcd(number1, number2)
    return question, str(correct_answer)
