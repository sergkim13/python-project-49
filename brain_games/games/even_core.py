from random import randint


game_task = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    question = randint(1, 100)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (question, correct_answer)
