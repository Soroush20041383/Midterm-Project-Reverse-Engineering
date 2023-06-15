from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Codemy.com - Tic Tac Toe')
# root.iconbitmap()
# root.geometry("1200x710")


# X starts so true
clicked = True
count = 0


# Start the game over!
def reset():
    pass


# disable all buttons
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)
    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)
    b16.config(state=DISABLED)


# Check to see if someone won
def checkifwon():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" and b4["text"] == "X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        b4.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS X Wins!")
        disable_all_buttons()
    elif b5["text"] == "X" and b6["text"] == "X" and b7["text"] == "X" and b8["text"] == "X":
        b5.config(bg="red")
        b6.config(bg="red")
        b7.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS X Wins!")
        disable_all_buttons()








    elif b9["text"] == "X" and b10["text"] == "X" and b11["text"] == "X" and b12["text"] == "X":
        b9.config(bg="red")
        b10.config(bg="red")
        b11.config(bg="red")
        b12.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS X Wins!")
        disable_all_buttons()








    elif b13["text"] == "X" and b14["text"] == "X" and b15["text"] == "X" and b16["text"] == "X":
        b13.config(bg="red")
        b14.config(bg="red")
        b15.config(bg="red")
        b16.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS X Wins!")
        disable_all_buttons()








    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" and b13["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        b13.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS X Wins!")
        disable_all_buttons()








    elif b2["text"] == "X" and b6["text"] == "X" and b10["text"] == "X" and b14["text"] == "X":
        b2.config(bg="red")
        b6.config(bg="red")
        b10.config(bg="red")
        b14.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRADUALTION X Wins!")
        disable_all_buttons()








    elif b3["text"] == "X" and b7["text"] == "X" and b11["text"] == "X" and b15["text"] == "X":
        b3.config(bg="red")
        b7.config(bg="red")
        b11.config(bg="red")
        b15.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRADUALTION X Wins!")
        disable_all_buttons()








    elif b4["text"] == "X" and b8["text"] == "X" and b12["text"] == "X" and b16["text"] == "X":
        b4.config(bg="red")
        b8.config(bg="red")
        b12.config(bg="red")
        b16.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRADUALTION X Wins!")
        disable_all_buttons()




    elif b1["text"] == "X" and b6["text"] == "X" and b11["text"] == "X" and b16["text"] == "X":
        b1.config(bg="red")
        b6.config(bg="red")
        b11.config(bg="red")
        b16.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRADUALTION X Wins!")
        disable_all_buttons()








    elif b4["text"] == "X" and b7["text"] == "X" and b10["text"] == "X" and b13["text"] == "X":
        b4.config(bg="red")
        b7.config(bg="red")
        b10.config(bg="red")
        b13.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRADUALTION X Wins!")
        disable_all_buttons()






    ####Check for O'S WIN
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" and b4["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        b4.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS O Wins!")
        disable_all_buttons()
    elif b5["text"] == "O" and b6["text"] == "O" and b7["text"] == "O" and b8["text"] == "O":
        b5.config(bg="red")
        b6.config(bg="red")
        b7.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS O Wins!")
        disable_all_buttons()








    elif b9["text"] == "O" and b10["text"] == "O" and b11["text"] == "O" and b12["text"] == "O":
        b9.config(bg="red")
        b10.config(bg="red")
        b11.config(bg="red")
        b12.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS O Wins!")
        disable_all_buttons()








    elif b13["text"] == "O" and b14["text"] == "O" and b15["text"] == "O" and b16["text"] == "O":
        b13.config(bg="red")
        b14.config(bg="red")
        b15.config(bg="red")
        b16.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS O Wins!")
        disable_all_buttons()








    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O" and b13["text"] == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        b13.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS O Wins!")
        disable_all_buttons()








    elif b2["text"] == "O" and b6["text"] == "O" and b10["text"] == "O" and b14["text"] == "O":
        b2.config(bg="red")
        b6.config(bg="red")
        b10.config(bg="red")
        b14.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRADUALTION O Wins!")
        disable_all_buttons()








    elif b3["text"] == "O" and b7["text"] == "O" and b11["text"] == "O" and b15["text"] == "O":
        b3.config(bg="red")
        b7.config(bg="red")
        b11.config(bg="red")
        b15.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRADUALTION O Wins!")
        disable_all_buttons()








    elif b4["text"] == "O" and b8["text"] == "O" and b12["text"] == "O" and b16["text"] == "O":
        b4.config(bg="red")
        b8.config(bg="red")
        b12.config(bg="red")
        b16.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRADUALTION O Wins!")
        disable_all_buttons()




    elif b1["text"] == "O" and b6["text"] == "O" and b11["text"] == "O" and b16["text"] == "O":
        b1.config(bg="red")
        b6.config(bg="red")
        b11.config(bg="red")
        b16.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRADUALTION O Wins!")
        disable_all_buttons()








    elif b4["text"] == "O" and b7["text"] == "O" and b10["text"] == "O" and b13["text"] == "O":
        b4.config(bg="red")
        b7.config(bg="red")
        b10.config(bg="red")
        b13.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRADUALTION O Wins!")
        disable_all_buttons()


# Button clicked function
def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkifwon()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\n pick another box...")


# Start the game over!
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16
    global clicked, count
    clicked = True
    count = 0
    # build our buttons
    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="purple", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="purple", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="purple", command=lambda: b_click(b3))
    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="purple", command=lambda: b_click(b4))

    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="purple", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="purple", command=lambda: b_click(b6))
    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="purple", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="purple", command=lambda: b_click(b8))

    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="purple", command=lambda: b_click(b9))
    b10 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="purple", command=lambda: b_click(b10))
    b11 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="purple", command=lambda: b_click(b11))
    b12 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="purple", command=lambda: b_click(b12))

    b13 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="purple", command=lambda: b_click(b13))
    b14 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="purple", command=lambda: b_click(b14))
    b15 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="purple", command=lambda: b_click(b15))
    b16 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="purple", command=lambda: b_click(b16))

    # Grid our buttons to the screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=0, column=3)

    b5.grid(row=1, column=0)
    b6.grid(row=1, column=1)
    b7.grid(row=1, column=2)
    b8.grid(row=1, column=3)

    b9.grid(row=2, column=0)
    b10.grid(row=2, column=1)
    b11.grid(row=2, column=2)
    b12.grid(row=2, column=3)

    b13.grid(row=3, column=0)
    b14.grid(row=3, column=1)
    b15.grid(row=3, column=2)
    b16.grid(row=3, column=3)


# Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

reset()

root.mainloop()