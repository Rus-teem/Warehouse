"""Классическая игра Змейка на tkinter."""

from tkinter import *
from random import randint


class Game:
    """Основной класс игры «Змейка»."""

    def __init__(self, canvas):
        self.canvas = canvas
        self.snake_coords = [[14, 14]]
        self.apple_coords = [randint(0, 29) for _ in range(2)]
        self.vector = {"Up": (0, -1), "Down": (0, 1), "Left": (-1, 0), "Right": (1, 0)}
        self.direction = self.vector["Right"]
        self.canvas.focus_set()
        self.canvas.bind("<KeyPress>", self.set_direction)
        self.GAME()

    def set_apple(self):
        """Устанавливает новое яблоко в случайную позицию, не занятую змейкой."""
        self.apple_coords = [randint(0, 29) for _ in range(2)]
        if self.apple_coords in self.snake_coords:
            self.set_apple()

    def set_direction(self, event):
        """Меняет направление движения змейки по нажатию клавиши."""
        if event.keysym in self.vector:
            self.direction = self.vector[event.keysym]

    def draw(self):
        """Отрисовывает игровое поле: змейку и яблоко."""
        self.canvas.delete(ALL)
        x_apple, y_apple = self.apple_coords
        self.canvas.create_rectangle(x_apple*10, y_apple*10, (x_apple+1)*10, (y_apple+1)*10, fill="red", width=0)
        for x, y in self.snake_coords:
            self.canvas.create_rectangle(x*10, y*10, (x+1)*10, (y+1)*10, fill="green", width=0)

    @staticmethod
    def coord_check(coord):
        """Возвращает координату в пределах поля (0-29) с wrap-around."""
        return 0 if coord > 29 else 29 if coord < 0 else coord

    def GAME(self):
        """Основной игровой цикл: движение, проверка коллизий, перерисовка."""
        self.draw()
        x, y = self.snake_coords[0]
        x += self.direction[0]
        y += self.direction[1]
        x = self.coord_check(x)
        y = self.coord_check(y)
        if x == self.apple_coords[0] and y == self.apple_coords[1]:
            self.set_apple()
        elif [x, y] in self.snake_coords:
            self.snake_coords = []
        else:
            self.snake_coords.pop()
        self.snake_coords.insert(0, [x, y])
        self.canvas.after(100, self.GAME)


root = Tk()
canvas = Canvas(root, width=300, height=300, bg="black")
canvas.pack()
game = Game(canvas)
root.mainloop()
