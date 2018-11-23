from tkinter import *

window = Tk()
window.title("Tic Tac Toe")
window.resizable(0, 0)

button11 = Button(window, text="X", font='Roboto 20 bold', fg='black', height=4, width=8)
button11.grid(row=1, column=0, sticky=S + N + E + W)

button12 = Button(window, text="X", font='Roboto 20 bold', fg='black', height=4, width=8)
button12.grid(row=1, column=1, sticky=S + N + E + W)

button13 = Button(window, text="X", font='Roboto 20 bold', fg='black', height=4, width=8)
button13.grid(row=1, column=2, sticky=S + N + E + W)

button21 = Button(window, text="X", font='Roboto 20 bold', fg='black', height=4, width=8)
button21.grid(row=2, column=0, sticky=S + N + E + W)

button22 = Button(window, text="X", font='Roboto 20 bold', fg='black', height=4, width=8)
button22.grid(row=2, column=1, sticky=S + N + E + W)

button23 = Button(window, text="X", font='Roboto 20 bold', fg='black', height=4, width=8)
button23.grid(row=2, column=2, sticky=S + N + E + W)

button31 = Button(window, text="X", font='Roboto 20 bold', fg='black', height=4, width=8)
button31.grid(row=3, column=0, sticky=S + N + E + W)

button32 = Button(window, text="X", font='Roboto 20 bold', fg='black', height=4, width=8)
button32.grid(row=3, column=1, sticky=S + N + E + W)

button33 = Button(window, text="X", font='Roboto 20 bold', fg='black', height=4, width=8)
button33.grid(row=3, column=2, sticky=S + N + E + W)

restartButton = Button(window, text="Restart", font='Roboto', fg='black', height=1, width=8, pady=10)
restartButton.grid(row=4, column=1, sticky=S + N + E + W)

window.mainloop()
