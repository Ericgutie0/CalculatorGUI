from tkinter import *


# every program has a root, which is the window
root = Tk()
root.title("-- CALCULATOR --")


# their values will change within the math operater functions
global value
global math


# --- Entry ----
# text box
e = Entry(root,borderwidth=3)
e.grid(row=0,column=0,columnspan=4,pady=3)



#  ----- Funtions -----


# button_click, activates on numerical face buttons
def button_click(number):

    # get what's in the entry
    curr_num = e.get()

    # delete previous entries
    e.delete(0,END)

    # concat on screen
    e.insert(0,curr_num + str(number))



# used in every mathmatical operator function
def fetch():

    # get what's in the text box(Entry)
    num_entry = e.get()

    # store that number
    global value

    value = float(num_entry)

    # clear it for the next
    e.delete(0,END)




def add():
    try:
        fetch()
    except:
        # print('Nothing to Calculate')
        pass

    global math
    math = "addition"


def subtract():
    try:
        fetch()
    except:
        # print('Nothing to Calculate')
        pass

    global math
    math = "subtraction"
    

def multiply():
    try:
        fetch()
    except:
        # print('Nothing to Calculate')
        pass

    global math
    math = "multiplication"
    

def divide():
    try:
        fetch()
    except:
        # print('Nothing to Calculate')
        pass

    global math
    math = "division"
   


# Equal to function
def equals():
    
    num_entry = e.get()

    e.delete(0,END)

    try:
        if math == 'addition':
            e.insert(0, value + float(num_entry))
        elif math == 'subtraction':
            e.insert(0,value - float(num_entry))
        elif math == 'multiplication':
            e.insert(0,value  * float(num_entry))
        elif math == 'division':
            e.insert(0,value / float(num_entry))
        else:
            pass
    except:
        # print("Nothing to Calculate")
        pass
    


# Clear the textbox
def clear():
    e.delete(0,END)




#    ---- Buttons -----

# Numbers , need to use lambdas to pass in parameters for command attribute (work around)

# 7
button_7 = Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
button_7.grid(row=1,column=0)

# 8
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))
button_8.grid(row=1,column=1)

# 9
button_9 = Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))
button_9.grid(row=1,column=2)

# 4
button_4 = Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
button_4.grid(row=2,column=0)

# 5
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
button_5.grid(row=2,column=1)

# 6
button_6 = Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))
button_6.grid(row=2,column=2)

# 3
button_3 = Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))
button_3.grid(row=3,column=2)

# 2
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
button_2.grid(row=3,column=1)

# 1
button_1 = Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
button_1.grid(row=3,column=0)

# 0
button_0 = Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))
button_0.grid(row=4,column=0)


# Addtion button + 
button_add = Button(root,text="+",padx=40,pady=20,command=add)
button_add.grid(row=4,column=3)

# Subtract button -
button_sub = Button(root,text="-",padx=40,pady=20,command=subtract)
button_sub.grid(row=3,column=3)

# Multiply x
button_mult = Button(root,text="x",padx=40,pady=20,command=multiply)
button_mult.grid(row=2,column=3)

# Divde /
button_div = Button(root,text="/",padx=40,pady=20,command=divide)
button_div.grid(row=1,column=3)

# Equal to button =
button_equals = Button(root,text="=",padx=85,pady=20,command=equals)
button_equals.grid(row=4,column=1,columnspan=2)


# Clear Button 
button_clear = Button(root,text="CLEAR",padx=100,pady=20,command=clear)
button_clear.grid(row=6,column=0,columnspan=4)


# Event Loop
root.mainloop()