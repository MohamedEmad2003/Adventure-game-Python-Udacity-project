import time
import random
import sys
all_places = ["own house", "shop", "friend's house", "air filling station"]
place = random.choice(all_places)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower().strip()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Please, Enter the right and valid choice")
    return response


def intro():
    print_pause("\nYou find yourself standing in the street")
    print_pause("\nYou intend to go swimming in the sea.")
    print_pause("\nAnd you have a swimming float which is empty from air!")
    print_pause(f"\nYou must wear it when you are swim As you can't swim.")
    print_pause("\nIf you fill the float with air, you can't fill it again")
    print_pause(f"\nYou can ride a bus and go to {place} to fill the float")
    print_pause("\nIf you swim and the float is empty, you will drown.")


def get_order():
    response = valid_input(" \nEnter 1 to return and fill the float.\n"
                           "\nEnter 2 to go swimming with the empty air float",
                           "1", "2")
    if "1" == response:
        print_pause(f"You have returned to {place}, have filled the float.")
        print_pause("\n you are going to go to the street again")
        order_again()
    elif "2" == response:
        print_pause("the float was empty, you have been rescued from drowning")
        print_pause("...Game over!")

        connection()
    else:
        print_pause("please, Enter the right and valid choice")
        get_order()


def play_again():
    response = valid_input(" \nEnter yes if you want to play again\n"
                           "\nEnter no to close the game",
                           "yes", "no")
    if "yes" == response:
        print_pause("Good, Let's go and win")
        get_order()
    elif "no" == response:
        print_pause("\n Ok, Good Bye")
        sys.exit()


def connection():
    print_pause("Would you like to play again ?\n")
    play_again()


def order_again():
    response = valid_input(" \nEnter 1 to return and fill the float again"
                           " \nEnter 2 to swim with the full air float\n",
                           "1", "2")
    if "1" == response:
        print_pause("the float was filled with air... Game over! ")
        connection()

    elif "2" == response:
        print_pause("Well done, You won, I'm happy to swim safely.")
        connection()


def order_project():
    intro()
    get_order()
    play_again()
    connection()
    order_again()
order_project()


# the end of programming this game
