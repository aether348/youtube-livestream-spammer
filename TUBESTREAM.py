import pyautogui as auto
import time
import random
import os


ascii_banner = r"""
 _________  ___  ___  ________  _______   ________  _________  ________  _______   ________  _____ ______      
|\___   ___\\  \|\  \|\   __  \|\  ___ \ |\   ____\|\___   ___\\   __  \|\  ___ \ |\   __  \|\   _ \  _   \    
\|___ \  \_\ \  \\\  \ \  \|\ /\ \   __/|\ \  \___|\|___ \  \_\ \  \|\  \ \   __/|\ \  \|\  \ \  \\\__\ \  \   
     \ \  \ \ \  \\\  \ \   __  \ \  \_|/_\ \_____  \   \ \  \ \ \   _  _\ \  \_|/_\ \   __  \ \  \\|__| \  \  
      \ \  \ \ \  \\\  \ \  \|\  \ \  \_|\ \|____|\  \   \ \  \ \ \  \\  \\ \  \_|\ \ \  \ \  \ \  \    \ \  \ 
       \ \__\ \ \_______\ \_______\ \_______\____\_\  \   \ \__\ \ \__\\ _\\ \_______\ \__\ \__\ \__\    \ \__\
        \|__|  \|_______|\|_______|\|_______|\_________\   \|__|  \|__|\|__|\|_______|\|__|\|__|\|__|     \|__|
                                            \|_________|                                                    
"""

os.system("color e")
print(ascii_banner)
print("_________________________________________________________________")
print("                                         |1.Custom Text Spammer |")
print("                                         |2.Custom List Spammer |")
print("                                         |3.Premade Text Spammer|")
print("                                         |4.Premade List Spammer|")
print("                                         |                      |")
print("                                         |______________________|")
option_select = input("user@[TUBESTREAM]> ")

def get_delay():
    while True:
        try:
            delay = float(input("Enter time between each message typed (in seconds): "))
            if delay < 0.01:
                print("Too short! Please enter a value >= 0.01")
            else:
                return delay
        except ValueError:
            print("Invalid number. Try again.")

def start_spam(messages, delay):
    print("You have 5 seconds to click an input bar!")
    time.sleep(5)
    while True:
        auto.write(random.choice(messages) if isinstance(messages, list) else messages)
        auto.press('enter')
        time.sleep(delay)

if option_select == "1":
    text = input("Enter text for the spam: ")
    delay = get_delay()
    start_spam(text, delay)

elif option_select == "2":
    final_list = [
        input("Enter custom list item 1: "),
        input("Enter custom list item 2: "),
        input("Enter custom list item 3: "),
        input("Enter custom list item 4: "),
        input("Enter custom list item 5: ")
    ]
    delay = get_delay()
    start_spam(final_list, delay)

elif option_select == "3":
    delay = get_delay()
    start_spam("HACKED!!!", delay)

elif option_select == "4":
    premade_list = ['spammed on', 'Hacked!!!', 'spammed', 'hahahahaha!!!!']
    delay = get_delay()
    start_spam(premade_list, delay)

else:
    print("Invalid option selected.")