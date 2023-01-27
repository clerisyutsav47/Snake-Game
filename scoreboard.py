from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("data.txt", 'r') as file:
            self.high_score = int(file.read())
        self.write(f"Score: {self.score}           High Score: {self.high_score} ", False, ALIGNMENT, FONT)

    def reset_game(self):
        if self.score > self.high_score:
            with open("data.txt", 'w') as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
