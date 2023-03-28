import random

green='\33[32m'
red='\33[31m'
default='\33[m'
yellow_back='\33[43m'
bold=('\33[1m')
underline=('\33[1m')

u_mark=0
m_mark=0
day=1
dummy=1

while (dummy!=0):

    if (u_mark>=100):
        print(bold+'''Wooh........!\n Game Over....! \n You won the game!  Now you are in the room number 100 and met the prensess! \3
        as per the agreement of the former king,
        Now you are the new king of the kingdom and I am your prime minister!\n''',default)
        break
    elif (m_mark>=100):
        print(bold+'''Wooh........!\n Game Over....! \n I won the game! Now I am in the room number 100 and I met the prensess! \3
        as per the agreement of the former king,
        Now I am the new king of the kingdome and you are my prime minister!\n''',default)
        break

#the user will play
#................ A new Day..........................

    else:
        print(yellow_back + bold + "Today is day",".........................................:",day , default,"\n")
        
        speed=input("What is the speed of throwing the dice? 1 or 2 or 3?: ")

        try:
            speed=int(speed)
        except: 
            speed=-1

        if (speed>=4):
            print (red+"Wrong input! We have only 3 speeds. Select a correct speed.", default)
        elif (speed<=0):
            print(red + "Wrong input! We have only 3 speeds. Select a correct speed", default)
        else:
            dice=random.randrange(1,7)

            if (speed==1):
                dice=dice+speed
                if (dice>=7):
                    dice=dice-6
                else:
                    dice=dice

            elif (speed==2):
                dice=dice+speed
                if (dice>=7):
                    dice=dice-6
                else:
                    dice=dice
            else:
                dice=dice+speed
                if (dice>=7):
                    dice=dice-6
                else:
                    dice=dice

            print("Face value of dice gave: ",dice)
            print("You are currently in room number:", u_mark)
            
            room=u_mark+dice

            if(room>=100):
                print("Move to room number 100")
                print(bold+'''Wooh........!\n Game Over....! \n You won the game!  Now you are in the room number 100 and met the prensess! \3
                as per the agreement of the former king,
                Now you are the new king of the kingdom and I am your prime minister!\n''',default)
                u_mark=100
                day=day+1
                break

            elif(room==5 or room==10 or room==15 or room==20 or room==25 or room==30 or room==35 or room==40 or room==50 or room==55 or room==60 or room==65 or room==70 or room==75 or room==80 or room==85 or room==95):
                print("So you have to go to room number:", dice+u_mark)
                print ("oh! There is a snake in the room number", room)
                print("Stay at the same room", "(Room number:",u_mark, ")")
                u_mark=u_mark
                day=day+1

            elif(room==9 or room==18 or room==27 or room==36 or room==45 or room==54 or room==63 or room==72 or room==81 or room==90 or room==99):
                print("So you have to go to room number:", dice+u_mark)
                print("Waaaaaah! There is a young lady in the room number:", room)
                print("I will play one additional chance for you to rest. ha ha haaa :D")
                u_mark=u_mark+dice
                day=day+1

#................ A new Day..........................
            
                print("\n",yellow_back + bold + "Today is day",".........................................:",day , default,"\n")
                
                print ("Now I will start to play. This is the additional chance I got yesterday\n")

                dice_m = random.randrange (1,7)
                speed_m=random.randrange(1,4)
                room_m=dice_m+m_mark
                print (green+"I choos the dice speed as..........", speed_m,)
                print("Face value of dice gave..........",dice_m)
                print("I am currently in room number..........", m_mark, default)

                if (room_m>=100):
                    print(green + "So, I will move to room number 100", default)
                    print(bold+'''Wooh........!\n Game Over....! \n I won the game! Now I am in the room number 100 and I met the prensess! \3
                    as per the agreement of the former king,
                    Now I am the new king of the kingdome and you are my prime minister!\n''',default)
                    u_mark=100
                    day=day+1
                    break

                elif(room_m==5 or room_m==10 or room_m==15 or room_m==20 or room_m==25 or room_m==30 or room_m==35 or room_m==40 or room_m==50 or room_m==55 or room_m==60 or room_m==65 or room_m==70 or room_m==75 or room_m==80 or room_m==85 or room_m==95):
                    print(green + "So I have to go to room number:", dice_m+m_mark , default)
                    print (green+"oh! There is a snake in the room number", room_m)
                    print("But as per our agreement, I can not go to find any safe room. I will stay here for today", default)
                    m_mark=m_mark+dice_m
                    day=day+1

                elif(room_m==9 or room_m==18 or room_m==27 or room_m==36 or room_m==45 or room_m==54 or room_m==63 or room_m==72 or room_m==81 or room_m==90 or room_m==99):
                    print(green + "So I have to go to room number:", dice_m+m_mark , default)
                    print(green + "Waaaaaah! There is a young lady in the room number:", room_m)
                    print("But as per our agreement, you will not get any additional chance to play tomorrow", default)
                    m_mark=m_mark+dice_m
                    day=day+1
            
                else:
                    print(green + "So I have to go to room number:", dice_m+m_mark , default)
                    print (green + "Room number", room_m, "is a safe room. I will stay there :)")
                    print ("Tomorrow again I will play my Original chance........", default)
                    m_mark = m_mark+dice_m
                    day=day+1
            
            else:
                print("So you have to go to room number:", dice+u_mark)
                print ("\n Room number", room, "is a safe room. Stay there \2 \n")
                u_mark = u_mark+dice
                day=day+1
                garbage_room=dice+u_mark

