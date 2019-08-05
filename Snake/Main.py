import curses #import the curses library
import curses.textpad
import DoublyLinkedCircularList
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, KEY_ENTER #import special KEYS from the curses library



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

def paint_userselection(win):
    win.clear()
    win.border(0) 
    paint_title(win,"USER SELECTION")
    win.addstr(5,20,"↓ Please select your username ↓")
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
    
def start_userselection(win):
    key4 = window.getch()
    while key4!=27:
        key4 = window.getch()
    paint_menu(win)   

def start_bulk(win):
    path = ""
    win2 = curses.newwin(1,40,9,15)
    tb = curses.textpad.Textbox(win2, insert_mode=True)
    text = tb.edit()
    path = tb.gather()
    win.refresh()
    win.addstr(23,10,"Press ESC to cancel  |  Press ENTER to bulk data")
    win.refresh()
    key5 = window.getch()
    while key5!=27:
        key5 = window.getch()
     
    
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
   
    if key == 51:
        paint_userselection(window)
        start_userselection(window)
        key = -1
    elif key == 53:
        paint_bulk(window)
        window.refresh()        
        start_bulk(window)
        key = -1
        paint_menu(window)  
              
    elif key == 27:      
       curses.endwin() #return terminal to previous state
    else:
        key = -1   

