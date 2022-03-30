print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay let's play:)")
score = 0
answer = input ("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print ('correct!')
    score += 1
else:
    print ('Incorrect!')

answer = input ("What does ALU stand for? ")

if answer.lower() == "arithmetic logical unit":
    print ('correct!')
    score += 1
else:
    print ('Incorrect!')

answer = input ("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print ('correct!')
    score += 1
else:
    print ('Incorrect!')

answer = input ("What does keyboard do? ")

if answer.lower() == "type":
    print ('correct!')
    score += 1
else:
    print ('Incorrect!')

print ("You got " + str(score) + " questions correct!")

