import players

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.winner = None

    def print_board(self):
        print("\nCurrent Board:")
        for i in range(3):
            start_index = i * 3
            end_index = start_index + 3
            row = []
            for idx in range(start_index, end_index):
                if self.board[idx] == ' ':
                    row.append(str(idx))
                else:
                    row.append(self.board[idx])
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        available_moves = []
        for i in range(len(self.board)):
            if self.board[i] == ' ':
                available_moves.append(i)
        return available_moves

    def get_empty_space(self):
        count = 0
        for slot in self.board:
            if slot == ' ':
                count += 1
        return count

    def make_move(self, position, player_letter):
        if self.board[position] == ' ':
            self.board[position] = player_letter
            if self.win_by_row(player_letter, position) or \
               self.win_by_column(player_letter, position) or \
               self.win_by_diagonal(player_letter, position):
                self.winner = player_letter
                return True
        return False

    def win_by_row(self, letter, position):
        row_index = position // 3
        start = row_index * 3
        end = start + 3
        for i in range(start, end):
            if self.board[i] != letter:
                return False
        return True

    def win_by_column(self, letter, position):
        column_index = position % 3
        for i in range(3):
            if self.board[column_index + i * 3] != letter:
                return False
        return True

    def win_by_diagonal(self, letter, position):
        first_diagonal = [0, 4, 8]
        second_diagonal = [2, 4, 6]

        is_first_diagonal = position in first_diagonal
        is_second_diagonal = position in second_diagonal

        if is_first_diagonal:
            for i in first_diagonal:
                if self.board[i] != letter:
                    break
            else:
                return True

        if is_second_diagonal:
            for i in second_diagonal:
                if self.board[i] != letter:
                    break
            else:
                return True

        return False


class Main:
    def __init__(self, game_board:TicTacToe, x_player:players.HumanPlayer, o_player:players.ComputerPlayer):
        self.game_board = game_board
        self.x_player = x_player
        self.o_player = o_player

    def play(self):
        while self.game_board.get_empty_space() > 0:
            self.game_board.print_board()

            x_player_input = self.x_player.get_move(self.game_board.available_moves())
            if self.game_board.make_move(x_player_input, self.x_player.player_letter):
                self.game_board.print_board()
                print("X player won!")
                return

            if self.game_board.get_empty_space() == 0:
                print("It's a tie!")
                return

            self.game_board.print_board()

            o_player_input = self.o_player.get_move(self.game_board.available_moves())
            if self.game_board.make_move(o_player_input, self.o_player.player_letter):
                self.game_board.print_board()
                print("O player won!")
                return

        self.game_board.print_board()
        print("It's a tie!")


game = Main(TicTacToe(), x_player=players.HumanPlayer("X"), o_player=players.ComputerPlayer("O"))
game.play()
