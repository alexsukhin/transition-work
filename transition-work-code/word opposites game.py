import random

words = ['hot', 'summer', 'hard', 'dry', 'simple', 'light',
 'weak', 'male', 'sad', 'win', 'small', 'ignore',
  'buy', 'succeed', 'reject', 'prevent', 'exclude']
antonyms = ['cold', 'winter', 'soft', 'wet', 'complex', 'darkness',
 'strong', 'female', 'happy', 'lose', 'big', 'pay attention',
  'sell', 'fail', 'accept', 'allow', 'include']

n = 1
max = 16

for i in range(8):
    first = random.randint(0, max)
    second = random.randint(0, max)

    print('Q' + str(n) + ':', words[first], 'is to', antonyms[first], 'as', antonyms[second], 'is to ... ?')
    answer = input("Answer: ")
    if answer == words[second]:
        print("Correct!")
    else:
        print("Wrong.")

    unwanted = [first, second]

    for ele in sorted(unwanted, reverse = True):
        del words[ele]
        del antonyms[ele]

    n += 1
    max -= 2

