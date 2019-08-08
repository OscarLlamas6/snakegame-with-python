import curses #import the curses library
import curses.textpad
import random
import csv
import os
import DoublyLinkedCircularList
from DoublyLinkedCircularList import *
import DoublyLinkedListV2
from DoublyLinkedListV2 import *
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, KEY_ENTER #import special KEYS from the curses library

player = "" #Username playing
score = 0 #Score count
users = ListaCircularDoble()  #List of usernames
snake = ListaDoble() #Snake body structure handler
speed = 100 #Timeout paramete(speed)
pypath =os.path.dirname(os.path.abspath(__file__)) #Relative path of .py file
snake.agregar_final(10,12)
snake.agregar_final(10,11)
snake.agregar_final(10,10)
snackx = 1
snacky = 1
tipo = 1
new_snack = True

def bulk_csv(filename):
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        count = 0
        for line in csv_reader:
            if count>0:                
                users.agregar_final(line[0])
            count = count + 1
           
def paint_title(win,title):                     
    x_start = round((70-len(title))/2)    
    win.addstr(0,x_start,title)

def paint_gametitle(win):
    global player
    global score
    x_start = round((70-len(" SNAKE RELOADED "))/2)
    win.addstr(0,x_start," SNAKE RELOADED ")
    user_x = round((68-len(" User: "+player+" ")))
    win.addstr(0,user_x," User: "+player+" ")

def paint_score(win):
    win.addstr(0,2," Score:"+str(score)+" ")


def paint_mycode(win,code):                  
    x_start = round((70-len(code))/2)    
    win.addstr(24,x_start,code)    

def paint_bulk(win):
    win.clear()
    win.border(0) 
    paint_title(win,"BULK LOADING")
    win.addstr(5,20,"↓ Please enter .csv file name ↓")
    win.addstr(10,15,"________________________________________")
    win.addstr(11,22,"Press ENTER to end typing")
    win.refresh()

def paint_reports(win):
    win.clear()
    win.border(0) 
    paint_title(win,"REPORTS")
    win.refresh()

def paint_playgame(win):
    win.clear()
    win.border(0)
    paint_gametitle(win)
    win.refresh()

def paint_userselection(win):
    win.clear()
    win.border(0) 
    paint_title(win,"USER SELECTION")
    win.addstr(5,20,"Please select your username")
    win.addstr(23,10,"Press ESC to cancel  |  Press ENTER to choose username")
    win.refresh()

def paint_scoreboard(win):
    win.clear()
    win.border(0) 
    paint_title(win,"Scoreboard")
    win.refresh()


def paint_menu(win):
    win.clear()
    win.border(0) 
    pos_x = 27              #initial x position
    pos_y = 9                #initial y position
    paint_title(win,"MAIN MENU")
    win.addstr(pos_y,pos_x,"1. Play") 
    win.addstr(pos_y+1,pos_x,"2. Scoreboard")  
    win.addstr(pos_y+2,pos_x,"3. User Selection")
    win.addstr(pos_y+3,pos_x,"4. Reports")
    win.addstr(pos_y+4,pos_x,"5. Bulk Loading")
    win.addstr(pos_y+5,pos_x,"6. Close Game")
    paint_mycode(win,"201602625") 
    win.refresh()
    win.timeout(-1)

def paint_username(win, name):
    username = "<-       "+name+"       ->"
    x_start = round((70-len(username))/2)
    win.addstr(10,x_start,username)
    win.refresh()

def check_coordinate():
    global snake
    global snackx
    global snacky
    xy_exists = False
    nodotemp = snake.primero
    while nodotemp is not None:
        if nodotemp.y == snacky and nodotemp.x == snackx:
            xy_exists = True
        nodotemp = nodotemp.siguiente
    if xy_exists:
        return True
    else:
        return False

def generate_coordinate():
    global snackx
    global snacky
    snacky = random.randint(1,23)
    snackx = random.randint(1,68)
    if check_coordinate():
        generate_coordinate   

def paint_snacks(win):
    global snackx
    global snacky
    generate_coordinate()
    win.addch(snacky,snackx,'+')
    win.refresh()


