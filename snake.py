from turtle import Turtle


class Snake:
    """In this part of code,here is most of the logic is present"""
    def __init__(self):
        """here it initializes snake and creates it."""
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
    
    def create_snake(self):
        """for the first time the snake has 3 turtles which are separated by a distance of 20 paces"""
        for i in range(3):
            t = Turtle(shape='square')
            t.color('white')
            if i==0:
                t.color('green')
                t.shape('turtle')
            t.up()
            t.goto(x=(i*-20),y=0)
            self.snake.append(t)
     
    def extend(self):
        """here it extends the snake by 1 segment if it has eaten food
            """
        self.add_snake(self.snake[-1].position())
    
    def add_snake(self,position):
        """here each snake segment is appends to snake list"""
        t = Turtle(shape='square')
        t.color('white')
        t.up()
        t.goto(position)
        self.snake.append(t)


    def move(self):
        """here each of the segment is moved to position of segment that is infront of its position"""
        for i in range(len(self.snake)-1,0,-1):
            i_x_pos = self.snake[i-1].xcor()
            i_y_pos = self.snake[i-1].ycor()
            self.snake[i].goto(i_x_pos,i_y_pos) 
        self.snake[0].fd(20)
        # print(self.snake[0].heading())
    
    """here snake heading is chaned based on key stroke given"""
    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)
    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].seth(270)
    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].seth(180)
    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].seth(0)

