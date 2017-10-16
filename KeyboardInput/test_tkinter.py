import tkinter as tk
import calculator

calc = calculator.calculator()
x = 0

def key_input(event):
    #print
    #'Key:', event.char
    key_press = event.char
    global x

    if key_press.lower() == 'w':
        print('addition by 1')
        x = calc.addition(x,1)
        print("%.2f" % x)
    elif key_press.lower() == 's':
        print('subtraction by 1')
        x = calc.subtraction(x, 1)
        print("%.2f" % x)
    elif key_press.lower() == 'a':
        print('mutliplication by 2')
        x = calc.multiplication(x, 2)
        print("%.2f" % x)
    elif key_press.lower() == 'd':
        print('division by 2')
        x = calc.division(x, 2)
        print("%.2f" % x)
    elif key_press == ' ':
        print('space')
    elif key_press.lower() == 'q':
        print('quit')
        root.quit()
    '''else:
        try:
            print(key_press)
        except ValueError:
            print('not valid key')
    '''

def leftKey(event):
    print("Left key pressed")
def rightKey(event):
    print("Right key pressed")
def upKey(event):
    print("Forward key pressed")
def downKey(event):
    print("Backward key pressed")

root = tk.Tk()
root.bind('<KeyPress>', key_input)
root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
root.bind('<Up>', upKey)
root.bind('<Down>', downKey)
root.mainloop()