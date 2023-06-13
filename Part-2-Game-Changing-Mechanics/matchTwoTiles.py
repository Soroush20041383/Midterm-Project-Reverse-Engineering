from tkinter import *
import random
from tkinter import messagebox

random.seed(42)
root = Tk()
root.title('Codemy.com - Match Game!')
#root.iconbitmap()
root.geometry("500x600")

global winner, matches, score
#Set Winner counter to 0
winner = 0
score = 0

#Create our matches
matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]

#Shuffle our matches
random.shuffle(matches)

# Create button frame
my_frame = Frame(root)
my_frame.pack(pady=10)

# Define some variables
count = 0
answer_list = []
answer_dict = {}

# Reset the Game
def reset():
    global matches, winner
    winner = 0
    # Create our matches
    matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]
    # Shuffle our matches
    random.shuffle(matches)

    # Reset label
    my_label.config(text="")

    # Rseset our tiles
    button_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15]
    # Loop thru buttons and change colors
    for button in button_list:
        button.config(text=" ",bg="SystemButtonFace", state="normal")


#Create winner function
def win():
    scoreboard_label.config(text = "Score: " + str(score))
    my_label.config(text="congradualtions! You Win!!!")
    button_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15]
    # Loop thru buttons and change colors
    for button in button_list:
        button.config(bg="yellow")

def button_click(b, number):
    global count, answer_list, answer_dict, winner, score

    if b["text"] == ' ' and count < 2:
        b["text"] = matches[number]
        # Add number to answer list
        answer_list.append(number)
        # add button and number to Answer Dictionary
        answer_dict[b] = matches[number]
        # Incerement our counter
        count += 1
        print(answer_dict)

    # Start to determine correct or not
    if len(answer_list) == 2:
        if matches[answer_list[0]] == matches[answer_list[1]]:
            my_label.config(text="MATCH!")
            score += int(matches[answer_list[0]])
            print(score)
            scoreboard_label.config(text= f"Score= {score}")
            for key in answer_dict:
                key["state"] = "disabled"
            count = 0
            answer_list = []
            answer_dict = {}
            #Increment our winner counter
            winner += 1
            if winner == 8:
                win()
        else:
            #my_label.config(text="DOH!")
            count = 0
            answer_list = []
            # pop up bow
            messagebox.showinfo("Incorrect!", "Incorrect")

            #Reset the buttons
            for key in answer_dict:
                key["text"] = " "

            answer_dict = {}



#Define our buttons
b0 = Button(my_frame, text=" ", font=("helvetica",20), height=3, width=6,command=lambda: button_click(b0, 0), relief="groove", bg="light blue")
b1 = Button(my_frame, text=" ", font=("helvetica",20), height=3, width=6,command=lambda: button_click(b1, 1), relief="groove", bg="light blue")
b2 = Button(my_frame, text=" ", font=("helvetica",20), height=3, width=6,command=lambda: button_click(b2, 2), relief="groove", bg="light blue")
b3 = Button(my_frame, text=" ", font=("helvetica",20), height=3, width=6,command=lambda: button_click(b3, 3), relief="groove", bg="light blue")
b4 = Button(my_frame, text=" ", font=("helvetica",20), height=3, width=6,command=lambda: button_click(b4, 4), relief="groove", bg="light blue")
b5 = Button(my_frame, text=" ", font=("helvetica",20), height=3, width=6,command=lambda: button_click(b5, 5), relief="groove", bg="light blue")
b6 = Button(my_frame, text=" ", font=("helvetica",20), height=3, width=6,command=lambda: button_click(b6, 6), relief="groove", bg="light blue")
b7 = Button(my_frame, text=" ", font=("helvetica",20), height=3, width=6,command=lambda: button_click(b7, 7), relief="groove", bg="light blue")
b8 = Button(my_frame, text=" ", font=("helvetica",20), height=3, width=6,command=lambda: button_click(b8, 8), relief="groove", bg="light blue")
b9 = Button(my_frame, text=" ", font=("helvetica",20), height=3, width=6,command=lambda: button_click(b9, 9), relief="groove", bg="light blue")
b10 = Button(my_frame, text=" ", font=("helvetica",20), height=3, width=6,command=lambda: button_click(b10, 10), relief="groove", bg="light blue")
b11 = Button(my_frame, text=" ", font=("helvetica",20), height=3, width=6,command=lambda: button_click(b11, 11), relief="groove", bg="light blue")
b12 = Button(my_frame, text=" ", font=("helvetica",20), height=3, width=6,command=lambda: button_click(b12, 12), relief="groove", bg="light blue")
b13 = Button(my_frame, text=" ", font=("helvetica",20), height=3, width=6,command=lambda: button_click(b13, 13), relief="groove", bg="light blue")
b14 = Button(my_frame, text=" ", font=("helvetica",20), height=3, width=6,command=lambda: button_click(b14, 14), relief="groove", bg="light blue")
b15 = Button(my_frame, text=" ", font=("helvetica",20), height=3, width=6,command=lambda: button_click(b15, 15), relief="groove", bg="light blue")


#Grid our Butoons
b0.grid(row=0,column=0)
b1.grid(row=0,column=1)
b2.grid(row=0,column=2)
b3.grid(row=0,column=3)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=1,column=3)

b8.grid(row=2,column=0)
b9.grid(row=2,column=1)
b10.grid(row=2,column=2)
b11.grid(row=2,column=3)

b12.grid(row=3,column=0)
b13.grid(row=3,column=1)
b14.grid(row=3,column=2)
b15.grid(row=3,column=3)

my_label = Label(root, text="")
my_label.pack(pady=20)


# Create a menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Craete an Options Dropdown Menu
option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Reset Game", command=reset)
option_menu.add_separator()
option_menu.add_command(label="Exit Game", command=root.quit)

# Create a label for the scoreboard
scoreboard_label = Label(root, text="Score: 0")
scoreboard_label.pack()


# Run the window
root.mainloop()


