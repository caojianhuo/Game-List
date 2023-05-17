import random

class player:
    def __init__(self,name):
        self.name = name
        self.gesture = ""
        self.intGesture = 0
    def choose_gesture(self):
        print("Choose your gesture:Rock, Paper, or Scissors")
        gesture = input()
        gestures = ["Rock", "Paper", "Scissors"]
        if gesture in gestures:
            print("You chose", gesture)
            self.gesture = gesture
            self.intGesture = gestures.index(gesture)
        else:
            print("Invalid input. Please try again.")
            self.choose_gesture()

class Human(player):
    def __init__(self, name):
        super().__init__(name)

class Computer(player):
    def __init__(self):
        super().__init__("Computer")
    def choose_gesture(self):
        gestures = ["Rock", "Paper", "Scissors"]
        gesture = random.choice(gestures)
        print("The computer chose", gesture)
        self.gesture = gesture
        self.intGesture = gestures.index(gesture)

class Judge():
    def __init__(self):
        self.player_one = ""
        self.player_two = ""
    def compare_gestures(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
        if (player_one.intGesture+1)%3 == player_two.intGesture:
            print(player_two.gesture, "win", player_one.gesture)   
            print(player_two.name, "wins!")
        elif (player_one.intGesture+2)%3 == player_two.intGesture:        
            print(player_one.gesture, "win", player_two.gesture)    
            print(player_one.name, "wins!")
        else:
            print("It's a tie!")

def main():
    again = "y"
    changePlayers = "y"
    while again == "y":
        if changePlayers == "y":
            name = input("Enter your name: ")
        player_one = Human(name)
        player_one.choose_gesture()
        computer = Computer()
        computer.choose_gesture()
        judge = Judge()
        judge.compare_gestures(player_one, computer)   
        again = input("Do you want to play again? (y/n): ") 
        if again == "n":
            changePlayers = input("Do you want to change players? (y/n): ")
            if changePlayers == "y":
                again = "y"
            else:
                print("Thanks for playing!")
                break
        else:    
            again = "y"
            changePlayers = "n"
            continue

if __name__ == "__main__":
    main()