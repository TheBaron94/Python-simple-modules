# Module Six Milestone
# Adam Schmidt

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom', 'Exit': 'Exit'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar', 'Exit': 'Exit'},
        'Cellar': {'West': 'Bedroom', 'Exit': 'Exit'}
    }

# Def the different room objects.


def room_bedroom():
    print()
    print('You are in the Bedroom')
    options = rooms['Bedroom'].items()  # Retrieve the options for this from the dict.
    for direction, room in options:
        print('You can type {direction} to go to {room}'.format(direction=direction, room=room))
    choice = input('Where to: ').capitalize()
    while choice not in rooms['Bedroom'].keys():  # Choice verification.
        choice = input('Invalid option. Try again: ').capitalize()
    if choice == 'North':
        room_great_hall()
    elif choice == 'East':
        room_cellar()
    elif choice == 'Exit':
        exit_game()


def room_great_hall():
    print()
    print('You are in the Great Hall')
    options = rooms['Great Hall'].items()  # Retrieve the options for this from the dict.
    for direction, room in options:
        print('You can type {direction} to go to {room}'.format(direction=direction, room=room))
    choice = input('Where to: ').capitalize()
    while choice not in rooms['Great Hall'].keys():  # Choice verification.
        choice = input('Invalid option. Try again: ').capitalize()
    if choice == 'South':
        room_bedroom()
    elif choice == 'Exit':
        exit_game()


def room_cellar():
    print()
    print('You are in the Cellar')
    options = rooms['Cellar'].items()  # Retrieve the options for this from the dict.
    for direction, room in options:
        print('You can type {direction} to go to {room}'.format(direction=direction, room=room))
    choice = input('Where to: ').capitalize()
    while choice not in rooms['Cellar'].keys():  # Choice verification.
        choice = input('Invalid option. Try again: ').capitalize()
    if choice == 'West':
        room_bedroom()
    elif choice == 'Exit':
        exit_game()


def exit_game():
    print()
    print('You have decided to leave the game? really?')  # Sarcasm (had to have that in here somewhere)
    print('Thank you for playing.')
    print('Good Bye.')
    quit()


room_bedroom()

# Q: What is the most used language in programming?
# A: Profanity!
# I bet you thought id forgotten to include a joke this time
# but i decided to hide it in my code lol
