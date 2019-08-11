import curses
import curses.textpad
import random
import csv
import os
import DoublyLinkedCircularList
from DoublyLinkedCircularList import *
import DoublyLinkedList
from DoublyLinkedList import *
import Stack
from Stack import *
import Queue
from Queue import *
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, KEY_ENTER

player = "" #Variable que almacenara el username del jugador en turno, inicia como cadena vacia
score = 0 #Contador del score por nivel
scoretotal = 0 #Contador del score total
users = ListaCircularDoble()  #Estructura para almacenar todos los usuarios (Lista circular doble)
snake = ListaDoble() #Estrcutura para manejar el cuerpo de la snake (Lista doble)
scorestack = StackList() #Estructura para almacenar el score (Pila)
sbqueue = QueueList() #Estructura para almacenar el scoreboard (Cola)
speed = 100 #Parametro para velocidad de la snake
pypath =os.path.dirname(os.path.abspath(__file__)) #Path relativo del archivo .py
snackx = 1 #Posicion en x inicial (temporal) para los snacks
snacky = 1 #Posicion en y inicial (temporal) para los snacks
tipo = 1 #Tipo inicial de snack (1 es + y 2 es *)
new_snack = True #Variable que indica si se debe crear otro snack o no (por ejemplo al quitar pausa)
lvl = 1 #Nivel inicial del juego
newgame = True
gameover = False
nouser = False

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
    x_start = round((70-len(" SNAKE RELOADED "))/2)
    win.addstr(0,x_start," SNAKE RELOADED ")
    user_x = round((68-len(" User: "+player+" ")))
    win.addstr(0,user_x," User: "+player+" ")

def paint_score(win):
    global score
    win.addstr(0,2," Score:"+str(score)+" ")

def paint_level(win):
    global lvl
    win.addstr(0,13," Level:"+str(lvl)+" ")

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
    win.addstr(5,17,"↓ Choose the report you want to see ↓")
    pos_x = 27              
    pos_y = 9               
    win.addstr(pos_y,pos_x,"a. Snake Report") 
    win.addstr(pos_y+1,pos_x,"b. Score Report")  
    win.addstr(pos_y+2,pos_x,"c. Scoreboard Report")
    win.addstr(pos_y+3,pos_x,"d. Users Report")
    win.refresh()

def paint_gameover(win):
    global scoretotal
    win.clear()
    win.border(0)
    win.addstr(5,30,'GAME OVER')
    win.addstr(10,30,'Score: '+str(scoretotal))
    win.addstr(23,18,"Press ENTER to return to the menu")
    win.refresh()

def paint_nouser(win):
    win.clear()
    win.border(0)
    win.addstr(5,10,'SELECCIONA TU USUARIO ANTES DE INICIAR EL JUEGO')
    win.addstr(10,18,"1. Crear nuevo usuario")
    win.addstr(11,18,"2. Elegir usuario existente")
    win.addstr(23,18,"Press ESC to return to the menu")
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

def check_gameover():
    global snake
    gameover = False
    nodotemp = snake.primero.siguiente
    while nodotemp is not None:
        if snake.primero.y == nodotemp.y and snake.primero.x == nodotemp.x:
            gameover = True
        nodotemp = nodotemp.siguiente
    if gameover:
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
    global tipo
    global new_snack
    probabilidad = 0
    tipo = random.randint(1,2)
    probabilidad = random.randint(1,10)
    if new_snack == True:
        generate_coordinate()
        new_snack = False
    if probabilidad>8:
        tipo = 2
    else:
        tipo = 1
    if tipo == 1:
        win.addch(snacky,snackx,'+')
    if tipo == 2:
        win.addch(snacky,snackx,'*')
    win.refresh()

def snack_effect(win):
    global snake
    global tipo
    global snacky
    global snackx
    global score
    global scoretotal
    global lvl
    global speed
    global scorestack
    xtemp = 0
    ytemp = 0
    if tipo == 1:
        score = score + 1
        scoretotal = scoretotal + 1
        if score == 15:
            score = 0
            lvl = lvl + 1
            speed = speed - 10
        paint_score(win)
        paint_level(win)
        snake.agregar_final(snacky,snackx)
        scorestack.push(snacky,snackx)      
    if tipo == 2:
        if score != 0:
            ytemp = snake.ultimo.y 
            xtemp = snake.ultimo.x 
            score = score - 1
            scoretotal = scoretotal - 1
            snake.eliminar_ultimo()
            win.addch(ytemp, xtemp,' ')
        paint_score(win)
        scorestack.pop()        
    win.refresh()



