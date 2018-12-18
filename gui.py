from tkinter import Tk, Button, font

from board import Board


class GUI:
    def __init__(self):
        self.app = Tk()
        self.app.title("Tic Tac Toe")
        self.app.resizable(0, 0)
        self.board = Board()
        self.buttons = {}
        self.font = font.Font(family='Roboto', size=20)
        for x, y in self.board.fields:
            def button_handler(x=x, y=y): self.click(x, y)

            button = Button(self.app, text="", font=self.font, fg='black', height=4, width=8, command=button_handler)
            button.grid(column=x, row=y)
            self.buttons[x, y] = button

        def reset_button_handler(): self.reset()

        reset_button = Button(self.app, text="Reset", font=self.font, fg='black', height=1,
                              command=reset_button_handler)
        reset_button.grid(row=self.board.size + 1, column=0, columnspan=self.board.size, sticky="WE")
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

    def reset(self):
        self.board = Board()
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

    def mainloop(self):
        self.app.mainloop()


if __name__ == "__main__":
    GUI().mainloop()
