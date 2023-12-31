#### Time's Up - the fastest version of Zork you'll ever play
#### SomeThing

#### RNGesus has entered the chat
import random

#### RNGesus
RNGesus = random.randint(0, 1)

#### Beginning steps
steps = random.randint(50, 60)

#### User inventory
gun         = 0
sword       = 0
camera      = 0
binoculars  = 0

#### Starting Position
start_hor = random.randint(0, 4) # starting hor
start_ver = random.randint(0, 4) # starting ver

#### Escape Position
end_hor = random.randint(0, 4) # escape hor
end_ver = random.randint(0, 4) # escape hor

#### Player Positions
hor = start_hor
ver = start_ver

min_hor = 0
min_ver = 0

max_hor = 4
max_ver = 4

#### Loose Brick
lb = 0

#### User Path
move_north      = 0
move_west       = 0
move_east       = 0
move_south      = 0
look_north      = 0
look_west       = 0
look_east       = 0
look_south      = 0

#### The Intro
print()
print("<<<                                   \x1B[1mWelcome to Zork Xtreme\x1B[0m                                                                         >>>")
print(f"<<< In this game you have a limited number of moves to escape \x1B[3mThe Beast\x1B[0m. You have {steps} moves to escape.                                >>>")
print('<<< Write "Look Left" to turn to your left, "Look Right" to turn to your right and "Move North","East","West" or "South" to move.    >>>')
print('<<< To pick up an item enter "pick up" <item>.                                                                                       >>>')
print("<<< When you're ready to begin type \"start\" and press ENTER.")
print()

for n in range(1):
    begin = input("<<< Are you ready to run? ").lower()
    if begin == "start":
        print()
        print("========")
        print("Let's Go")
        print("========")
        print()
    else:
        print()
        print("<<< Too scared? No one blames you. Come back when you're ready.                                           >>>")
        print()
        exit()

#### User inputs

