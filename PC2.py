while True:
    print('welcome, please type in what you want me to do.')
    option=raw_input()
    if option=='shut down':
        break
    elif option=='reboot':
        continue
    elif option=='quiz':
        print('enter a number from 1 to 5 to get a problem')
        quizoption=raw_input()
        if quizoption=='1':
            print('how many sides do a triangle have?')
            answer1=raw_input()
            if answer1=='3':
                print('correct')
                continue
            else:
                print('incorrect')
                continue
        elif quizoption=='2':
            print('what is 40*4?')
            answer2=raw_input()
            if answer2=='160':
                print('correct')
                continue
            else:
                print('incorrect')
                continue
        elif quizoption=='3':
            print('what is 50/2?')
            answer3=raw_input()
            if answer3=='25':
                print('correct')
                continue
            else:
                print('incorrect')
                continue
        elif quizoption=='4':
            print('what is 250+200?')
            answer4=raw_input()
            if answer4=='450':
                print('correct')
                continue
            else:
                print('incorrect')
                continue
        elif quizoption=='5':
            print('who became president?')
            print('A,Einstein B,Lincoln C,Elone Musk')
            answer5=raw_input()
            if answer5=='B':
                print('correct')
                continue
            else:
                print('incorrect')
                continue
        else:
            print('invalid command')
            print ""
            continue
    elif option=='cauculator':
        print('which operation??')
        operation=raw_input()
        if operation=='+':
            print('first vaulue')
            vau1p=raw_input()
            vau1p=int(vau1p)
            print('second vaulue')
            vau2p=raw_input()
            vau2p=int(vau2p)
            print(vau1p + vau2p)
            continue
        elif operation=='-':
            print('first vaulue')
            vau1mi=raw_input()
            vau1mi=int(vau1mi)
            print('second vaulue')
            vau2mi=raw_input()
            vau2mi=int(vau2mi)
            print(vau1mi - vau2mi)
            continue
        elif operation=='/':
            print('first vaulue')
            vau1d=raw_input()
            vau1d=vau1d+'.'
            vau1d=float(vau1d)
            print('second value')
            vau2d=raw_input()
            vau2d=vau2d+'.'
            vau2d=float(vau2d)
            print(vau1d / vau2d)
            continue
        elif operation=='*':
            print('first vaulue')
            vau1mu=raw_input()
            vau1mu=int(vau1mu)
            print('second vaulue')
            vau2mu=raw_input()
            vau2mu=int(vau2mu)
            print(vau1mu * vau2mu)
            continue
        else:
            print('invalid command')
            print ""
            continue
    elif option=='guess':
        ####################################################################################################################################
        #This is a guessing game with functions........................................................................................... #
        #The goal is to make this game let players guess a number and the computer will say if the player's number is too high or too low. #
        ####################################################################################################################################


        #Section 1: Prepare for The Guessing Game.
        print('Are You Ready??? (yes/no)')
        """p is for the propmt of all raw inputs."""
        p="Your Answer: "
        start=raw_input(p)
        if start=='yes' or start=='Yes' or start=='YES':
            """random is for the random number, time is for waiting"""
            import random
            import time
            """this is the game round's code, the game will run as the code block below."""
            def game():
                """cn for computer's number, randint for random interger."""
                cn=random.randint(0,100)
                print('your number is generated, it will be 0-100, type e to exit game.')
                """count down for player to prepare"""
                time.sleep(1)
                print('5')
                time.sleep(1)
                print('4')
                time.sleep(1)
                print('3')
                time.sleep(1)
                print('2')
                time.sleep(1)
                print('1')
                time.sleep(1)
                print('please start')
                """loop until the player guesses correctly, if entered a not number, it will tell you to enter a number, type e to exit game."""
                while True:
                    ans=raw_input(p)
                    """seeing if the player's number is correct"""
                    try:
                        ans=int(ans)
                        if ans==cn:
                            print('Correct!!')
                            break
                        elif ans>cn:
                            print('Too High!!')
                        else:
                            print('Too Low!!')
                        """if input is not a number, the code block below will run"""
                    except:
                        if ans=='e' or ans=='E':
                            print('Goodbye!!')
                            time.sleep(2)
                            break
                        else:
                            print('Please enter a number, or type e to exit game.')
            #section 2: run game.
            """def game(): made the code 'game()', the code 'game()' has the code for the game round in the gigantic code block, so if we use the code 'game', we will run the game."""
            game()
            #section 3: exit game.
            """game will exit in 5 seconds"""
            print('Game ended')
            continue
    
                

    elif option=="Ming-Ming" or option=="Evan":
        print("Congrats! You found an EASTER EGG!")
        continue
    elif option=="riskyprogram":
        print("Are you sure you want to run this program? [yes/no]")
        conf=raw_input()
        if conf=="yes":
              while True:
                  print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        elif conf=="no":
              print("you made the right desision")
              continue
        else:
              print("INVALID ANSWER")
    else:
        print('INVALID COMMAND')
        print ""
        continue
