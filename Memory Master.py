'''
NOTE
medium column: 13
1/4 column:    7
3/4 column:    19
medium row:    8
'''




import time
import random

#block set
empty = " "
wall  = "#"
enemy = "V"

#screen set
width = 25
height = 15



#FUNCTIONS



def draw_frame(delay):

    for i in range(height):
        
        if i == 0 or i == height - 1:
            for i in range(width):
                print(wall, end="")

        else:
            for i in range(width):
                if i == 0 or i == width - 1:
                    print(wall, end="")
                else:
                    print(empty, end="")
        
        print(end="\n")
        time.sleep(delay)



def curser_up(how_many):
    count = 0

    while count < how_many:
        print(end="\033[F")
        count += 1
    

def curser_down(how_many):
    count = 0

    while count < how_many:
         print(end="\n")
         count += 1

def draw_enemy(column):
    for i in range(width):
        if i == column - 1:
            print(enemy, end="")
            break
        elif i == 0 or i == width - 1:
            print(wall, end="")
        else:
            print(empty, end="")
    print(end="\r")


def draw_anything(shape, column):
    for i in range(width):
        if i == column - 1:
            print(str(shape), end="")
            break
        elif i == 0 or i == width - 1:
            print(wall, end="")
        else:
            print(empty, end="")
    print(end="\r")

def draw_flash(column):
    curser_up(1)
    draw_anything("\4\4\4", column - 1)
    curser_down(1)
    draw_anything("\4\4\4", column - 1)
    curser_down(1)
    draw_anything("\4\4\4", column - 1)

def draw_right_flash():
    curser_up(8)
    draw_flash(19)
    draw_enemy(13)
    curser_up(1)
    draw_enemy(13)
    curser_up(1)
    draw_enemy(13)
    curser_down(9)

def draw_left_flash():
    curser_up(8)
    draw_flash(7)
    curser_down(7)

def clear_flash():
    curser_up(9)
    clear_frame()
    draw_enemy(13)
    curser_down(1)
    clear_frame()
    draw_enemy(13)
    curser_down(1)
    clear_frame()
    draw_enemy(13)
    curser_down(7)

def clear_frame():
    for i in range(width):
        if i == 0 or i == width - 1:
            print(wall, end="")
        else:
            print(empty, end="")
    print(end="\r")

def clear_all():
    print("                                                            ")



#TUTORIAL FUNCTION
def tutorial():

    #tutorial
    print("")
    print("if i show you sentence like this, read carefully [y]")
    print("the [y] means enter 'y' if you understand it.")
    curser_up(3)
    input("read below and respond here: ")

    curser_up(1)
    clear_all()
    clear_all()
    clear_all()
    curser_up(3)

    time.sleep(1)


    #drawing square frame
    draw_frame(0.1)

    #drawing horizontal line
    curser_up(14)

    for i in range(13):
        draw_enemy(13)
        curser_down(1)
        time.sleep(0.1)

    curser_down(1)


    time.sleep(0.1)


    # guide(show 1,2 on each side)
    curser_up(8)
    draw_anything(2, 19)
    draw_enemy(13)
    draw_anything(1, 7)
    curser_down(9)

    #understanding the rule
    print("left = 1, right = 2 [y]")
    curser_up(2)
    a = input("respond: ")

    #erase the numbers on the screen
    clear_all()
    curser_up(10)
    clear_frame()
    draw_enemy(13)
    curser_down(8)
    clear_all()

    time.sleep(0.5)

    #understanding the rule
    print("remember the flashes [y]")
    curser_up(2)
    a = input("respond: ")

    curser_up(1)
    clear_all()
    clear_all()
    curser_up(2)

    time.sleep(0.5)

    draw_left_flash()
    curser_down(1)
    print("if it flashes like this, [y]")
    curser_up(2)
    input("respond: ")

    curser_up(1)
    clear_all()
    clear_all()
    curser_up(1)

    print("you should enter 1 [enter 1]")
    curser_up(2)

    while True:
        a = input("respond: ")
        if a != "1":
            curser_up(1)
            clear_all()
            curser_up(1)
            print("              Wrong!", end="\r")
        else:
            break

    curser_up(1)
    clear_all()
    clear_all()
    curser_up(2)

    clear_flash()
    print("correct!")


    time.sleep(1)

    curser_up(1)
    clear_all()
    clear_all()
    curser_up(2)

    draw_right_flash()

    time.sleep(0.7)

    clear_flash()

    time.sleep(0.3)

    draw_left_flash()

    time.sleep(0.7)

    clear_flash()

    curser_down(1)


    print("enter the answer (2 , 1)")
    curser_up(2)

    while True:
        a = input("respond: ")
        if a == "21":
            curser_up(1)
            clear_all()
            curser_up(1)
            print("              Enter one number at a time!", end="\r")
        elif a != "2":
            curser_up(1)
            clear_all()
            curser_up(1)
            print("              Wrong!", end="\r")
        else:
            break

    curser_up(1)
    clear_all()
    clear_all()
    curser_up(2)

    clear_flash()


    print("Correct!")
    time.sleep(1)
    curser_up(1)
    clear_all()


    print("enter the answer")
    curser_up(2)

    while True:
        a = input("respond: ")
        if a == "21":
            curser_up(1)
            clear_all()
            curser_up(1)
            print("              Enter one number at a time!", end="\r")
        elif a != "1":
            curser_up(1)
            clear_all()
            curser_up(1)
            print("              Wrong!", end="\r")
        else:
            break

    curser_up(1)
    clear_all()
    clear_all()
    curser_up(2)

    clear_flash()


    print("Correct!")
    time.sleep(1)
    curser_up(1)
    clear_all()
    curser_up(1)

    print("tutorial end", end="\r")

    time.sleep(1)

    for i in range(0, 16):
        clear_all()
        curser_up(2)



