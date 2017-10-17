import curses

def key_input(event):
    if event == curses.KEY_LEFT:
        print("Left Arrow Key pressed")
    elif event == curses.KEY_RIGHT:
        print("Right Arrow Key pressed")
    elif event == curses.KEY_DOWN:
        print("Lower Arrow Key pressed")
    elif event == curses.KEY_UP:
        curses.endwin()
    else:
        print(event)

screen = curses.initscr()
try:
    #curses.noecho()
    #curses.curs_set(0)
    screen.keypad(1)
    screen.addstr("Press a key")
except Exception:
    print('Error')

try:
    while 1:
        x = screen.getch()
        key_input(x)
except Exception:
    print('Error')



