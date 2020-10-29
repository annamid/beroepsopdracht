#explanation
def explanation():
    print("you are given a story with different choices.")
    print("but be aware, the choices you make decide your ending")

#start
def start():
    print("Witches and wizards have lived among the muggles peacefully for ages,") 
    print("but today everything changed.")
    print("you are a young witch on a normal muggle school living a normal life but they found you,")
    print("the seekers who kill everyone that is like you.")

#end4
def end4():
    print(" you lie and tell him you’ve been here before.")
    print("he looks at you with a questioned face but only for a second, his faces changes to a smile")
    print("you start crying. Everything comes back to you")
    print("the man grabs your hand")
    print("here you can finally be yourself and you are safe")
    print("END")

#end3
def end3():
    print("you tell him the truth.")
    print("he looks at you smiling and brings you to Hogwarts, the school for witches and wizards")
    print("where you can start your new life")
    print("END")

#story8 -> end 4 or end 3
def story8():
    print("you close your eyes and keep running. You bumped into something soft,")
    print("you opened your eyes and saw that it wasn’t a something but a someone.")
    print("you looked around, you were somewhere magical, somewhere where you felt home,")
    print("even though you never been there")
    print("the big man you bumped up against asks you if you are okay")
    print("do you LIE or tell him the TRUTH")
    choice = input ("lie or truth")
    
    if choice == "lie":
        end4()
    elif choice == "truth":
        end3()



#end5
def end5():
    print("you explore on your own but get hold back by some wizards in suits")
    print("you try to tell them what happened but it is no use")
    print("they don’t believe you and take you in")
    print("END")

#story9 -> story 10 or end 5
def story9():
    print("you cast incedio")
    print("the fire holds the seekers back and gives you time to run away")
    print("you run towards the light and as soon as you walk trough the gateway,")
    print(" you enter a whole different world")
    print("do you EXPLORE or ASK someone for help")
    choice = input ("explore or ask?: ")
    if choice == "explore":
        end5()
    elif choice == "ask":
        story10()

#end2
def end2():
    print("you cast flipendo but it was clearly not enough.")
    print("the seekers close in on you")
    print("there is nothing you can do")
    print("they take you in")
    print("END")


#story7 -> story 9 or end 2
def story7():
    print("forget it.")
    print("you turn around to see the seekers stand before you with their guns pointed towards you.")
    print("you take out your wand.")
    print("do you cast FLIPENDO to knock back the seekers or INCENDIO to make a fire in front of the seekers")
    choice = input ("flipendo or incendio?: ")

    if choice == "flipendo":
        end2()
    elif choice == "incendio":
        story9()

#story6 -> story 7 or story 8
def story6():
    print("you run towards the light. It becomes brighter and brighter the closer you are")
    print("you swore you saw something like a gateway,")
    print("like there was something behind the alley you have never seen before")
    print("but what if your wrong? If its just a wall and you are imagining things.")
    print("you have to decide quickly")
    print("do you keep GOING or do you STOP")
    choice = input ("going or stop?: ")

    if choice == "going":
        story8()
    elif choice == "stop":
        story7()

#story5 -> story 6 or story 7
def story5():
    print("you decide to do it on your own,")
    print(" you don’t want to risk your friends life for something he shouldn’t even be a part of.")
    print("you run as fast as you can towards the alley that has been your safe place for your whole life.")
    print("when you arrive something feels different.")
    print("out of nowhere a light appears at the end of the alley")
    print("do you INVESTIGATE or IGNORE it")
    choice = input ("investagate or ignore?: ")

    if choice == "investigate":
        story6()
    elif choice == "ignore":
        story7()

#story4 -> story 6 or story 7
def story4():
    print("you accept his offer but somewhere inside you feel a wave of guild flood over you,")
    print("like you alreadyknow this isn’t going to end well.")
    print("together you run towards the alley where you guys always used to play hide and seek")
    print("but something is different.")
    print("all of the sudden you hear people run towards you.")
    print("you grab your friends arm to pull him with you but he holds back")
    print("you have to go!")
    print("do you go WITHOUT him or do you STAY")
    choice = input ("without or stay?: ")

    if choice == "without":
        story6()
    elif choice == "stay":
        story7()


#story3 -> story 4 or story 5
def story3():
    print("your best friend only lives a couple of houses further down the street.")
    print("you carefully walk to his house, making sure no one sees you. you arrive and knock on his door.")
    print("For a couple minutes it’s quiet, but finally you see his sleepy face in the window")
    print("you explain him what’s happening and he offers to go with you")
    print("do you ACCEPT or DECLINE")
    choice = input ("accept or decline?: ")

    if choice == "accept":
        story4()
    elif choice == "decline":
        story5()


#story1 -> story 3 or story 5
def story1():
    print("you open the window and get out quickly")
    print("but where do you go next?")
    print("do you go to your FRIEND for help or RUN alone")
    choice = input ("friend or run?: ")

    if choice == "friend":
        story3()
    elif choice == "run":
        story5()

#end1
def end1():
    print("you open the door and grab your wand to fight, but you are not quick enough")
    print("there is a loud noise, making your ears hurt and... evrything goes silent")
    print("you look down and see blood come trough your shirt.")
    print("you got shot")
    print("END")

#story2 -> story 1 or end 1
def story2():
    print("you run out of your room as quickly as you can")
    print("the moment you reach the front door you see the seekers outside")
    print("do you GO or run back to your ROOM and climb to the window")
    choice = input ("go or room?: ")

    if choice == "go":
        end1()
    elif choice == "room":
        story1()
    
#begin story -> story 1 or story 2
def begin():
    print("you wake up from a loud knock on your bedroom door.")
    print("your mom barges in with a worried look on her face")
    print("She didn’t have to say anything, you knew what was going on.")
    print("they found you and want to kill you. you have no choice but to leave.")
    print("Do you get out through the WINDOW or go for the front DOOR")
    choice = input ("window or door?: ")

    if choice == "window":
        story1()
    elif choice == "door":
        story2()

explanation()
start()
begin()