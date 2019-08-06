import curses #import the curses library
import curses.textpad
import csv
import DoublyLinkedCircularList
from DoublyLinkedCircularList import *
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, KEY_ENTER #import special KEYS from the curses library

player = "";
users = ListaCircularDoble()


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

def start_scoreboard(win):
    key2 = -1
    while key2!=27:
        key2 = window.getch()
    paint_menu(win) 

def start_userselection(win):
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
    path = "C:\\Snake\\"+tb.gather()
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
   
    if key == 50:
        paint_scoreboard(window)
        window.refresh()
        start_scoreboard(window)
        key = -1

    elif key == 51:
        paint_userselection(window)
        window.refresh()  
        start_userselection(window)
        key = -1
    
    elif key == 52:
        paint_reports(window)
        window.refresh()
        start_reports(window)
        key = -1

    elif key == 53:
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

