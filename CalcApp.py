from tkinter import *

calc = Tk()
calc.title("My Simple Calculator")
calc.geometry("400x500")

calc_input = ""
calc_display = StringVar()

def button_click(number): 
    global calc_input
    calc_input = calc_input + str(number)
    calc_display.set(calc_input)

def equal():
    global calc_input

    try:
        result = str (eval(calc_input))
        calc_display.set(result)
        calc_input = result

    except SyntaxError:
        calc_display.set("Syntax Error")
        calc_input = ""

    except ZeroDivisionError:
        calc_display.set("Cannot divide by 0")
        calc_input = ""

def backspace():
    global calc_input
    calc_input = calc_input[:-1]
    calc_display.set(calc_input)

def clear():
    global calc_input
    calc_display.set ("")
    calc_input = ""

#display screen
display_screen= Label(calc,
                      textvariable=calc_display, 
                      font=("Lexend", 12),
                      width=35,
                      borderwidth=5)

display_screen.grid(row=0, 
                    column=0, 
                    columnspan=5, 
                    padx=10, 
                    pady=10)

frame = Frame(calc)
frame.grid(row=1, column=0, columnspan=4)

#buttons for numbers
button_1 = Button(frame, 
                  text="1", 
                  font=("Lexend", 12),
                  height=3,
                  width=6,
                  padx=3, 
                  pady=3,
                  command= lambda: button_click(1))

button_1.grid(row=3, column=0)

button_2 = Button(frame, 
                  text="2", 
                  font=("Lexend", 12),
                  height=3,
                  width=6,
                  padx=3, 
                  pady=3,
                  command= lambda: button_click(2))

button_2.grid(row=3, column=1)

button_3 = Button(frame, 
                  text="3", 
                  font=("Lexend", 12),
                  height=3,
                  width=6,
                  padx=3, 
                  pady=3,
                  command= lambda: button_click(3))

button_3.grid(row=3, column=2)

button_4 = Button(frame, 
                  text="4", 
                  font=("Lexend", 12),
                  height=3,
                  width=6,
                  padx=3, 
                  pady=3,
                  command= lambda:button_click(4))

button_4.grid(row=2, column=0)

button_5 = Button(frame, 
                  text="5", 
                  font=("Lexend", 12),
                  height=3,
                  width=6,
                  padx=3, 
                  pady=3,
                  command= lambda: button_click(5))

button_5.grid(row=2, column=1)

button_6 = Button(frame, 
                  text="6", 
                  font=("Lexend", 12),
                  height=3,
                  width=6,
                  padx=3, 
                  pady=3,
                  command= lambda: button_click(6))

button_6.grid(row=2, column=2)

button_7 = Button(frame, 
                  text="7", 
                  font=("Lexend", 12),
                  height=3,
                  width=6,
                  padx=3, 
                  pady=3,
                  command= lambda:button_click(7))

button_7.grid(row=1, column=0)

button_8 = Button(frame, 
                  text="8", 
                  font=("Lexend", 12),
                  height=3,
                  width=6,
                  padx=3, 
                  pady=3,
                  command= lambda:button_click(8))

button_8.grid(row=1, column=1)

button_9 = Button(frame, 
                  text="9", 
                  font=("Lexend", 12),
                  height=3,
                  width=6,
                  padx=3, 
                  pady=3,
                  command= lambda:button_click(9))

button_9.grid(row=1, column=2)

button_0 = Button(frame, 
                  text="0",
                  font=("Lexend", 12),
                  height=3,
                  width=6,
                  padx=3, 
                  pady=3,
                  command= lambda:button_click(0))

button_0.grid(row=4, column=1)

#buttons for operations
button_add = Button(frame, 
                  text="+", 
                  font=("Lexend", 12),
                  height=3,
                  width=6,
                  padx=3, 
                  pady=3,
                  command= lambda: button_click("+"))

button_add.grid(row=1, column=3)

button_sub = Button(frame, 
                  text="-", 
                  font=("Lexend", 12),
                  height=3,
                  width=6,
                  padx=3, 
                  pady=3,
                  command= lambda: button_click("-"))

button_sub.grid(row=2, column=3)

button_mul = Button(frame, 
                  text="×", 
                  font=("Lexend", 12),
                  height=3,
                  width=6,
                  padx=3, 
                  pady=3,
                  command= lambda: button_click("*"))

button_mul.grid(row=3, column=3)

button_div = Button(frame, 
                  text="÷", 
                  font=("Lexend", 12),
                  height=3,
                  width=6,
                  padx=3, 
                  pady=3,
                  command= lambda:button_click("/"))

button_div.grid(row=4, column=3)

decimal= Button(frame, 
                  text=".", 
                  font=("Lexend", 12),
                  height=3,
                  width=6,
                  padx=3, 
                  pady=3,
                  command= lambda: button_click("."))

decimal.grid(row=4, column=0)


button_equal = Button(frame, 
                  text="=", 
                  font=("Lexend", 12),
                  height=3,
                  width=6,
                  padx=3, 
                  pady=3,
                  command= lambda: equal())

button_equal.grid(row=4, column=2)

button_clear = Button(frame, 
                  text="C", 
                  font=("Lexend", 12),
                  height=3,
                  width=6,
                  padx=3, 
                  pady=3,
                  command= clear)

button_clear.grid(row=4, column=3)

button_backspace = Button(frame,
                  text="⌫",
                  font=("Lexend", 12),
                  height=3,
                  width=6,
                  padx=3, 
                  pady=3,
                  command= backspace)

button_backspace.grid(row=0, column=4)

calc.mainloop()