while steps != 1:
        # Map Layout
        # Row Zero (0)
       if hor == 0 and ver == 0:
               
              print()
              print("\x1B[1mTowering walls as far as the eye can see surround you to the West and South. The fog of the forest makes\nit hard to see the path from the door to the west running to the east.")
              print("\x1B[1mIn the distant North you see a light through the trees but the forest is thick and dark, you should stay\nclose to the wall.")
              print()
              print()
        
       if hor == 1 and ver == 0:
               
              print()
              print("\x1B[1mThe fog is thinner here, you can see the path winding through the trees to the west and to the east.")
              print("\x1B[1mTo the north the forest grows thicker and looks unforgiving.")
              print()
              print()

       if hor == 2 and ver == 0:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       if hor == 3 and ver == 0:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       if hor == 4 and ver == 0:
              
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()
        
        # Row One (1)
       if hor == 0 and ver == 1 and lb == 1:
              
              print()
              print("\x1B[1mYou're surrounded by dense trees and shrubbery, you decide to hold close to the western wall so you\ndon't get lost.")
              print("\x1B[1mYou stub your toe on the brick you dropped on the floor. -1 to run away.")
              print()
              print()
               
       if hor == 0 and ver == 1 and lb != 1:
               
              print()
              print("\x1B[1mYou're surrounded by dense trees and shrubbery, you decide to hold close to the western wall so you\ndon't get lost.")
              print("\x1B[1mAs you run your hand over the bricks to keep your way you notice one of the bricks is loose from\nthe wall.")
              print()
              print()
        
       if hor == 1 and ver == 1:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       if hor == 2 and ver == 1:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       if hor == 3 and ver == 1:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()
        
       if hor == 4 and ver == 1:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()
        
        # Row Two (2)
       if hor == 0 and ver == 2:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()
        
       if hor == 1 and ver == 2:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       if hor == 2 and ver == 2:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       if hor == 3 and ver == 2:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       if hor == 4 and ver == 2:
               
              print()
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

        # Row Three (3)
       if hor == 0 and ver == 3:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       if hor == 1 and ver == 3:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       if hor == 2 and ver == 3:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       if hor == 3 and ver == 3:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       if hor == 4 and ver == 3:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

        #Row Four (4)
       if hor == 0 and ver == 4:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       if hor == 1 and ver == 4:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       if hor == 2 and ver == 4:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       if hor == 3 and ver == 4:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       if hor == 4 and ver == 4:
               
              print()
              print("\x1B[1mThere's a clearning in the forrest and the wall here is broken through but climing it looks deadly\nbased on the steep drop.")
              print("\x1B[1mYou make out a faint object in the distance, if only you had something to get a better look.")
              print()
              print()



       print("What would you like to do? ")
       user_input = input("> ").lower().strip()

        # Boarder Control
       if user_input == "move north" and ver == max_ver:
              print()
              print("A giant wall stands in your way.")
              print("Horizontal: ", hor, "Vertical: ", ver)
              print()

       elif user_input == "move west" and hor == min_hor:
              print()
              print("A giant wall stands in your way.")
              print("Horizontal: ", hor, "Vertical: ", ver)
              print()

       elif user_input == "move east" and hor == max_hor:
              print()
              print("A giant wall stands in your way.")
              print("Horizontal: ", hor, "Vertical: ", ver)
              print()

       elif user_input == "move south" and ver == min_ver:
              print()
              print("A giant wall stands in your way.")
              print("Horizontal: ", hor, "Vertical: ", ver)
              print()

        # Movement
       elif user_input == "move north":
              ver += 1
              steps -= 1
              print(hor, ", ", ver)
       elif user_input == "move west":
              hor -= 1
              steps -= 1
              print(hor, ", ", ver)
       elif user_input == "move east":
              hor += 1
              steps -= 1
              print(hor, ", ", ver)
       elif user_input == "move south":
              ver -= 1
              steps -= 1
              print(hor, ", ", ver)

        # Inspect
       elif user_input == "inspect brick" and hor == 0 and ver == 1:
              lb += 1
              print("==============================")
              print("\x1B[1mDon't look back.")
              print("\x1B[1mIt will only catch you faster.")
              print("==============================")
              print()
       elif user_input == "inspect brick":
              print("What brick?")
       


       # Pick up Items
       elif user_input == "pick up gun" and gun == 1:
              print()
              print("===========================================================================")
              print("\x1B[1mYou already have a gun and we don't trust you to have two.")
              print("\x1B[1mShouldn't you be trying to get out of here?.")
              print("===========================================================================")
              print()

       elif user_input == "pick up gun":
              gun += 1
              print()
              print("===========================================================================")
              print("\x1B[1mYou put the gun in your belt.")
              print("\x1B[1mDon't shoot yourself.")
              print("===========================================================================")
              print()

       elif user_input == "pick up sword" and sword == 1:
              print()
              print("===========================================================================")
              print("\x1B[1mYou cannot carry two swords.")
              print("\x1B[1mDon't fall on it.")
              print("===========================================================================")
              print()

       elif user_input == "pick up sword":
              sword += 1
              print()
              print("===========================================================================")
              print("\x1B[1mYou put the sword over your shoulder.")
              print("\x1B[1mJust because you have a sword now doesn't make you a swashbuckler.")
              print("===========================================================================")
              print()

       elif user_input == "pick up camera" and camera == 1:
              print()
              print("===========================================================================")
              print("\x1B[1mCameras are out of stock.")
              print("\x1B[1mBloody tourists.")
              print("===========================================================================")
              print()

       elif user_input == "pick up camera":
              camera += 1
              print()
              print("===========================================================================")
              print("\x1B[1mYou put the camera strap around your neck.")
              print("\x1B[1mBloody tourists.")
              print("===========================================================================")
              print()

       elif user_input == "pick up binoculars" and binoculars == 1:
              print()
              print("===========================================================================")
              print("\x1B[1mYou already have the binoculars.")
              print("\x1B[1mYou know you only have one set of eyes right?")
              print("===========================================================================")
              print()

       elif user_input == "pick up binoculars":
              binoculars += 1
              print()
              print("===========================================================================")
              print("\x1B[1mYou put the binoculars into your sack.")
              print("\x1B[1mGood thing there aren't any windows 'round here.")
              print("===========================================================================")
              print()

       # Use Items
       elif user_input == "use binoculars" and hor == 4 and ver == 4:

              print()
              print("\x1B[1mYou see an old decrepit tower of a once great castle in the distance. Maybe that explains the walls...")
              for n in range(0, 25):
                     print()
              print("\x1B[1mSUDDENLY THROUGH THE ARROW SLITS OF THE TOWER YOU MAKE EYE CONTACT WITH IT.")
              print()
              print()

       elif user_input == "use binoculars":
              print()
              print("You look through the binoculars and see nothing due to the thick fog.")
              print()
              print()

       # Quit game
       elif user_input == "quit" or user_input == "exit":
              print()
              print("==============================")
              print("That's the cowards way out.")
              print("==============================")
              print()
              exit()
       
       # Uknown Inputs
       else:
              print()
              print("Uknown Command, see \"HELP\" for valid inputs.")
              print()



    
    #### PLACEHOLDER for later inspects

    # Binoculars
#elif user_input == "use binoculars" and binoculars == 1 and hor == 5 and ver == 5:
#        print("There's an old decrepit tower of a once great castle in the distance. Maybe that explains the walls...")
#        for n in range(25):
#            print()
#        print("SUDDENLY THROUGH THE ARROW SLITS OF THE TOWER YOU MAKE EYE CONTACT WITH IT.\n")
#elif user_input == "use binoculars" and binoculars == 0:
#        print()
#        print("You are not carrying any binoculars")
#        print()
#else:
#        print("You look through the binoculars and see nothing, the fog is too thick.")
        
    



#### VALUE CHECK ####
print(f"Guns         : {gun}")
print(f"Sword        : {sword}")
print(f"Camera       : {camera}")
print(f"Binoculars   : {binoculars}")
print()
print(f"Moves: {move_north}")
print(f"Moves: {move_east}")
print(f"Moves: {move_west}")
print(f"Moves: {move_south}")
print()


#if user_input == "use gun" and gun == 1 and RNGesus == 1:
#print("<<< You come to a clearing in the middle of the misty woods. You see a faint light in the distance.")
