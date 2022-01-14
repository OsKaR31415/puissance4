from users_gestion import Users

PLAYER_1_LOGO   = "\u001b[31m●\u001b[0m"
PLAYER_2_LOGO   = "\u001b[33m●\u001b[0m"
EMPTY_CELL_LOGO = "\u001b[38;5;233m█\u001b[0m"

def all_equal_and_non_zero(list_pawns: list[int]) -> bool:
    """Function to test if a list is made of elements that are all equal and
    different from 0."""
    if len(list_pawns) == 0:
        return False
    # if there is one zero, they can't be all equal *and non zero*
    if list_pawns[0] == 0:
        return False
    # if the set is only one element, they are all equal
    if len(set(list_pawns)) == 1:
        return True
    # else, they are different
    return False

class Board:
    def __init__(self, board_size_x: int =10, board_size_y: int =6):
        self.BOARD_SIZE_X = int(board_size_x)
        self.BOARD_SIZE_Y = int(board_size_y)
        self.board = [[0 for _ in range(self.BOARD_SIZE_X)]
                for _ in range(self.BOARD_SIZE_Y)]
        self.__winner = None

    def game_won(self, column: int) -> bool:
        """Method to test if the game has been won.
        If it is the case, it sets the __winner attribute to the winner's index.
        """
        # coordinates of the last added pawn
        lin, col = self.__which_line_to_add(column)+1, column

        # check for horizontal lines
        line = self.board[lin] # the line to test
        for shift in range(-3, 4):
            if col+shift+4 > self.BOARD_SIZE_X:
                break
            four_pawns = line[col+shift:col+shift+4]
            # print('-', four_pawns, col+shift, col+shift+4)
            if all_equal_and_non_zero(four_pawns):
                self.__winner = four_pawns[0]
                return True

        # check for vertical lines
        column = list(map(lambda x: x[col], self.board)) # the column to test
        for shift in range(-3, 4):
            if lin+shift+4 > self.BOARD_SIZE_X:
                break
            four_pawns = column[lin+shift:lin+shift+4]
            if len(four_pawns) != 4:
                continue
            # print('|', four_pawns, lin+shift, lin+shift+4)
            if all_equal_and_non_zero(four_pawns):
                self.__winner = four_pawns[0]
                return True

        # check for diagonal lines
        for shift in range(-3, 4):
            # \ diagonal
            try:
                four_pawns = [self.board[col+x+shift-4][lin+x+shift-4]
                        for x in range(4)]
            except IndexError:
                # print('.')
                continue
            if len(four_pawns) != 4:  # must be of length 4
                continue
            # print('\\', four_pawns,
            #         col+shift-4, lin+shift-4, '->', col+shift, lin+shift)
            if all_equal_and_non_zero(four_pawns):
                self.__winner = four_pawns[0]
                return False

            # / diagonal
            try:
                four_pawns = [self.board[col+x+shift][lin-x-shift]
                    for x in range(4)]
            except IndexError:
                # print('.')
                continue
            if len(four_pawns) != 4:  # must be of length 4
                continue
            # print('/', four_pawns,
            #         col+shift-4, lin-shift-4, '->', col+shift, lin-shift)
            if all_equal_and_non_zero(four_pawns):
                self.__winner = four_pawns[0]
                # print("✓")
                return True
        return False



    def play_if_legit(self, player: int, column: int) -> bool:
        """Check if the movement is legal and the play it.
        If the movement is not legit, it will return False."""
        if self.is_column_full(column):
            return False
        self.__add_at_column(player, column)
        return True

    def play(self, player: int, column: int) -> bool:
        """Play the movement if it is legit.
        Returns True if the game can continue, and False if one player has won.
        """
        self.play_if_legit(player, column)
        return not self.game_won(column)

    def __add_at_column(self, player: int, column: int) -> None:       
        """Add the player's pawn at the correct column."""
        self.board[self.__which_line_to_add(column)][column] = int(player)

    def __which_line_to_add(self, column: int) -> int:
        row_index = 0
        try:
            while self.board[row_index][column] == 0:
                row_index += 1
        except IndexError:
            pass
        # the correct line is the one before the IndexError
        return row_index - 1

    def is_column_full(self, column: int) -> bool:
        """Returns True if the givent column is full, False otherwise."""
        if all(map(lambda x: 0!=x[column], self.board)):
            return True
        return False

    def win_message(self):
        """Returns a simple message to show who is the winner."""
        winner_logo = (PLAYER_1_LOGO, PLAYER_2_LOGO)[self.__winner-1]
        return f"bravo, le joueur {winner_logo} à gagné !"

    def __str__(self):
        """Returns the grid properly formatter to be played."""
        result = '┏' + "━"*self.BOARD_SIZE_X + '┓\n'
        for line in self.board:
            result += '┃'
            for cell in line:
                if cell == 0:
                    result += EMPTY_CELL_LOGO
                elif cell == 1:
                    result += PLAYER_1_LOGO
                elif cell == 2:
                    result += PLAYER_2_LOGO
                else:
                    result += "~"
            result += "┃\n"
        result += '┣' + "━"*self.BOARD_SIZE_X + '┫\n'
        result += '┗'
        result += '0123456789abcdefghijklmnopqrstuvwxyz'[:self.BOARD_SIZE_X]
        result += '┛'
        return result


def main():
    print("""
┏━╸┏━┓┏┓╻┏┓╻┏━╸┏━╸╺┳╸   ╻ ╻
┃  ┃ ┃┃┗┫┃┗┫┣╸ ┃   ┃ ╺━╸┗━┫
┗━╸┗━┛╹ ╹╹ ╹┗━╸┗━╸ ╹      ╹
       by OsKaR31415
""")
    my_game = Board(14, 10)
    user = Users()
    continue_game = True
    while continue_game:
        print(my_game)
        column_to_play = int(input(f"player {user.current_logo()} > "), 36)
        if column_to_play < 0 or column_to_play > my_game.BOARD_SIZE_X -1:
            print("this is not a valid column !")
            continue
        continue_game = my_game.play(user.current(), column_to_play)
        user.switch()
    print(my_game)
    print(my_game.win_message())


if __name__ == "__main__":
    main()




