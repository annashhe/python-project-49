from random import randint


task = 'What number is missing in the progression?'
MAX_STEP = 100 #maximum step
SET = 10 #number of numbers in set
MAX_NUMBER = 50 #maximum number to start list with


def generate_question_and_get_answer():
    first_number = randint(1, MAX_NUMBER)
    step = randint(1, MAX_STEP)
    missing_index = randint(0, SET-1)
    i = 0
    random_sentence = ''
    while i < SET:
        if i != missing_index:
            next_number = first_number + step
            random_sentence = random_sentence + ' ' + str(next_number)
            first_number = next_number
        elif i == missing_index and missing_index == 0:
            random_sentence = random_sentence + '..'
            correct_answer = first_number
            first_number = first_number
        else:
            random_sentence = random_sentence + ' ..'
            correct_answer = first_number + step
            first_number = next_number + step
        i += 1
    question = f'''Question: {random_sentence}'''
    return question, str(correct_answer)
