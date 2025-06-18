#Adventure Game: Murder Case Edition
#Creative Addition: This gaame includes a hidde safe, multiple paths,
# and two differnt "end game" secnarios based on your investigation path.
# i gave my friend Gavin and freemam to play the game, and they said it's a nice game.i then explained the program how it works/run for them.



# def start_game():
#     print("You are a detective who's investigating a mysterious murder. The victim was found dead in their apartment, No signs of forced entry.")
#     print()

#     print("What do you do first?: EXAMINE the body or SEARCH the apartment for clues")

#     choice1 = input("> ").strip().lower()

#     if choice1 ==  choice1 == "examine":
#         examine_body()
#     elif choice1 == choice1 == "search":
#         search_room()
#     else:
#         print("Invalid choice. Please restart the game and choose EXAMINE Or SEARCH.")

# def examine_body():
#     print("\nYou examine the body and find a small, cryptic note clutched in the victim’s hand.")
#     print()

#     print("What do you do?: READ the note or CONTINUE examining the body for other clues")

#     choice2 = input("> ").strip().lower()

#     if choice2 == choice2 == "read":
#         print("\nThe note reads, 'The killer is someone close.' You now have a new lead.")
#         print("You decide to QUESTION the people closest to the victim.")
#         print("Game Over. Try other paths to uncover more.")
#     elif choice2 == choice2 == "continue":
#         print("\nYou find a hidden compartment in the victim’s desk containing a key.")
#         print("You don't know what it opens, but it could be important.")
#         print()

#         print("What do you do?: SEARCH for what the key opens or QUESTION the people closest to the victim")

#         choice3 = input("> ").strip().lower()

#         handle_key_scenario(choice3)
#     else:
#         print("Invalid choice. Please restart the game and choose SEARCH or QUESTION.")

# def search_room():
#     print("\nYou search the room and find a hidden compartment in the desk containing a mysterious key.You don't know what it opens, but it could be important.")
#     print()

#     print("What do you do?: SEARCH for what the key opens or QUESTION the people closest to the victim")

#     choice2 = input("> ").strip().lower()

#     handle_key_scenario(choice2)

# def handle_key_scenario(choice):
#     if choice == "a" or choice == "search":
#         print("\nYou find the key opens a safe in the victim’s bedroom.")
#         print("Inside, you discover a large sum of money and a list of names.")
#         print()

#         print("What do you do?: INVESTIGATE the list of names or QUESTION the people closest to the victim")

#         choice3 = input("> ").strip().lower()

#         if choice3 == "a" or choice3 == "investigate":
#             print("\nYou discover that the names are people who owed the victim large debts.")
#             print("You now have a solid list of suspects. Time to investigate them further.")
#             print("Game Over. You did well uncovering a key clue.")
#         elif choice3 == choice3 == "question":
#             print("\nYou question the people closest to the victim.")
#             print("They appear shocked, but you sense some are hiding something.")
#             print("Game Over. You may revisit the case with more evidence.")
#         else:
#             print("Invalid choice. Please restart the game and choose SEARCH or QUESTION.")
#     elif choice == choice == "question":
#         print("\nYou question the people closest to the victim.")
#         print("Their answers raise suspicions, but without evidence, you're stuck.")
#         print("Game Over. Try another path to find more clues.")
#     else:
#         print("Invalid choice. Please restart the game and choose SEARCH or QUESTION.")

# start_game()
my_list = [3,1,0,-1,-9]


largest = 0

for value in my_list:

    if value < largest:

        largest = value

print(f"The largest is {largest}")
