print("Hello You!, I am Anna")
print("who are you?")
naam = input("Enter name: ")
print("hello " + naam)

print("I'm new here at Mediacollege")
print("pssst, do you want to hear a secret?")


anwser=(input("yes or no?: "))
if anwser.lower()=="yes":
    print("okay listen closely")
else:
    print("okay well I'm gonna tell you anyway")

print("There is a secret room somewhere here in the school")
print("when you enter the school you have to go right or left... I forgot")
print("what do you think?")
anwser=(input("right or left?: "))
if anwser.lower()=="right":
    print("ah yes now I remember it was indeed go right first, thank you")
else:
    print("wait i remember now, it was go right first but thank you ayway")

print("now if you enter the second door you see you'll arrive in a dark room with another 3 doors in front of you")
print("what door are you taking?")
anwser=(input("1, 2 or 3?: "))
if anwser=="1":
    print("You did it! but the story is far from done yet")
    print("to be continued....")
    exit()
elif anwser=="2":
    print("it was not the right door and you got caught by a teacher")
    exit()
elif anwser=="3":
    print("it was not the right door and you got caugh by a teacher")
    exit()
else:
    print("wrong anwser closing program")
    exit()



