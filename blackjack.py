import tkinter as tk
import random
from tkinter.constants import CENTER, DISABLED
from typing import Text
from PIL import ImageTk, Image
#import PIL.ImageTk
#import PIL.Image
from tkinter import Entry, Label, PhotoImage, messagebox
#from tkinter import *
import time

i = 0


class Card:
    def __init__(self, value, photo, typer):
        self.value = value
        self.photo = photo
        self.typer = typer

    def show_card(self, master):
        card_photo = Image.open(self.photo)
        card_photo = card_photo.resize((100, 150), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(card_photo)
        img_label = tk.Label(master, image=img, borderwidth=0,bg="#3b8a38")
        img_label.image = img
        img_label.grid(column=i + 1, row=0, padx=10)


C2 = Card(2, "./images/2C.png", "normal")
D2 = Card(2, "./images/2D.png", "normal")
H2 = Card(2, "./images/2H.png", "normal")
S2 = Card(2, "./images/2S.png", "normal")

C3 = Card(3, "./images/3C.png", "normal")
D3 = Card(3, "./images/3D.png", "normal")
H3 = Card(3, "./images/3H.png", "normal")
S3 = Card(3, "./images/3S.png", "normal")

C4 = Card(4, "./images/4C.png", "normal")
D4 = Card(4, "./images/4D.png", "normal")
H4 = Card(4, "./images/4H.png", "normal")
S4 = Card(4, "./images/4S.png", "normal")

C5 = Card(5, "./images/5C.png", "normal")
D5 = Card(5, "./images/5D.png", "normal")
H5 = Card(5, "./images/5H.png", "normal")
S5 = Card(5, "./images/5S.png", "normal")

C6 = Card(6, "./images/6C.png", "normal")
D6 = Card(6, "./images/6D.png", "normal")
H6 = Card(6, "./images/6H.png", "normal")
S6 = Card(6, "./images/6S.png", "normal")

C7 = Card(7, "./images/7C.png", "normal")
D7 = Card(7, "./images/7D.png", "normal")
H7 = Card(7, "./images/7H.png", "normal")
S7 = Card(7, "./images/7S.png", "normal")

C8 = Card(8, "./images/8C.png", "normal")
D8 = Card(8, "./images/8D.png", "normal")
H8 = Card(8, "./images/8H.png", "normal")
S8 = Card(8, "./images/8S.png", "normal")

C9 = Card(9, "./images/9C.png", "normal")
D9 = Card(9, "./images/9D.png", "normal")
H9 = Card(9, "./images/9H.png", "normal")
S9 = Card(9, "./images/9S.png", "normal")

C10 = Card(10, "./images/10C.png", "normal")
D10 = Card(10, "./images/10D.png", "normal")
H10 = Card(10, "./images/10H.png", "normal")
S10 = Card(10, "./images/10S.png", "normal")

CJ = Card(10, "./images/JC.png", "normal")
DJ = Card(10, "./images/JD.png", "normal")
HJ = Card(10, "./images/JH.png", "normal")
SJ = Card(10, "./images/JS.png", "normal")

CQ = Card(10, "./images/QC.png", "normal")
DQ = Card(10, "./images/QD.png", "normal")
HQ = Card(10, "./images/QH.png", "normal")
SQ = Card(10, "./images/QS.png", "normal")

CK = Card(10, "./images/KC.png", "normal")
DK = Card(10, "./images/KD.png", "normal")
HK = Card(10, "./images/KH.png", "normal")
SK = Card(10, "./images/KS.png", "normal")

CA = Card(11, "./images/AC.png", "ace")
DA = Card(11, "./images/AD.png", "ace")
HA = Card(11, "./images/AH.png", "ace")
SA = Card(11, "./images/AS.png", "ace")

back = Card(0, "./images/purple_back.png", "back")

global player_score,verif_ace,chips
verif_ace=0
player_chips=500
dealer_chips=500
chips=0
name_text=" "
name=" "

def win():
    global window, dealer_frame, player_frame, cards, player_score, i, hit_bt, player_score_lb1, dealer_score_lb1, stand_bt, score_frame, verif_ace
    global player_chips, dealer_chips, chips, name,name_text
    verif_ace = 0
    player_score = 0
    dealer_score=0
    window = tk.Tk()
    window.geometry("900x600+600+200")
    window.configure(bg="#3b8a38")
    window.resizable(True, True)
    icon = ImageTk.PhotoImage(file="./images/blackjack.png")
    window.iconphoto(False, icon)
    window.title("Black Jack Game")

    cards = [C2, D2, H2, S2, C3, D3, H3, S3, C4, D4, H4, S4, C5, D5, H5, S5, C6, D6, H6, S6, C7, D7, H7, S7,
             C8, D8, H8, S8, C9, D9, H9, S9, C10, D10, H10, S10, CJ, DJ, HJ, SJ, CQ, DQ, HQ, SQ, CK, DK, HK, SK,
             CA, DA, HA, SA]

    # frames
    player_score = 0

    global settings_frame

    settings_frame = tk.Frame(
        window,
        #height=20,
        bg="#3b8a38"
        #bg="#302B2B"
    )
    settings_frame.pack(fill = "y", side = "right")

    score_frame = tk.Frame(
        window,
       # height=20,
        bg="#3b8a38"
    )
    score_frame.pack(fill = "y", side = "left")
    #score_frame.grid(row=100,column=0,padx=100,pady=100)


    dealer_frame = tk.Frame(
        window,
      #  height=20,
        bg="#3b8a38"
    )
    dealer_frame.pack(pady=20)

    empty_frame = tk.Frame(
        window,
      # height=40,
        bg="#3b8a38"
    )
    empty_frame.pack()

    player_frame = tk.Frame(
        window,
        bg="#3b8a38",
       # height=60
    )
    player_frame.pack(pady=30)

    global dealer_card
    i = 0
    dealer_card = random.choice(cards)
    cards.remove(dealer_card)
    dealer_card.show_card(dealer_frame)
    i = 1

    back.show_card(dealer_frame)
    if dealer_card.typer == "ace":
        dealer_card.value = 11
        decace = random.choice([1,11])
        if decace==1:
            dealer_card.value=1

    # scores
    dealer_score_lb1 = tk.Label(
        score_frame,
        text=f"Dealer's score: {dealer_card.value}",
        bg="#3b8a38",
        font=("Helvetica", 17)
    )
    dealer_score_lb1.grid(row=0, column=0)

    player_score_lb1 = tk.Label(
        score_frame,
        text=f"Your score {name}: 0 +",
        bg="#3b8a38",
        font=("Helvetica", 17)
    )
    player_score_lb1.grid(row=1, column=0, padx=0,pady=(100,100))

    dealer_score_lb1.config(text="Dealer's Score: " + str(dealer_card.value)+'\n'+"Dealer's chips: "+str(dealer_chips))
    player_score_lb1.config(text=f"Your Score {name}: " + str(player_score)+'\n'+f"Your chips {name}: "+str(player_chips))

    global chips_lb1
    chips_photo = Image.open("./images/chips3.png")
    chips_photo = chips_photo.resize((100, 150), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(chips_photo)
    
    '''
    chips_lb1 = tk.Label(
        settings_frame,
        image=img,
        text="Your bet ",
        bg="#3b8a38",
        font=("Helvetica", 17)
    )
    chips_lb1.grid(row=100, column=0, padx=0,pady=(100,100))
    '''
    

    # buttons
    change_bt = tk.Button(
        score_frame,
        text="Change Ace",
        command=change,
        relief=tk.FLAT,
        font=("Helvetica", 14),
        width=15,
        bg="#255AEA"
    )
    change_bt.grid(row=2, column=0, pady=2,padx=0)

    hit_bt = tk.Button(
        score_frame,
        text="Hit",
        command=hit,
        relief=tk.FLAT,
        font=("Helvetica", 14),
        width=15,
        bg="#255AEA"
    )
    hit_bt.grid(row=3, column=0, pady=2)

    stand_bt = tk.Button(
        score_frame,
        text="Stand",
        command=stand,
        relief=tk.FLAT,
        font=("Helvetica", 14),
        width=15,
        bg="#255AEA"
    )
    stand_bt.grid(row=4, column=0, pady=2)

    restart_bt = tk.Button(
        score_frame,
        text="Restart",
        command=restart,
        relief=tk.FLAT,
        font=("Helvetica", 14),
        width=15,
        #fg="#FFFFFF",
        bg="#77AAE8"
    )
    restart_bt.grid(row=5, column=0, pady=2)

    bet_bt = tk.Button(
        score_frame,
        text="Bet",
        command=bet,
        relief=tk.FLAT,
        font=("Helvetica", 14),
        width=15,
        bg="#DB2E2E"
    )
    bet_bt.grid(row=6, column=0, pady=2)

    name_bt = tk.Button(
        settings_frame,
        text="Name",
        command=changename,
        relief=tk.FLAT,
        font=("Helvetica", 14),
        width=15,
        bg="#8896B9"
    )
    name_bt.grid(row=7, column=10, pady=2)

    
    window.mainloop()

def hit():
    global i,player_score,verif_ace
    i = i + 1
    card = random.choice(cards)
    card.show_card(player_frame)
    cards.remove(card)
    #print(card.typer)

    if card.typer == "ace":
        if player_score<11:
            card.value = 11
            verif_ace += 1
        else:
            card.value=1
    player_score = player_score + card.value
    player_score_lb1.config(text=f"Your Score {name}: " + str(player_score)+'\n'+f"Your chips {name}: "+str(player_chips))

    if player_score > 21:
        messagebox.showinfo("Blackjack", "You lost, try again!")
        #player_chips -- dealer_chips ++
        hit_bt.config(state=tk.DISABLED)
        stand_bt.config(state=tk.DISABLED)
        youlose()

    if player_score == 21:
        stand()

def change():
    global player_score,verif_ace
    if verif_ace!=0:
        if verif_ace %2== 1:
        #print(1)
            player_score -= 10
            player_score_lb1["text"]=f"Your Score {name}: " + str(player_score)+'\n'+f"Your chips {name}: "+str(player_chips)
            verif_ace +=1
        else:
            player_score += 10
            player_score_lb1["text"]=f"Your Score {name}: " + str(player_score)+'\n'+f"Your chips {name}: "+str(player_chips)
            verif_ace +=1
    


def bet():
    #open a window
    
    windowbet = tk.Tk()
    windowbet.geometry("500x500+800+250")
    windowbet.configure(bg="#302B2B")
    windowbet.resizable(True, True)
    windowbet.iconphoto = ImageTk.PhotoImage(file="./images/aces.png")
    #windowbet.iconphoto(False, iconphoto)
    windowbet.title("Betting")
    number=0
    
    def bet_command():
        global number,chips,player_chips,dealer_chips
        number=entry1.get()
        print(number)
        
        chips=int(number)
        if chips>=player_chips or chips>=dealer_chips:
            chips=min(player_chips,dealer_chips)

        
        '''
        global chips_lb1
        chips_lb1 = tk.Label (image=img, borderwidth=0,bg="#3b8a38")
        chips_lb1.image = img
        chips_lb1.p()
        #img_label.grid(column=i + 1, row=0, padx=10)
        '''


        return None

    entry1=Entry(windowbet,width=50)
    entry1.pack(padx=50,pady=50)
    
    Bet_bt = tk.Button(
        windowbet,
        text="Bet",
        #command=windowbet.configure(),
        #commnad=windowbet.config(state=tk.DISABLED),
        command=bet_command,
        relief=tk.FLAT,
        font=("Helvetica", 12),
        width=15,
        bg="#DB2E2E"
    )
    Bet_bt.pack()
    #Bet_bt.grid(row=6, column=0, pady=2)
    print(number)

    #player writes number
    

def changename():
    
    #open a frame
    windowname = tk.Tk()
    windowname.geometry("500x500+800+250")
    windowname.configure(bg="#302B2B")
    windowname.resizable(True, True)
    windowname.iconphoto = ImageTk.PhotoImage(file="./images/aces.png")
    #windowbet.iconphoto(False, iconphoto)
    windowname.title("Name")
    #enter name

    def name_command():
        global name_text,name
        name_text=entry1.get()
        print(name_text)
        name=name_text
        player_score_lb1.config(text=f"Your Score {name}: " + str(player_score)+'\n'+f"Your chips {name}: "+str(player_chips))
        return None

    entry1=Entry(windowname,width=50)
    entry1.pack(padx=50,pady=50)
    
    name_bt = tk.Button(
        windowname,
        text="Name",
        #command=windowbet.configure(),
        #commnad=windowbet.config(state=tk.DISABLED),
        command=name_command,
        relief=tk.FLAT,
        font=("Helvetica", 12),
        width=15,
        bg="#8896B9"
    )
    name_bt.pack()
    

global decision
decision=1    

def stand():
    hit_bt.config(state=tk.DISABLED)
    global i,dealer_chips,player_chips,decision,decace,dealer_score,dealer_card2,dealer_card3
    i = 1
    dealer_card2 = random.choice(cards)
    cards.remove(dealer_card2)
    dealer_card2.show_card(dealer_frame)
    dealer_score = dealer_card.value

    if dealer_card2.typer == "ace" and dealer_score < 11:
        dealer_card2.value == 11
        decace = random.choice([1,11])
        if decace==1:
            dealer_card2.value=1
   
    print(dealer_card2.value)

    
    dealer_score = dealer_score + dealer_card2.value
    print(dealer_score)
    dealer_score_lb1.config(text="Dealer's Score: " + str(dealer_score)+'\n'+"Dealer's chips: "+str(dealer_chips))
    player_score_lb1.config(text=f"Your Score {name}: " + str(player_score)+'\n'+f"Your chips {name}: "+str(player_chips))

    while dealer_score < 21 and decision==1:
        i = i + 1
        #random hit or stand
        if(dealer_score>14):
            decision = random.choice([1,2])
        #print(decision,dealer_score)
        if decision==1:
            dealer_card3 = random.choice(cards)
            cards.remove(dealer_card3)
            dealer_card3.show_card(dealer_frame)
            if dealer_card3.typer == "ace" and dealer_score < 11:
               dealer_card3.value == 11
               decace = random.choice([1,11])
               if decace==1:
                  dealer_card3.value=1
            dealer_score = dealer_score + dealer_card3.value
            dealer_score_lb1.config(text="Dealer's Score: " + str(dealer_score)+'\n'+"Dealer's chips: "+str(dealer_chips))

    if dealer_score > 21:
        messagebox.showinfo("Blackjack", "Congratulations, you won!")
        player_chips+=chips
        dealer_chips-=chips
        dealer_score_lb1.config(text="Dealer's Score: " + str(dealer_score)+'\n'+"Dealer's chips: "+str(dealer_chips))
        player_score_lb1.config(text=f"Your Score {name}: " + str(player_score)+'\n'+f"Your chips {name}: "+str(player_chips))
        #player_chips++ dealer_chips--
        youwin()

    elif dealer_score == player_score:
        messagebox.showinfo("Blackjack", "It is draw, money will split!")
        #player_chips dealer_chips

    elif dealer_score > player_score:
        messagebox.showinfo("Blackjack", "You lost, try again!")
        #player_chips-- dealer_chips++
        player_chips-=chips
        dealer_chips+=chips
        dealer_score_lb1.config(text="Dealer's Score: " + str(dealer_score)+'\n'+"Dealer's chips: "+str(dealer_chips))
        player_score_lb1.config(text=f"Your Score {name}: " + str(player_score)+'\n'+f"Your chips {name}: "+str(player_chips))
        youlose()
    elif dealer_score < player_score:
        messagebox.showinfo("You won, congratulations!")
        #player_chips++ dealer_chips--
        player_chips+=chips
        dealer_chips-=chips
        dealer_score_lb1.config(text="Dealer's Score: " + str(dealer_score)+'\n'+"Dealer's chips: "+str(dealer_chips))
        player_score_lb1.config(text=f"Your Score {name}: " + str(player_score)+'\n'+f"Your chips {name}: "+str(player_chips))
        youwin()
    stand_bt.config(state=tk.DISABLED)

def youwin():
    windowwin = tk.Toplevel(window)
    windowwin.geometry("400x500+600+200")
    windowwin.configure(bg="#FFFFFF")
    windowwin.resizable(True, True)
    img=ImageTk.PhotoImage(Image.open("./images/youwin.jpg"))
    windowwin.iconphoto = ImageTk.PhotoImage(file="./images/youwin.jpg")
    windowwin.title("You win")
    lb1=tk.Label(windowwin,image=img)
    lb1.image=img
    lb1.pack()

def youlose():
    windowlose = tk.Toplevel(window)
    windowlose.geometry("400x500+600+200")
    windowlose.configure(bg="#BBBBBB")
    windowlose.resizable(True, True)
    img=ImageTk.PhotoImage(Image.open("./images/youlose.jpg"))
    windowlose.iconphoto = ImageTk.PhotoImage(file="./images/youlose.jpg")
    windowlose.title("You lost")
    label1=tk.Label(windowlose,image=img)
    label1.image=img
    label1.pack()

def restart():
    window.destroy()
    win()


win()
