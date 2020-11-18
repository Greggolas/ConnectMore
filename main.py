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
        self.is_over = False
        size = int(input("Grid Size: "))
        self.grid = Grid(int(size))

        while not self.is_over:
            clear()
            self.grid.paint()
            player = self.player_turn
            print(f"\nPlayer {player} Turn")
            column = input(f"Drop Location (0-{size-1}): ")
            
            if self.grid.play(column, player):
                # end on win confirmation
                self.is_over = self.grid.win_check()

                if not self.is_over:
                    self.player_turn = 2 if player == 1 else 1

        print(f"\nPlayer {self.player_turn} Wins!!!")
        print("Press Enter to play again (or type quit to exit)")
        confirm = input()

        if confirm == "quit":
            exit(0)

        self.start()

game = Game()
game.start()

