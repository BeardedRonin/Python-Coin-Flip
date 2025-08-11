# Hopefully this script should run a simple coin toss game
import random
import time

#Variables
Heads = ("Heads")
Tails = ("Tails")
Result = random.choice(["Heads","Tails"])
TimesPlayed = 0
Score = 0
ResultsList = []

UserPlaying = input("Do you want to play a game? y/n \n")
if UserPlaying == "y" or "yes":
    PlayTimes = int(input("OK, how many times do you want to play? \n"))
else:
    print("Thanks for your time, see you later!")

while TimesPlayed < PlayTimes:
    UserChoice=input("Pick Heads or Tails...\n")
    time.sleep(1)
    print(Result)
    ResultsList.append(Result)
    if Result == UserChoice:
        Score += 10
        print("Yay, you win! \n"
        "Your score is now " ,Score,)
    else:
        Score -= 10
        print("Better luck next time! \n"
        "Your score is now ",Score,)
    TimesPlayed = TimesPlayed + 1

print("Thats great, thanks for playing! \n"
      "Your final score is ",Score, "\n"
      "It went down like ",ResultsList
      )
