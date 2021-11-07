import os
def menu_to_enter():
    print('''
    --------PARQUES(1.0)--------
    1.Enter to game
    2.Exit
    ''', end='')

def menu_player(options, name_user, conected, color_user):
    os.system('clear')
    print(f"Username:{name_user}")
    print(f"connected:{'Yes' if conected else 'Not'}")
    print(f"number of players connected:{len(options['bd_users'])}")
    for i, user in enumerate(options['bd_users']):
        print(f"Player({i+1}), Name:{user}")
    print(f"assigned color:{color_user}")
    print(f"your turn:{'Yes' if options['your_turn'] else 'Not'}")
