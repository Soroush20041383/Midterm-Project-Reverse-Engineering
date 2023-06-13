from tkinter import *
from random import randint
from tkinter import ttk



root = Tk()
root.title('Codemy.com - Rock, Paper, Scissors, Lizard, Spock')
# root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x600") # what does it do
# Change bg color to white \
root.config(bg="white")

# Define our images
rock = PhotoImage(file='C:\\Users\\Soroush\\Downloads\\Rock.png')
paper = PhotoImage(file='C:\\Users\\Soroush\\Downloads\\Paper.png')
scissors = PhotoImage(file='C:\\Users\\Soroush\\Downloads\\Scissors.png')
lizard = PhotoImage(file='C:\\Users\\Soroush\\Downloads\\Lizard.png')
spock = PhotoImage(file='C:\\Users\\Soroush\\Downloads\\Spock.png')
# Add Images to a list
image_list = [rock, paper, scissors, lizard, spock]

# Pick random number between 0 and 4
pick_number = randint(0, 4)

# Throw up an image when the programs starts
image_label = Label(root, image=image_list[pick_number], bd=0)
image_label.pack(pady=20)

# Create Spin Function
def spin():
    # Pick random number
    pick_number = randint(0, 4)
    # Show Image
    image_label.config(image=image_list[pick_number])

    # 0 = Rock
    # 1 = Paper
    # 2 = Scissors
    # 3 = Lizard
    # 4 = Spock

    # Convert Dropdown choice to a number
    if user_choice.get() == "Rock":
        user_choice_value = 0
    elif user_choice.get() == "Paper":
        user_choice_value = 1
    elif user_choice.get() == "Scissors":
        user_choice_value = 2
    elif user_choice.get() == "Lizard":
        user_choice_value = 3
    elif user_choice.get() == "Spock":
        user_choice_value = 4

    # Determine if we won or lost
    if user_choice_value == 0: # Rock
        if pick_number == 0:
            win_lose_label.config(text="It's a tie! Spin again...")
        elif pick_number == 1: # Paper
            win_lose_label.config(text="Paper covers Rock! You lose...")
        elif pick_number == 2: # Scissors
            win_lose_label.config(text="Rock crushes Scissors! You win...")
        elif pick_number == 3: # Lizard
            win_lose_label.config(text="Rock crushes Lizard! You win...")
        elif pick_number == 4: # Spock
            win_lose_label.config(text="Spock vaporizes Rock! You lose...")

    elif user_choice_value == 1: # Paper
        if pick_number == 0: # Rock
            win_lose_label.config(text="Paper covers Rock! You win...")
        elif pick_number == 1:
            win_lose_label.config(text="It's a tie! Spin again...")
        elif pick_number == 2: # Scissors
            win_lose_label.config(text="Scissors cuts Paper! You lose...")
        elif pick_number == 3: # Lizard
            win_lose_label.config(text="Lizard eats Paper! You lose...")
        elif pick_number == 4: # Spock
            win_lose_label.config(text="Paper disproves Spock! You win...")

    elif user_choice_value == 2: # Scissors
        if pick_number == 0: # Rock
            win_lose_label.config(text="Rock crushes Scissors! You lose...")
        elif pick_number == 1: # Paper
            win_lose_label.config(text="Scissors cuts Paper! You win...")
        elif pick_number == 2:
            win_lose_label.config(text="It's a tie! Spin again...")
        elif pick_number == 3: # Lizard
            win_lose_label.config(text="Scissors decapitates Lizard! You win...")
        elif pick_number == 4: # Spock
            win_lose_label.config(text="Spock smashes Scissors! You lose...")

    elif user_choice_value == 3: # Lizard
        if pick_number == 0: # Rock
            win_lose_label.config(text="Rock crushes Lizard! You lose...")
        elif pick_number == 1: # Paper
            win_lose_label.config(text="Lizard eats Paper! You win...")
        elif pick_number == 2: # Scissors
            win_lose_label.config(text="Scissors decapitates Lizard! You lose...")
        elif pick_number == 3:
            win_lose_label.config(text="It's a tie! Spin again...")
        elif pick_number == 4: # Spock
            win_lose_label.config(text="Lizard poisons Spock! You win...")

    elif user_choice_value == 4: # Spock
        if pick_number == 0: # Rock
            win_lose_label.config(text="Spock vaporizes Rock! You win...")
        elif pick_number == 1: # Paper
            win_lose_label.config(text="Paper disproves Spock! You lose...")
        elif pick_number == 2: # Scissors
            win_lose_label.config(text="Spock smashes Scissors! You win...")
        elif pick_number == 3: # Lizard
            win_lose_label.config(text="Lizard poisons Spock! You lose...")
        elif pick_number == 4:
            win_lose_label.config(text="It's a tie! Spin again...")

#Create a Dropdown
options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
user_choice = ttk.Combobox(root, value=options)
user_choice.current(0)
user_choice.pack(pady=20)

#Create Spin Button
spin_button = Button(root, text="Spin!", command=spin)
spin_button.pack(pady=20)

#Create a label to display if you won or lost
win_lose_label = Label(root, text="", font=("Helvetica", 18), bg="white")
win_lose_label.pack(pady=50)

#Run tkinter mainloop
root.mainloop()