import tkinter


def on_button_click():
    label.config(text="Nice choice")


m = tkinter.Tk()  # where m is the name of the main window object
m.title('Major Decision')
label = tkinter.Label(m, text="No Selection Made")
label.grid(row=4)
var1 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="CIS", variable=var1).grid(row=0)
var2 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="BIS", variable=var2).grid(row=1)
button = tkinter.Button(m, text='Choose', width=25, command=on_button_click)
button.grid(row=3)
exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=5)
m.mainloop()  # infinite loop that waits for events to happen
