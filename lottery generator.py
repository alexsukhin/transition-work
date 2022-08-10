import random

lotterywin = []
guessarray = []
n = 0
valid = False

print("Choose seven numbers between 1 and 49.")
while valid == False:
    guess = int(input(""))
    guessarray.append(guess)

    if guess < 1 or guess > 49:
        guessarray.clear()
        print("Number outside of range. Please retry.")

    if len(guessarray) == 7:
        valid = True


def doLottery():
    print("Lottery winners!")

    lotteryinv = list(range(1, 50))

    for i in range(6):
        n = random.choice(lotteryinv)
        print(n)
        lotterywin.append(n)
        lotteryinv.remove(n)
    
    n = random.choice(lotteryinv)
    print("Bonus: " + str(n))
    lotterywin.append(n)
    lotteryinv.remove(n)
    print(lotteryinv)
    
doLottery()

for i in range(7):
    if lotterywin[n] == guessarray[n]:
        print(str(guessarray[n]), " is valid.")
    n += 1

print("Probability of finding these numbers is 1 in 432 billion!")