def game_run():

    #game countdown
    print("start in 3.")
    time.sleep(1)
    curser_up(1)
    print("start in 2..")
    time.sleep(1)
    curser_up(1)
    print("start in 1...")
    time.sleep(1)
    curser_up(1)
    clear_all()
    curser_up(1)

    print("remember!")

    time.sleep(1)

    curser_up(1)
    clear_all()
    curser_up(1)



    #memorize game begin

    answer = []
    level = 0

    while True:

        level += 1

        print("level: " + str(level))
        curser_up(1)

        #add 1 or 2 to answer list
        answer.append(random.randint(1, 2))

        #draw flash on random side followin the list
        for i in range(0, len(answer)):
            if answer[i] == 1:
                draw_left_flash()
            else:
                draw_right_flash()

            time.sleep(0.7)

            clear_flash()

            time.sleep(0.3)

        #repeat guessing until the end
        for i in range(0, len(answer)):

            #get user respond and if it is not 1 or 2, output error message and try again
            only_number = False
            while only_number == False:
                guess = input("respond: ")
                if guess == "1" or guess == "2":
                    only_number = True
                    guess = int(guess)
                else:
                    print("ERROR: please enter only 1 or 2")
                    curser_up(2)
                    clear_all()
                    curser_up(1)

            if guess == answer[i]:
                print("Correct!")
                game_over = False
                time.sleep(0.4)
                curser_up(2)
                clear_all()
                clear_all()
                curser_up(2)
            else:
                clear_all()
                clear_all()
                curser_up(2)
                print("Wrong!")
                print("answer: " + str(answer[i]))
                time.sleep(1)
                print("GAME OVER")
                game_over = True
                break
            

        if game_over:
            break


    time.sleep(2)

    for i in range(0, 20):
        clear_all()
        curser_up(2)
        time.sleep(0.1)
    
def draw_horizontal_line():
    #drawing horizontal line
    curser_up(14)

    for i in range(13):
        draw_enemy(13)
        curser_down(1)
        time.sleep(0.1)

def draw_ui():
    print("Play Game [1]")
    print("Tutorial  [2]")

def eraze_ui():
    curser_up(3)
    clear_all()
    clear_all()
    clear_all()
    clear_all()
    curser_up(3)




#----====----====----====----====+=+=+=+<-(-{-[-|GAME SCENE STARTS HERE|-]-}-)->+=+=+=+====----====----====----====----#
#----====----====----====----====+=+=+=+<-(-{-[-|GAME SCENE STARTS HERE|-]-}-)->+=+=+=+====----====----====----====----#
#----====----====----====----====+=+=+=+<-(-{-[-|GAME SCENE STARTS HERE|-]-}-)->+=+=+=+====----====----====----====----#
#----====----====----====----====+=+=+=+<-(-{-[-|GAME SCENE STARTS HERE|-]-}-)->+=+=+=+====----====----====----====----#
#----====----====----====----====+=+=+=+<-(-{-[-|GAME SCENE STARTS HERE|-]-}-)->+=+=+=+====----====----====----====----#
#----====----====----====----====+=+=+=+<-(-{-[-|GAME SCENE STARTS HERE|-]-}-)->+=+=+=+====----====----====----====----#
#----====----====----====----====+=+=+=+<-(-{-[-|GAME SCENE STARTS HERE|-]-}-)->+=+=+=+====----====----====----====----#
#----====----====----====----====+=+=+=+<-(-{-[-|GAME SCENE STARTS HERE|-]-}-)->+=+=+=+====----====----====----====----#




#drawing main lobby ui
print("\f\f -+<({[MEMORY MASTER]})>+-")
print("===========================")
draw_ui()


#repeating game
while True:
    #ui
    select = input("select: ")

    #when user choose to play game
    if select == "1":
        #eraze ui, draw game screen
        eraze_ui()
        draw_frame(0.1)
        draw_horizontal_line()
        curser_down(1)

        #user play game
        game_run()

        #when game end, draw ui back
        draw_ui()

    #when user choose tutorial
    elif select == "2":

        #there's a problem if you dont understand below
        eraze_ui()

        tutorial()

        draw_ui()

    #when user choose to type random things (maybe user feel boring)
    else:
        #error message
        print("ERROR: please enter only 1 or 2")
        curser_up(2)
        clear_all()
        curser_up(1)
