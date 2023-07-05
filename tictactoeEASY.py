from tkinter import *
from tkinter import messagebox
from random import randint

# FOR EASY THE AI RANDOMLY CLICKS A BOX
#FOR MEDIUM THEY CHECK FOR TWO X OR OS NEXT TO EACH OTHER

root = Tk()
root.title("Brandon Atkinson - Tic-Tac-Toe")
root.geometry("1200x700")

player_character=""
ai_character=""
positions = ['-','-','-','-','-','-','-','-','-',]
turn=1
turns=0
game_over=False

Grid.rowconfigure(root, 2, weight=1)
Grid.rowconfigure(root, 5, weight=1)
Grid.rowconfigure(root, 6, weight=1)
Grid.rowconfigure(root, 7, weight=1)

Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 2, weight=1)

def check_game_over(positions):
    global game_over
    if positions[0] + positions[1] + positions[2] == 'XXX' or \
        positions[3] + positions[4] + positions[5]== 'XXX' or \
        positions[6] + positions[7] + positions[8]== 'XXX' or \
        positions[0] + positions[3] + positions[6]== 'XXX' or \
        positions[1] + positions[4] + positions[7]== 'XXX' or \
        positions[2] + positions[5] + positions[8]== 'XXX' or \
        positions[0] + positions[4] + positions[8]== 'XXX' or \
        positions[2] + positions[4] + positions[6]== 'XXX':
        game_over=True
        win_label=Label(root, text="X Wins!"). grid(row=8, column=0, columnspan=3)
    elif positions[0] + positions[1] + positions[2] == 'OOO' or \
        positions[3] + positions[4] + positions[5]== 'OOO' or \
        positions[6] + positions[7] + positions[8]== 'OOO' or \
        positions[0] + positions[3] + positions[6]== 'OOO' or \
        positions[1] + positions[4] + positions[7]== 'OOO' or \
        positions[2] + positions[5] + positions[8]== 'OOO' or \
        positions[0] + positions[4] + positions[8]== 'OOO' or \
        positions[2] + positions[4] + positions[6]== 'OOO':
        game_over=True
        win_label=Label(root, text="O Wins!"). grid(row=8, column=0, columnspan=3)
    else:
        game_over=False
    return game_over


def ai_turn():
    global turn
    global turns
    global positions
    global game_over
    while turn == 0 and turns <9 and game_over==False:
        ai_select = randint(0,8)
        if positions[ai_select] == "-":
            positions[ai_select] = ai_character
            if 0<=ai_select<=2:
                r=5
            elif 3<=ai_select<=5:
                r=6
            else:
                r=7

            if ai_select ==0 or ai_select == 3 or ai_select == 6:
                c=0
            elif ai_select ==1 or ai_select == 4 or ai_select == 7:
                c=1    
            else:
                c=2
            new_button = Button(root, text=positions[ai_select], font=("Helvetica", 20), bg="SystemButtonFace").grid(row=r, column=c , sticky="nesw")
            game_over=check_game_over(positions)
            turn = 1
            turns +=1


def x_select():
    global player_character
    global ai_character
    player_character="X"
    ai_character="O"
    player_select_label.config(text="You have selected "  + player_character)
    start_button= Button(root, text="Start Game", command=draw_board, font=("Helvetica", 20), bg="SystemButtonFace").grid(row=4,column=0, columnspan=3)


def o_select():
    global player_character
    global ai_character
    player_character="O"
    ai_character="X"
    player_select_label.config(text="You have selected "  + player_character)
    start_button= Button(root, text="Start Game", command=draw_board, font=("Helvetica", 20), bg="SystemButtonFace").grid(row=4,column=0, columnspan=3)

def player_pos(position):
    global turn
    global turns
    global positions
    global game_over
    if 0<=position<=2:
        r=5
    elif 3<=position<=5:
        r=6
    else:
        r=7

    if position ==0 or position == 3 or position == 6:
        c=0
    elif position ==1 or position == 4 or position == 7:
        c=1    
    else:
        c=2   

    if turn==1 and turns <9 and game_over==False: 
        if positions[position] == "-":
            positions[position] = player_character
            new_button = Button(root, text=positions[position], font=("Helvetica", 20), bg="SystemButtonFace").grid(row=r, column=c , sticky="nesw")
            game_over=check_game_over(positions)
            turn = 0
            turns +=1
            ai_turn()

def draw_board():
    global positions
    global turn
    global turns
    global game_over
    turn =1
    turns =0
    game_over=False

    positions = ['-','-','-','-','-','-','-','-','-',]
    t_l=Button(root, text=positions[0], font=("Helvetica", 20), bg="SystemButtonFace",command=lambda: player_pos(0)).grid(row=5,column=0, sticky="nesw")
    t_m=Button(root, text=positions[1], font=("Helvetica", 20), bg="SystemButtonFace",command=lambda: player_pos(1)).grid(row=5,column=1, sticky="nesw")
    t_r=Button(root, text=positions[2], font=("Helvetica", 20), bg="SystemButtonFace",command=lambda: player_pos(2)).grid(row=5,column=2, sticky="nesw")

    m_l=Button(root, text=positions[3], font=("Helvetica", 20), bg="SystemButtonFace",command=lambda: player_pos(3)).grid(row=6,column=0, sticky="nesw")
    m_m=Button(root, text=positions[4], font=("Helvetica", 20), bg="SystemButtonFace",command=lambda: player_pos(4)).grid(row=6,column=1, sticky="nesw")
    m_r=Button(root, text=positions[5], font=("Helvetica", 20), bg="SystemButtonFace",command=lambda: player_pos(5)).grid(row=6,column=2, sticky="nesw")

    b_l=Button(root, text=positions[6], font=("Helvetica", 20), bg="SystemButtonFace",command=lambda: player_pos(6)).grid(row=7,column=0, sticky="nesw")
    b_m=Button(root, text=positions[7], font=("Helvetica", 20), bg="SystemButtonFace",command=lambda: player_pos(7)).grid(row=7,column=1, sticky="nesw")
    b_r=Button(root, text=positions[8], font=("Helvetica", 20), bg="SystemButtonFace",command=lambda: player_pos(8)).grid(row=7,column=2, sticky="nesw") 

    win_label=Label(root, text="                                                 "). grid(row=8, column=0, columnspan=3)   

#widgets
main_label = Label(root, text="Brandon Atkinson - Tic-Tac-Toe!", font=("Helvetica", 20))
player_select_label = Label(root,text="Select: X or O", font=("Helvetica", 20))
x_button = Button(root, text="X", command=x_select, font=("Helvetica", 20), bg="SystemButtonFace")
o_button = Button(root, text="O", command=o_select, font=("Helvetica", 20), bg="SystemButtonFace")


#draw widgets on screen
main_label.grid(row=0, column=0, columnspan=3)
x_button.grid(row=2, column=0, sticky="ew")
o_button.grid(row=2, column=2, sticky="ew")

player_select_label.grid(row=1, column=0, columnspan=3)



root.mainloop()