#................ A new Day..........................

            print(yellow_back + bold + "Today is day",".........................................:",day , default,"\n")
            print (green + "Now I will play my chance..........\n", default)
                
                

# The Programme will play the game


            dice_m = random.randrange (1,7)
            speed = random.randrange(1,4)
            room = dice_m + m_mark
            print (green + "I choos the dice speed as..........", speed,)
            print("Face value of dice gave..........", dice_m)
            print("I am currently in room number..........", m_mark, default)

            

            if(room>=100):
                print(green+"I will move to romm number 100", default)
                print(bold+'''Wooh........!\n Game Over....! \n I won the game! Now I am in the room number 100 and I met the prensess! \3
                as per the agreement of the former king,
                Now I am the new king of the kingdome and you are my prime minister!\n''',default)
                m_mark=100
                day=day+1
                break
            

            elif(room==5 or room==10 or room==15 or room==20 or room==25 or room==30 or room==35 or room==40 or room==50 or room==55 or room==60 or room==65 or room==70 or room==75 or room==80 or room==85 or room==95):
                print(green+"So I have to go to room number:", dice_m + m_mark)
                print ("oh! There is a snake in the room number", room)
                print("So I will not move and stay at the same room", "(Room number:",m_mark, ")", default)
                m_mark=m_mark
                day=day+1

            elif(room==9 or room==18 or room==27 or room==36 or room==45 or room==54 or room==63 or room==72 or room==81 or room==90 or room==99):
                print(green+"So I have to go to room number:", dice_m + m_mark)
                print("Waaaaaah! There is a young lady in the room number:", room)
                print("You can play one additional chance for me to rest. ha ha haaa :D \n ", default)
                m_mark=m_mark+dice_m
                day=day+1

#................ A new Day..........................

                print(yellow_back + bold + "Today is day",".........................................:",day , default,"\n")
                print ("Now you should start to play..........","\n")

                speed=input("What is the speed of throwing the dice? 1 or 2 or 3?: ")

                try:
                    speed=int(speed)
                except: 
                    speed=-1

                if (speed>=4):
                    print ("Wrong input! We have only 3 speeds. Select a correct speed.")
                elif (speed<=0):
                    print("Wrong input! We have only 3 speeds. Select a correct speed")
                else:
                    dice=random.randrange(1,7)

                    if (speed==1):
                        dice=dice+speed
                        if (dice>=7):
                            dice=dice-6
                        else:
                            dice=dice

                    elif (speed==2):
                        dice=dice+speed
                        if (dice>=7):
                            dice=dice-6
                        else:
                            dice=dice
                    else:
                        dice=dice+speed
                        if (dice>=7):
                            dice=dice-6
                        else:
                            dice=dice

                    print("Face value of dice gave: ",dice)
                    print("You are currently in room number:", u_mark)

                    room_m=u_mark+dice

                    if(room_m>=100):
                        print("you have to go to room number 100")
                        print(bold+'''Wooh........!\n Game Over....! \n You won the game!  Now you are in the room number 100 and met the prensess! \3
                        as per the agreement of the former king,
                        Now you are the new king of the kingdom and I am your prime minister!\n''',default)
                        u_mark=100
                        day=day+1
                        break

                    elif (room_m==5 or room_m==10 or room_m==15 or room_m==20 or room_m==25 or room_m==30 or room_m==35 or room_m==40 or room_m==50 or room_m==55 or room_m==60 or room_m==65 or room_m==70 or room_m==75 or room_m==80 or room_m==85 or room_m==95):
                        print("So you have to go to room number:", dice+u_mark)
                        print ("oh! There is a snake in the room number", room_m)
                        print("But as per our agreement, You can not go to find any safe room. You have stay here for today")
                        u_mark=u_mark+dice
                        day=day+1

                    elif(room_m==9 or room_m==18 or room_m==27 or room_m==36 or room_m==45 or room_m==54 or room_m==63 or room_m==72 or room_m==81 or room_m==90 or room_m==99):
                        print("So you have to go to room number:", dice+u_mark)
                        print("Waaaaaah! There is a young lady in the room number:", room_m)
                        print("But as per our agreement, you will not get any additional chance to play untill tomorrow")
                        u_mark=u_mark+dice
                        day=day+1
            
                    else:
                        print("So you have to go to room number:", dice+u_mark)
                        print ("Room number", room_m, "is a safe room. you can stay there :)")
                        print ("Tomorrow again you can play your Original chance also........")
                        u_mark = u_mark+dice
                        day=day+1

            
            
            else:
                print (green +"Room number", room, "is a safe room. Today I will stay there :)")
                print ("Tomrrow you can play again..........",default,"\n")
                m_mark = m_mark+dice
                day=day+1


