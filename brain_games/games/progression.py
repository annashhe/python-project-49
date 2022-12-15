from random import randint


task = 'What number is missing in the progression?'
MAX_STEP = 10  # maximum step
SET = 10  # number of numbers in set
MAX_NUMBER = 50  # maximum number to start list with


def generate_question_and_get_answer():
    start_number = randint(1, MAX_NUMBER)
    step = randint(1, MAX_STEP)
    missing_index = randint(0, SET - 1)
    finish_number = start_number + step * SET
    range_sentence = list(range(start_number, finish_number, step))
    correct_answer = range_sentence[missing_index]
    range_sentence[missing_index] = '..'
    range_sentence = list(map(str, range_sentence))
    progression = " ".join(range_sentence)
    question = f'''Question: {progression}'''
    return question, str(correct_answer)
