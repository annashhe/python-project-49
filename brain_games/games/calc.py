from random import randint, choice


task = 'What is the result of the expression?'
MAX_NUMBER = 10 #maximum number


def generate_question_and_get_answer():
    number1 = randint(1, MAX_NUMBER)
    number2 = randint(1, MAX_NUMBER)
    operator = choice(['+', '-', '*'])
    question = f'''Question: {number1} {operator} {number2}'''
    if operator == '+':
        correct_answer = number1 + number2
    elif operator == '-':
        correct_answer = number1 - number2
    elif operator == '*':
        correct_answer = number1 * number2
    return question, str(correct_answer)
