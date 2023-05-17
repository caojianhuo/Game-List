from flask import Flask, render_template, request
from random import choice

app = Flask(__name__, template_folder='templates')

class Player:
    def __init__(self, name):
        self.name = name
        self.gesture = ""
        self.intGesture = 0

    def choose_gesture(self):
        gestures = ["Rock", "Paper", "Scissors"]
        gesture = request.form["gesture"]
        if gesture in gestures:
            self.gesture = gesture
            self.intGesture = gestures.index(gesture)
        else:
            return "Invalid input. Please try again."

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

class Computer(Player):
    def __init__(self):
        super().__init__("Computer")

    def choose_gesture(self):
        gestures = ["Rock", "Paper", "Scissors"]
        gesture = choice(gestures)
        self.gesture = gesture
        self.intGesture = gestures.index(gesture)

class Judge:
    def __init__(self):
        self.player_one = ""
        self.player_two = ""

    def compare_gestures(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
        if (player_one.intGesture + 1) % 3 == player_two.intGesture:
            return f"{player_two.gesture} wins against {player_one.gesture}. {player_two.name} wins!"
        elif (player_one.intGesture + 2) % 3 == player_two.intGesture:
            return f"{player_one.gesture} wins against {player_two.gesture}. {player_one.name} wins!"
        else:
            return "It's a tie!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/404')
def game():
    return render_template('game.html')

@app.route('/404/result', methods=['POST'])
def game_result():
    human = Human("Human")
    computer = Computer()
    human.choose_gesture()
    computer.choose_gesture()
    judge = Judge()
    result = judge.compare_gestures(human, computer)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.debug = True
    app.run()
