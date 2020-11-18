import os
from grid import Grid


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Game:
    def __init__(self):
        self.is_over = False
        self.grid = None
        self.player_turn = 1

    def start(self):
        clear()
        size = input("Grid Size: ")
        self.grid = Grid(int(size))

        while not self.is_over:
            clear()
            self.grid.paint()
            player = self.player_turn
            print(f"\nPlayer {player} Turn")
            column = input(f"Drop Location (0-{size}): ")
            
            if self.grid.play(column, player):
                # check for win
                # break if win               
                self.player_turn = 2 if player == 1 else 1

        print("Player {self.player_turn} Wins!!!")
        confirm = input("Press any key to play again (q to exit)")

        if confirm == "q":
            exit(0)

        self.start()

game = Game()
game.start()

