print('Welcome to Quiz')
answer = input('Are you ready to play the Quiz ? this is a yes or no game(yes/no) :')
score = 0
total_questions = 3

if answer.lower() == 'yes':
    answer = input('Question 1: are you ok?')
    if answer.lower() == 'no':
        score += 1
        print('correct')
    else:
        print('Wrong Answer no one is')

    answer = input('Question 2: Do you follow any games? ')
    if answer.lower() == 'yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer i know you do')

    answer = input('Question 3: am i real')
    if answer.lower() == 'no':
        score += 1
        print('correct')
    else:
        print('Wrong Answer we both know thats wrong')

print('Thankyou for Playing this small quiz game, you attempted', score, "questions correctly!")
mark = (score / total_questions) * 100
print('Marks obtained:', mark)
print('BYE!')