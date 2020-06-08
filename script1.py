from tkinter import *

# project made up of two manin things window and widget
window = Tk()

def km_to_miles():
    
    # lets try a miles to 
    try:
        miles = float(e1_value.get())*1.6
        t1.insert(END,miles)
    except ValueError:
        t1.insert(END,"please enter number")

b1 = Button(window,text="Execute", command=km_to_miles)
b1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)


t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)





window.mainloop()