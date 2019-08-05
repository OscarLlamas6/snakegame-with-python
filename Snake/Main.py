import curses #import the curses library
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library
from curses.textpad import Textbox, rectangle

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

key = KEY_RIGHT         #key defaulted to KEY_RIGHT
pos_x = 27              #initial x position
pos_y = 10               #initial y position
window.addstr(0,30,"MAIN MENU") 
window.addstr(pos_y,pos_x,"1. Play") 
window.addstr(pos_y+1,pos_x,"2. Scoreboard")  
window.addstr(pos_y+2,pos_x,"3. User Selection")
window.addstr(pos_y+3,pos_x,"4. Reports")
window.addstr(pos_y+4,pos_x,"5. Bulk Loading")
window.addstr(24,30,"201602625") 
while key != 27:                #run program while [ESC] key is not pressed
    window.timeout(100)         #delay of 100 milliseconds
    keystroke = window.getch()  #get current key being pressed
    if keystroke is not  -1:    #key is pressed 
        key = keystroke 
    if key == 53:
        window.addch(1,1,' ')
        window.clrtobot()
        window.border(0)
        window.addstr(0,28,"BULK LOADING") 
        window.addstr(5,20,"↓ Please enter .csv file name ↓")
        window.border(0)
        window.refresh()    
              
    if key == 27:      
        window.addch(1,1,' ')
        window.clrtobot()
        window.border(0)
        window.addstr(10,30,"ADIOS")
        window.refresh()
      

curses.endwin() #return terminal to previous state