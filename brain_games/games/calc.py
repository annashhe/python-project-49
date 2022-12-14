from random import randint, choice


task = 'What is the result of the expression?'


def question_answer():
    number1 = randint(1, 10)
    number2 = randint(1, 10)
    operator = choice(['+', '-', '*'])
    question = f'''Question: {number1} {operator} {number2}'''
    if operator == '+':
        correct_answer = number1 + number2
    elif operator == '-':
        correct_answer = number1 - number2
    elif operator == '*':
        correct_answer = number1 * number2
    return question, str(correct_answer)
