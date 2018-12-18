import sys
from Board import Board

if sys.version_info[0] < 3:  # Specific import for python 2 and 3 compatibility
    from Tkinter import Tk, Button
    from tkFont import Font
else:
    from tkinter import Tk, Button, font

    Font = font.Font  # remapping font func for compatibility


class GUI:
    def __init__(self):
        self.app = Tk()
        self.app.title("Tic Tac Toe")
        self.app.resizable(0, 0)
        self.board = Board()
        self.buttons = {}
        self.font = Font(family='Roboto', size=20)
        for x, y in self.board.fields:
            def button_handler(x=x, y=y): self.click(x, y)

            button = Button(self.app, text="", font=self.font, fg='black', height=4, width=8, command=button_handler)
            button.grid(column=x, row=y)
            self.buttons[x, y] = button

        def restart_button_handler(): self.restart()

        restart = Button(self.app, text="Restart", font=self.font, fg='black', height=1,
                         command=restart_button_handler)
        restart.grid(row=self.board.size + 1, column=0, columnspan=self.board.size, sticky="WE")
        self.update()

    def click(self, x, y):
        self.app.config(cursor="watch")
        self.app.update()
        self.board = self.board.move(x, y)
        self.update()
        best_move = self.board.best_move()
        if best_move:
            self.board = self.board.move(*best_move)  # python's way of destructuring a tuple into two distinct value
            self.update()
        self.app.config(cursor="")

    def restart(self):
        self.board = Board()  # create new board instance
        self.update()

    def update(self):
        for (x, y) in self.board.fields:
            text = self.board.fields[x, y]
            self.buttons[x, y]['text'] = text
            self.buttons[x, y]['disabledforeground'] = 'black'
            if text != '':
                self.buttons[x, y]['state'] = 'disabled'
            else:
                self.buttons[x, y]['state'] = 'normal'

        winning = self.board.winning_position()

        if winning:
            for x, y in winning:
                self.buttons[x, y]['disabledforeground'] = 'green'
            for x, y in self.buttons:
                self.buttons[x, y]['state'] = 'disabled'

    def start(self):
        self.app.mainloop()


if __name__ == "__main__":
    GUI().start()
