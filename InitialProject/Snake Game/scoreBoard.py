from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("C:/Users/spanta6/OneDrive - DXC Production/Desktop/Python/Python/InitialProject/Snake Game/Data.txt") as data :
            self.high_score=int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score} " , align= ALIGNMENT, font= FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align= ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open( "C:/Users/spanta6/OneDrive - DXC Production/Desktop/Python/Python/InitialProject/Snake Game/Data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def count(self):
        self.score += 1
        self.update_scoreboard()

