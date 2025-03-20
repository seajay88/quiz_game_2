print('Welcome to the quiz game!')

# input is a function that allows the user to input something directly.
# put space after punctuation in input to put space between question and answer.
playing = input("Do you want to play? ")

# != is not equal
# if player is not playing, quit the game (app)
# quit and if is a function in python
#if the user types anything but yes, the app will quit.
# put a colon: if the condition is true, the indented actions will be performed.
#.lower will make all characters from user input lowercase.
if playing.lower() != "yes":
    quit()

print ("Okay! Let's play! ")
score = 0

#== (is equal to)
# indent lines after colon to execute simultaneously

answer = input("Who is the all time NFL passing yards leader? ")
if answer.lower() == "tom brady":
    print('CORRECT!')
    score += 1

else:
    print("Incorrect!")

answer = input("Who is the all time NFL Rushing Yards leader? ")
if answer.lower() == "emmitt smith":
    print('CORRECT!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who won Super Bowl 59? ")
if answer.lower() == "the philadelphia eagles":
    print('CORRECT!')
    score += 1
else:
    print("Incorrect!")
    print("seriously?")

answer = input("Who was the 2010 rushing champion? ")
if answer.lower() or answer.upper() == "arian foster":
    print('CORRECT!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the best Quarterback in the NFL? (Carl Bias) ")
if answer.lower() == "jalen hurts":
    print('CORRECT! ')
    print('FLY EAGLES FLYYYYY')
    score += 1
else:
    print("Incorrect!")
    print('idiot...')

print("You Got " + str(score) + " questions correct")
print("You Got " + str((score / 5) * 100) + "%.")
