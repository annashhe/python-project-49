from random import randint


task = 'What number is missing in the progression?'


def question_answer():
    step = randint(1, 10)
    missing_index = randint(0, 9)
    i = 0
    random_line = ''
    first_number = randint(1, 50)
    while i < 10:
        if i != missing_index:
            next_number = first_number + step
            random_line = random_line + ' ' + str(next_number)
            first_number = next_number
        elif i == missing_index and missing_index == 0:
            random_line = random_line + '..'
            correct_answer = first_number
            first_number = first_number
        else:
            random_line = random_line + ' ..'
            correct_answer = first_number + step
            first_number = next_number + step
        i += 1
    question = f'''Question: {random_line}'''
    return question, str(correct_answer)
