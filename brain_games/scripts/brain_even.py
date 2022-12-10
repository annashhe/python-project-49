#!/usr/bin/env python3
import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    i = 0

    while i < 3:
        number = randint(1, 100)
        print('Question: ', number)
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

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