def start_game(win): #Method to start game
    global snake 
    global score
    global snackx
    global snake
    headx = 0
    heady = 0
    key1 = KEY_RIGHT
    nodoaux = snake.primero
    while nodoaux is not None:
        win.addch(nodoaux.y, nodoaux.x, '#')
        nodoaux = nodoaux.siguiente
    paint_snacks(win)
    while key1!=27:
        win.timeout(speed)
        keychange = window.getch()
        if keychange is not -1:
            key1 = keychange
        if key1 == KEY_RIGHT:
            heady = 0
            headx = 1
        elif key1 == KEY_LEFT:
            heady = 0
            headx = -1
        elif key1 == KEY_UP:
            heady = -1
            headx = 0
        elif key1 == KEY_DOWN:
            heady = 1
            headx = 0       
        aux = snake.primero
        tempy = 0
        tempx = 0
        if aux is snake.primero:
            headposy = aux.y+heady
            headposx = aux.x+headx
            if headposy == 24:
                headposy = 1
            if headposy == 0:
                headposy = 23
            if headposx == 69:
                headposx = 1
            if headposx == 0:
                headposx = 68          
            win.addch(aux.y,aux.x,' ') 
            win.addch(headposy,headposx,'0')
            tempy = aux.y 
            tempx = aux.x
            aux.y = headposy
            aux.x = headposx
            if aux.y==snacky and aux.x==snackx:
                paint_snacks(win)
            aux = aux.siguiente
        while aux is not None:
            win.addch(aux.y,aux.x,' ')
            win.addch(tempy,tempx,'#')
            newy = aux.y
            newx = aux.x
            aux.y = tempy
            aux.x = tempx
            tempy = newy
            tempx = newx
            aux = aux.siguiente       
        win.refresh()  
    
    paint_menu(win) 

def start_scoreboard(win):
    key2 = -1
    while key2!=27:
        key2 = window.getch()
    paint_menu(win) 

def start_userselection(win):
    global player
    nodoaux = users.primero
    if nodoaux is not None:
        paint_username(win,str(nodoaux.dato))        
    else:
        win.addstr(10,20,"No hay usuario(s) registrado(s)")
    key3 = -1
    while key3!=27:
        key3 = window.getch()
        if key3 == KEY_RIGHT:
            nodoaux = nodoaux.siguiente
            paint_userselection(win)
            paint_username(win,str(nodoaux.dato))
            key3 = -1
        if key3 == KEY_LEFT:
            nodoaux = nodoaux.anterior
            paint_userselection(win)
            paint_username(win,str(nodoaux.dato))
            key3 = -1
        if key3 == 10:
            if nodoaux is not None:
                player = str(nodoaux.dato)
            key3 = 27
        
    paint_menu(win)   

def start_reports(win):
    key4 = -1
    while key4!=27:
        key4 = window.getch()
    paint_menu(win) 

def start_bulk(win):
    path = ""
    win2 = curses.newwin(1,40,9,15)
    tb = curses.textpad.Textbox(win2, insert_mode=True)
    text = tb.edit()
    path = pypath+"\\"+tb.gather()
    path = path[:-1]
    win.refresh()
    count = 22
    while count <= 48:
        win.addstr(11,count," ")
        count = count + 1
    win.addstr(23,10,"Press ESC to cancel  |  Press ENTER to bulk data")
    win.refresh()
    key5 = -1
    while key5!=27:
        key5 = window.getch()
        if key5 == 10:
            bulk_csv(path)
            key5 = 27
    paint_menu(win)  
    
stdscr = curses.initscr() #initialize console
height = 25
width = 70
pos_y = 0
pos_x = 0
window = curses.newwin(height,width,pos_y,pos_x) #create a new curses window
window.keypad(True)     #enable Keypad mode
curses.noecho()         #prevent input from displaying in the screen
curses.curs_set(0)      #cursor invisible (0)
window.border(0)
window.nodelay(True)    #return -1 when no key is pressed
paint_menu(window)
key = -1
while key == -1:                #run program while [ESC] key is not pressed
    key = window.getch()  #get current key being pressed

    if key == 49:
        paint_playgame(window)
        paint_score(window)
        window.refresh()
        start_game(window)
        key = -1

    elif key == 50:     #Shows scoreboard
        paint_scoreboard(window)
        window.refresh()
        start_scoreboard(window)
        key = -1

    elif key == 51:   #Starts User selection
        paint_userselection(window)
        window.refresh()  
        start_userselection(window)
        key = -1
    
    elif key == 52: #Shows Reports Menu
        paint_reports(window)
        window.refresh()
        start_reports(window)
        key = -1

    elif key == 53:   #Starts Data Bulk
        paint_bulk(window)
        window.refresh()        
        start_bulk(window)
        key = -1

    elif key == 54:
        curses.endwin();  #Close curses   
              
    elif key == 27:      
       curses.endwin() #Close curses
    else:
        key = -1   

