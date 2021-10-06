from turtle import Turtle

class ScoreBoard(Turtle):
    """here Turtle is class is inherited to ScoreBoard and generates an new
        turtle object to print score and GAME OVER texts over screen"""
    def __init__(self):
        super().__init__()
        self.up()
        self.ht()
        self.up()
        self.goto(0,270)
        self.color('white')
        self.score = 0
        self.refresh_score()
        
    
    def refresh_score(self):
        self.clear()
        self.write(f"score: {self.score}",align='center',font=("Courier", 18, "bold"))
    
    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write("GAME OVER",align='center',font=("Courier", 20, "bold"))
        self.goto(0,-50)
        self.write(f"Score: {self.score}",align='center',font=("Courier", 18, "bold"))