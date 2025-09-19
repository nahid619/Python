import turtle
import random
import time
import tkinter.messagebox as MessageBox

WIDTH, HEIGHT = 800, 600
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

class TurtleRaceGame:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(WIDTH, HEIGHT)
        self.screen.title("Turtle Race Game")
        self.turtles = []
        self.colors = []
        self.num_racers = 0

    def get_user_input(self):
        self.x= self.screen.textinput("welcome","do you want to play?(Y or N) ").lower()
        if self.x != "y":
            exit()

        while True:
            try:
                self.num_racers = int(self.screen.textinput("Number of Racers", "Enter the number of racers (2-10):"))
                if 2 <= self.num_racers <= 10:
                    break
                else:
                    self.re_input("Error", "Please enter a number between 2 and 10.")
            except (ValueError, TypeError):
                self.show_message("Error", "Invalid input. Try again.")

    def show_message(self, title, message):
        MessageBox.showinfo(title, message)
    
    def re_input(self, title, message):
        self.screen.textinput(title, message)

    def setup_turtles(self):
        self.colors = random.sample(COLORS, self.num_racers)
        spacing_x = WIDTH // (self.num_racers + 1)
        self.turtles = []
        
        for i, color in enumerate(self.colors):
            racer = turtle.Turtle()
            racer.color(color)
            racer.shape("turtle")
            racer.penup()
            racer.left(90)
            racer.setpos(-WIDTH // 2 + (i + 1) * spacing_x, -HEIGHT // 2 + 20)
            racer.pendown()
            self.turtles.append(racer)

    def countdown(self):
        countdown_turtle = turtle.Turtle()
        countdown_turtle.hideturtle()
        countdown_turtle.color("black")
        countdown_turtle.penup()
        countdown_turtle.setpos(0, HEIGHT // 2 - 50)
        countdown_turtle.write("Ready?", align="center", font=("Arial", 24, "bold"))
        time.sleep(1)
        
        for count in range(3, 0, -1):
            countdown_turtle.clear()
            countdown_turtle.write(f"{count}", align="center", font=("Arial", 36, "bold"))
            time.sleep(1)
        
        countdown_turtle.clear()
        countdown_turtle.write("Go!", align="center", font=("Arial", 24, "bold"))
        time.sleep(1)
        countdown_turtle.clear()

    def start_race(self):
        while True:
            for racer in self.turtles:
                distance = random.randint(1, 10)
                racer.forward(distance)
                if racer.ycor() >= HEIGHT // 2 - 10:
                    self.winner = self.colors[self.turtles.index(racer)]
                    self.index = self.turtles.index(racer)
                    return self.index, self.winner

    def replay_option(self):
        choice = self.screen.textinput("Replay?", "Do you want to play again? (yes/no):")
        return choice and choice.lower() == "yes"

    def run(self):
        while True:
            self.get_user_input()
            self.setup_turtles()
            self.countdown()
            index, winner = self.start_race()
            self.show_message("Winner", f"The winner is no. {index+1} turtle with color: {winner}!")
            
            if not self.replay_option():
                self.show_message("Goodbye!", "Thanks for playing the Turtle Race!")
                break

        self.screen.bye()

if __name__ == "__main__":
    game = TurtleRaceGame()
    game.run()