def start_game(win): #Method to start game
    global snake
    global snackx
    global snake
    global new_snack
    global newgame
    global gameover
    global speed
    global scorestack
    global sbqueue
    headx = 0
    heady = 0
    key1 = KEY_RIGHT
    if newgame:
        scorestack.head = None
        snake.primero = None
        snake.ultimo = None
        snake.agregar_final(10,12) #primera parte del cuerpo de la snake 1/3
        snake.agregar_final(10,11) #segunda parte del cuerpo de la snake 2/3
        snake.agregar_final(10,10) #tercera parte del cuerpo de la snake 3/3
        newgame = False
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
            if check_gameover():
                gameover = True
                key1 = 27
            else:
                if aux.y==snacky and aux.x==snackx:
                    snack_effect(win)
                    new_snack = True
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
    if gameover == False:
        paint_menu(win) 

def start_scoreboard(win):
    key2 = -1
    while key2!=27:
        key2 = window.getch()

def start_userselection(win):
    global player
    nodoaux = users.primero
    if nodoaux is not None:
        paint_username(win,str(nodoaux.dato))
        key3 = -1
        while key3!=27:
            key3 = win.getch()
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
    else:
        win.addstr(10,20,"No hay usuario(s) registrado(s)")
        key3 = -1
        while key3!=27:
            key3 = win.getch()            
            if key3 == 10:           
                key3 = 27 

def snake_report():
    global snake
    global pypath
    urldot = pypath+'\\SnakeReport.dot'
    urlpng = pypath+'\\SnakeReport.png'
    if snake.primero is None:               
        print('The list is empty')     
    else:
        f = open(urldot,'w')
        f.write('digraph SnakeReport{\n')
        f.write('node [shape=record];\n')
        f.write('rankdir=LR;\n')
        temp = snake.primero
        count = 0
        limit = 0
        f.write('node{} [label=\"{{ null }}\"];\n'.format(str(count)))
        while temp is not None:
            count+=1
            f.write('node{} [label=\"{{ |({},{})| }}\"];\n'.format(str(count),str(temp.x),str(temp.y)))           
            temp = temp.siguiente
        f.write('node{} [label=\"{{ null }}\"];\n'.format(str(count+1)))
        limit = count
        count = 0
        while count < limit:
            f.write('node{} -> node{} [dir=back];\n'.format(str(count),str(count+1)))
            count = count + 1
        count = 1
        while count < limit+1:
            f.write('node{} -> node{};\n'.format(str(count),str(count+1)))
            count = count + 1
        f.write('}')
        f.close()
        os.system('dot {} -Tpng -o {}'.format(urldot,urlpng))
        os.startfile(urlpng,'open')

def score_report():
    global scorestack
    global pypath
    urldot = pypath+'\\ScoreReport.dot'
    urlpng = pypath+'\\ScoreReport.png'
    if snake.primero is None:               
        print('The list is empty')     
    else:
        f = open(urldot,'w')
        f.write('digraph SnakeReport{\n')
        f.write('node [shape=record];\n')
        f.write('rankdir=LR;\n')
        temp = scorestack.head
        command = 'stack1 [label=\"'
        while temp is not None:
            command= command+'|({},{})'.format(str(temp.x),str(temp.y))          
            temp = temp.next
        command = command + '\"];'
        f.write(command)       
        f.write('}')
        f.close()
        os.system('dot {} -Tpng -o {}'.format(urldot,urlpng))
        os.startfile(urlpng,'open')

def scoreboard_report():
    global sbqueue
    global pypath
    urldot = pypath+'\\ScoreboardReport.dot'
    urlpng = pypath+'\\ScoreboardReport.png'
    if sbqueue.head is None:               
        print('The queue is empty')     
    else:
        f = open(urldot,'w')
        f.write('digraph SnakeReport{\n')
        f.write('node [shape=record];\n')
        f.write('rankdir=LR;\n')
        temp = sbqueue.head
        count = 0
        limit = 0
        f.write('node{} [label=\"{{ null }}\"];\n'.format(str(count)))
        while temp is not None:
            count+=1 
            f.write('node{} [label=\"{{({},{})| }}\"];\n'.format(str(count),temp.username,str(temp.score)))          
            temp = temp.next           
        limit = count
        while limit > 1:
            f.write('node{} -> node{};\n'.format(str(limit),str(limit-1)))
            limit = limit - 1
        f.write('node1 -> node0;\n'.format(str(limit),str(limit-1)))
        f.write('}')
        f.close()
        os.system('dot {} -Tpng -o {}'.format(urldot,urlpng))
        os.startfile(urlpng,'open')

