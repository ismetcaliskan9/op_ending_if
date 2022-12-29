print('''
                  .--------------------------------...
               ,'-------------------------------,'   |
              /                                /     |
             /________________________________/    ,'|
             |               ..               |  ,'  |
             |___________-==/69\==-___________|,' /) |.
             |  \    \     ((  ))     /    /  |  (/  |-. .
             |   \    \     \{}/     /    /   |    .' .  .
          . '|    \    \     )(     / _  /    |    ,   .  .
         . . |\    \    \    \/    _.( ~-.   /|\ ,' .   . .
       ` .  -`_-.--.______..._____( ,/  ` \~-.|,' .   .
        .  `    .     .       .  ,'\. ~-  . , .  .  .   .
           .  `   .     ,   .      , ~~-.' .  .    .
''')
print("Welcome to Raftel!")
print("Your mission is to find the One Piece.")
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".').lower()

if choice1 == "left":
  choice2 = input('You\'ve come to a river. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the mountain unharmed. There is a entrance with 3 doors. One red, one yellow, one blue. Which colour do you choose? ").lower()
    if choice3 == "red":
      print("Hero Garp is in this room! Game over.")
    elif choice3 == "yellow":
        print("You found the One Piece! Heil Pirate King!")
    elif choice3 == "blue":
      print("This room is full of Blackbeard and his crewmates! Game over.")
  else:
    print("Sea kings ate you! Game over.")
else:
  print("There is no right in this game. Try left pls.")