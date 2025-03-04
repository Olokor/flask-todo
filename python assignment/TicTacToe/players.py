import random

class Player:
    def __init__(self, player_letter:str):
        self.player_letter = player_letter

    def get_move(self, board_current_state):...


class ComputerPlayer(Player):
    def __init__(self, player_letter:str):
        super().__init__(player_letter)

    def get_move(self, board_current_state:list):
        computer_position = random.choice(board_current_state)
        return computer_position

class HumanPlayer(Player):
    def __init__(self, player_letter:str):
        super().__init__(player_letter)

    def get_move(self, board_current_state:list)->int:
        player_move = None
        while True:
            input_move = input(f"{self.player_letter}'s turn, Enter your move (0-9): ")
            if self.check_user_input(input_move, board_current_state):
                player_move = int(input_move)
                break
            else:
                print("Please enter a valid move")
        return player_move
    def check_user_input(self, input_position:str, board_current_state:list)->bool:
        try:
            position = int(input_position)
            if 0 <= position <= 9 and position in board_current_state:
                return True
        except ValueError:
            return False



