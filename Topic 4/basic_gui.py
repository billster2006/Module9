import tkinter

main_window = tkinter.Tk() # where m is the name of the main window object
main_window.title('Major Decision')
var1 = tkinter.IntVar()
check = tkinter.Checkbutton(main_window, text="CIS", variable=var1).grid(row=0)
var2 = tkinter.IntVar()
check = tkinter.Checkbutton(main_window, text="BIS", variable=var2).grid(row=1)
button = tkinter.Button(main_window, text='Choose', width=25, command=main_window.destroy)
button.grid(row=3)
main_window.mainloop()  # infinite loop that waits for events to happen
