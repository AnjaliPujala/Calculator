from tkinter import Tk, Label, Button

root = Tk()

mytext = ""
textLabel = Label(root, text=mytext, justify="right", relief="sunken", padx=150, pady=20)
textLabel.grid(row=0, column=0, columnspan=3, padx=20, pady=20)
previousop=0
def changeText(value):
    global mytext
    mytext += str(value)
    textLabel.configure(text=mytext)

def CheckNum(value):
    changeText(value)
def performOp():
    res = 0
    mystr = ""
    l = []
    operator = []
    text = textLabel.cget("text")

    for i in text:
        if i.isdigit():
            mystr += i
        elif i in ['+', '-', '*', '/']:
            l.append(int(mystr))
            l.append(i)
            operator.append(i)
            mystr = ""
    
    l.append(int(mystr))  
    res = l[0]
    for i in range(1, len(l), 2):
        if operator[i // 2] == '+':
            res += l[i + 1]
        elif operator[i // 2] == '-':
            res -= l[i + 1]
        elif operator[i // 2] == '*':
            res *= l[i + 1]
        elif operator[i // 2] == '/':
            if l[i + 1] != 0:
                res /= l[i + 1]
            else:
                textLabel.configure(text="Error: Division by zero")
                return

    textLabel.configure(text=str(res))
def ClearText():
    textLabel.configure(text="")
for i in range(10):
    button = Button(root, text=str(i), command=lambda i=i: CheckNum(i), padx=20, pady=10)
    button.grid(row=(i // 3) + 1, column=i % 3)
buttonPlus=Button(root,text="+",command=lambda symbol="+": CheckNum(symbol),padx=20,pady=10)
buttonPlus.grid(row=4,column=1)
buttonMinus=Button(root,text="-",command=lambda symbol="-": CheckNum(symbol),padx=20,pady=10)
buttonMinus.grid(row=4,column=2)
buttonMul=Button(root,text="*",command=lambda symbol="*": CheckNum(symbol),padx=20,pady=10)
buttonMul.grid(row=5,column=0)
buttonDiv=Button(root,text="/",command=lambda symbol="/": CheckNum(symbol),padx=20,pady=10)
buttonDiv.grid(row=5,column=1)
buttonEqual=Button(root,text="=",command=lambda : performOp(),padx=20,pady=10)
buttonEqual.grid(row=5,column=2)
buttonClear=Button(root,text="C",command=lambda : ClearText(),padx=150,pady=10)
buttonClear.grid(row=6,column=0,columnspan=3)
root.mainloop()

