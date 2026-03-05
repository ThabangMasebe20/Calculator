import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0 , "end")
    text_result.insert(1.0, calculation)
    

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0 , "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")
        pass


def backspace():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, tk.END)
    text_result.insert(1.0, calculation)


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.title("Calculator")

root.geometry("280x270")

text_result = tk.Text(root, height=2, width=16, font=('Arial', 23))
text_result.grid(columnspan=5)


btnClear = tk.Button(root, text= "C", command=lambda: clear_field(), width=5, font=("Arial", 14))
btnClear.grid(row=2, column=1)

btnOpen = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14)) 
btnOpen.grid(row=2, column=2)

btnClose = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
btnClose.grid(row=2, column=3)

btnBack = tk.Button(text= "←", command=backspace, width=5, font=("Arial", 14))
btnBack.grid(row=2, column=4)

btn1 = tk.Button(root, text="1", command=lambda : add_to_calculation(1), width=5, font=("Arial", 14))
btn1.grid(row=3, column=1)

btn2 = tk.Button(root, text="2", command=lambda : add_to_calculation(2), width=5, font=("Arial", 14))
btn2.grid(row=3, column=2)

btn3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn3.grid(row=3, column=3)

btn4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn4.grid(row=4, column=1)

btn5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn5.grid(row=4, column=2)

btn6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn6.grid(row=4, column=3)

btn7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn7.grid(row=5, column=1)

btn8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn8.grid(row=5, column=2)

btn9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn9.grid(row=5, column=3)

btn0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
btn0.grid(row=6, column=2)

btnPlus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btnPlus.grid(row=6, column=4)

btnMinus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btnMinus.grid(row=5, column=4)

btnEqual = tk.Button(root, text="=", command=lambda: evaluate_calculation(), width=5, font=("Arial", 14))
btnEqual.grid(row=6, column=3) # We will to which one is better. Row 5 or 6

btnDiv = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btnDiv.grid(row=3, column=4)

btnMulti = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btnMulti.grid(row=4, column=4)


btnDot = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, font=("Arial", 14))
btnDot.grid(row=6, column=1)


root.mainloop()