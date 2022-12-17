from random import randint, choice


TASK = 'What is the result of the expression?'
MAX_NUMBER = 10  # maximum number


def generate_question_and_answer():
    number1 = randint(1, MAX_NUMBER)
    number2 = randint(1, MAX_NUMBER)
    operator = choice(['+', '-', '*'])
    question = f'{number1} {operator} {number2}'
    correct_answer = calculate(number1, number2, operator)
    return question, str(correct_answer)


def calculate(number1, number2, operator):
    if operator == '+':
        correct_answer = number1 + number2
    elif operator == '-':
        correct_answer = number1 - number2
    elif operator == '*':
        correct_answer = number1 * number2
    return correct_answer
