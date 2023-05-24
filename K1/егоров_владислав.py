# Создал Егоров Владислав
end_game_flag = False
while not end_game_flag:
    print("Welcome to my Text Adventure Game!")
    # Introduction
    print("\nYou wake up in a dark room with no memory of how you got there. "
          "The only thing you can see is a door on the other side of the room.")
    # First decision
    decision = input("\nWhat do you do?\n"
                     "A: Try to open the door.\n"
                     "B: Look for a light switch.\n"
                     "Choose A or B: ").upper()
    if decision == "A":
        print("\nThe door is locked. You need to find a key.")
        # Second decision
        decision2 = input("\nWhat do you do?\n"
                          "A: Search the room.\n"
                          "B: Break down the door.\n"
                          "Choose A or B: ").upper()
        if decision2 == "A":
            print("\nYou find a key hidden under the bed. You unlock the door and escape to freedom!")
        elif decision2 == "B":
            print("\nYou try to break down the door, but it's too strong and you injure yourself. "
                  "You pass out and are trapped forever.")
        else:
            print("\nInvalid choice. You stand there until you starve to death.")
    elif decision == "B":
        print("\nYou find a light switch on the wall and turn it on. "
              "You see that there is a key on the desk in the corner of the room.")
        # Second decision
        decision2 = input("\nWhat do you do?\n"
                          "A: Take the key and try to open the door.\n"
                          "B: Search the room for clues.\n"
                          "Choose A or B: ").upper()
        if decision2 == "A":
            print("\nYou take the key and unlock the door. You escape to freedom!")
        elif decision2 == "B":
            print("\nYou find a note that says 'The key is the only way out.' "
                  "You take the key and unlock the door. You escape to freedom!")
        else:
            print("\nInvalid choice. You stand there until you starve to death.")
    else:
        print("\nInvalid choice. You stand there until you starve to death.")
    choice = input('Ещё раз? (Y) или любое значение бля выхода')
    if choice != 'Y':
        end_game_flag = True