def users_report():
    global users
    global pypath
    urldot = pypath+'\\UsersReport.dot'
    urlpng = pypath+'\\UsersReport.png'
    if users.primero is None:               
        print('The list is empty')     
    else:
        f = open(urldot,'w')
        f.write('digraph UsersReport{\n')
        f.write('node [shape=record];\n')
        f.write('rankdir=LR;\n')
        temp = users.primero
        count = 0
        limit = 0
        while temp is not users.ultimo:           
            f.write('node{} [label=\"{{ |({})| }}\"];\n'.format(str(count),temp.dato))
            count+=1          
            temp = temp.siguiente
        f.write('node{} [label=\"{{ |({})| }}\"];\n'.format(str(count),temp.dato))
        limit = count
        count = 0
        while count < limit:
            f.write('node{} -> node{} [dir=back];\n'.format(str(count),str(count+1)))
            count = count + 1
        count = 0
        while count < limit:
            f.write('node{} -> node{};\n'.format(str(count),str(count+1)))
            count = count + 1
        count = 0
        f.write('node{} -> node{} [dir=back];\n'.format(str(count),str(limit)))
        f.write('node{} -> node{};\n'.format(str(count),str(limit)))
        f.write('}')
        f.close()
        os.system('dot {} -Tpng -o {}'.format(urldot,urlpng))
        os.startfile(urlpng,'open')
        

def start_reports(win):
    key4 = -1
    while key4!=27:
        key4 = window.getch()
        if key4 == 97:
            snake_report()
            key4 = -1
        if key4 == 98:
            score_report()
            key4 = -1
        if key4 == 99:
            scoreboard_report()
            key4 = -1
        if key4 == 100:
            users_report()
            key4 = -1        

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

def start_gameover(win):
    global newgame
    global gameover
    global score
    global scoretotal
    global sbqueue
    global player
    global speed
    key6 = -1
    while key6!=10:
        key6 = window.getch()
    gameover = False
    if sbqueue.size<10:
        sbqueue.enqueue(player,scoretotal)
    else:
        sbqueue.dequeue()
        sbqueue.enqueue(player,scoretotal)
    scoretotal = 0
    score = 0    
    speed = 100
    newgame = True
    paint_menu(win)

def start_nouser(win):
    key7 = -1
    while key7!=27:
        key7 = win.getch()
        if key7 == 50:
            paint_userselection(win)
            win.refresh()  
            start_userselection(win)
            key7 = 27
            
    
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
        if player != "":
            paint_playgame(window)
            paint_score(window)
            paint_level(window)
            window.refresh()
            start_game(window)
            key = -1
        else:
            paint_nouser(window)
            window.refresh()
            start_nouser(window)
            paint_menu(window)
            window.refresh()
            key = -1

    elif key == 50:     #Shows scoreboard
        paint_scoreboard(window)
        window.refresh()
        start_scoreboard(window)
        paint_menu(window)
        window.refresh()
        key = -1

    elif key == 51:   #Starts User selection
        paint_userselection(window)
        window.refresh()  
        start_userselection(window)
        paint_menu(window)
        window.refresh()
        key = -1
    
    elif key == 52: #Shows Reports Menu
        paint_reports(window)
        window.refresh()
        start_reports(window)
        paint_menu(window)
        window.refresh()
        key = -1

    elif key == 53:   #Starts Data Bulk
        paint_bulk(window)
        window.refresh()        
        start_bulk(window)
        paint_menu(window)
        window.refresh()
        key = -1

    elif key == 54:
        curses.endwin() #Close curses   

    elif gameover == True:
        paint_gameover(window)
        window.refresh()
        start_gameover(window)
        key = -1

    elif key == 27:      
       curses.endwin() #Close curses
    else:
        key = -1   

