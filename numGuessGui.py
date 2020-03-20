import tkinter as tk
from tkinter import messagebox
import random

window = tk.Tk()
window.geometry("500x500")
window.configure(bg="#a8f7b5")

tk.Label(window,text="Welcome to NumGuess!",font="bold 20",bg="#a8f7b5").pack()

tk.Label(window,text="Guess the 3 digits with the clue's provided",bg="#a8f7b5").place(x=10,y=50)

x = 0

count_submit = 0

def clear():
    entry_one.delete(0,"end")
    entry_two.delete(0,"end")
    entry_three.delete(0,"end")

def generate():
    btn_submit.config(state='normal')
    global x
    global count_submit
    count_submit=0
    x1 = random.randrange(100, 1000)
    x = list(map(int, str(x1)))

    tk.Label(window, text="***CLUE***", font="bold",bg="#a8f7b5").place(x=10, y=110)

    if x[0]%2==0:
        tk.Label(window,text="1)The the 1st digit is EVEN",bg="#a8f7b5").place(x=10,y=150)
    else:
        tk.Label(window,text="1)The the 1st digit is ODD",bg="#a8f7b5").place(x=10,y=150)

    if x[1]%2==0:
        tk.Label(window,text="2)The the 2nd digit is EVEN",bg="#a8f7b5").place(x=10,y=170)
    else:
        tk.Label(window,text="2)The the 2nd digit is ODD",bg="#a8f7b5").place(x=10,y=170)

    if x[2]%2==0:
        tk.Label(window,text="3)The the 3rd digit is EVEN",bg="#a8f7b5").place(x=10,y=190)
    else:
        tk.Label(window,text="3)The the 3rd digit is ODD",bg="#a8f7b5").place(x=10,y=190)
    clear()


def check():
    try:
        p = int(entry_one.get())
        q = int(entry_two.get())
        r = int(entry_three.get())

        global x
        global count_submit

        if count_submit==0:

            if (x[0], x[1], x[2]) == (p, q, r):
                messagebox.showinfo("Note","Matched!!!\nPlease generate a number")
                btn_submit.config(state='disabled')
                return 0

            elif (x[0], x[1]) == (p, q):
                messagebox.showinfo("Note","First and Second Number's are correct")
                count_submit+=1

            elif (x[1], x[2]) == (q, r):
                messagebox.showinfo("Note","Second and Third Number's are correct")
                count_submit += 1

            elif (x[0], x[2]) == (p, r):
                messagebox.showinfo("Note","First and Third Number's are correct")
                count_submit += 1

            elif x[0] == p:
                messagebox.showinfo("Note","First Number is correct")
                count_submit += 1

            elif x[1] == q:
                messagebox.showinfo("Note","Second Number is correct")
                count_submit += 1

            elif x[2] == r:
                messagebox.showinfo("Note","Third Number is correct")
                count_submit += 1

            else:
                messagebox.showinfo("Note","No match!!")
                count_submit += 1

        elif count_submit==1:
            if (x[0], x[1], x[2]) == (p, q, r):
                messagebox.showinfo("Note","Matched!!!\nPlease generate a number")
                btn_submit.config(state='disabled')


            elif (x[0], x[1]) == (p, q):
                messagebox.showinfo("Note","First and Second Number's are correct\nNext attempt is "
                                           "your last attempt")
                count_submit+=1

            elif (x[1], x[2]) == (q, r):
                messagebox.showinfo("Note","Second and Third Number's are correct\nNext attempt is "
                                           "your last attempt")
                count_submit += 1

            elif (x[0], x[2]) == (p, r):
                messagebox.showinfo("Note","First and Third Number's are correct\nNext attempt is "
                                           "your last attempt")
                count_submit += 1

            elif x[0] == p:
                messagebox.showinfo("Note","First Number is correct\nNext attempt is "
                                           "your last attempt")
                count_submit += 1

            elif x[1] == q:
                messagebox.showinfo("Note","Second Number is correct\nNext attempt is "
                                           "your last attempt")
                count_submit += 1

            elif x[2] == r:
                messagebox.showinfo("Note","Third Number is correct\nNext attempt is "
                                           "your last attempt")
                count_submit += 1

            else:
                messagebox.showinfo("Note","No match!!\nNext attempt is "
                                           "your last attempt")
                count_submit += 1
        else:

            if (x[0], x[1], x[2]) == (p, q, r):
                messagebox.showinfo("Note","Matched!!!\nPlease generate a number")
                btn_submit.config(state='disabled')


            elif (x[0], x[1]) == (p, q):
                messagebox.showinfo("Note","First and Second Number's are correct\nThis was your last "
                                           "attempt\nplease generate a new number")
                count_submit+=1

            elif (x[1], x[2]) == (q, r):
                messagebox.showinfo("Note","Second and Third Number's are correct\nThis was your last "
                                           "attempt\nplease generate a new number")
                count_submit += 1

            elif (x[0], x[2]) == (p, r):
                messagebox.showinfo("Note","First and Third Number's are correct\nThis was your last "
                                           "attempt\nplease generate a new number")
                count_submit += 1

            elif x[0] == p:
                messagebox.showinfo("Note","First Number is correct\nThis was your last "
                                           "attempt\nplease generate a new number")
                count_submit += 1

            elif x[1] == q:
                messagebox.showinfo("Note","Second Number is correct\nThis was your last "
                                           "attempt\nplease generate a new number")
                count_submit += 1

            elif x[2] == r:
                messagebox.showinfo("Note","Third Number is correct\nThis was your last "
                                           "attempt\nplease generate a new number")
                count_submit += 1

            else:
                messagebox.showinfo("Note","No match!!\nThis was your last "
                                           "attempt\nplease generate a new number")
                count_submit += 1
            messagebox.showinfo("Note","The number was {}".format("".join(str(i) for i in x)))
            btn_submit.config(state='disabled')
        clear()
    except Exception:
        messagebox.showwarning("ALERT","Enter valid digits into the box")
        clear()

highlightbackground='#3E4149'

btn_generate = tk.Button(window,text="Generate Number",command=generate,highlightbackground='#3E4149',
                       foreground="black")
btn_generate.place(x=120,y=90)


btn_submit = tk.Button(window,text="Submit",command=check,highlightbackground='#3E4149',
                       foreground="black")
btn_submit.place(x=150,y=320)
btn_submit.config(state="disabled")

entry_one = tk.Entry(window,width=5)
entry_two = tk.Entry(window,width=5)
entry_three = tk.Entry(window,width=5)

entry_one.place(x=50,y=240)
entry_two.place(x=150,y=240)
entry_three.place(x=250,y=240)



window.mainloop()