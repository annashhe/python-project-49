#!/usr/bin/env python3
import prompt
from random import randint, choice
from brain_games.cli import welcome_user


def main():
    answer_comparison()


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


def answer_comparison():
    name = welcome_user()
    print('What is the result of the expression?')

    i = 0

    while i < 3:
        question, correct_answer = question_answer()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f''''{answer}' is wrong answer ;(.
Correct answer was '{correct_answer}'.
Let's try again, {name}!''')
            break
        i += 1
        if i == 3:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
