#!/usr/bin/python3

class Board:
    TAILLE_GRILLE_X = 10
    TAILLE_GRILLE_Y = 6

    def __init__(self):
        self.board = [[0 for _ in range(self.TAILLE_GRILLE_X)]
                for _ in range(self.TAILLE_GRILLE_Y)]
        self.__winner = None

    def check_winner(self, column: int) -> bool:
        lin, col = self.__which_line_to_add(column)+1, column
        # check for horizontal lines
        line = self.board[lin] # the line to test
        for shift in range(-3, 3):
            if col+shift+4 > self.TAILLE_GRILLE_X:
                break
            four_pieces = line[col+shift:col+shift+4]
            print(four_pieces)
            if len(set(four_pieces)) == 1 and four_pieces[0] != 0:
                self.__winner = four_pieces[0]
                return True
        # check for horizontal lines
        column = list(map(lambda x: x[col], self.board)) # the column to test
        for shift in range(-3, 3):
            if lin+shift+4 > self.TAILLE_GRILLE_X:
                break
            four_pieces = column[lin+shift:lin+shift+4]
            print(four_pieces)
            if len(set(four_pieces)) == 1 and four_pieces[0] != 0:
                self.__winner = four_pieces[0]
                return True
        # check for diagonal lines

    def play(self, player: int, column: int) -> bool:
        """Check if the movement is legal and the play it.
        If the movement is not legit, it will return False."""
        if self.is_column_full(column):
            return False
        self.__add_at_column(player, column)
        return True

    def __add_at_column(self, player: int, column: int) -> None:
        """Add the player's piece at the correct column."""
        self.board[self.__which_line_to_add(column)][column] = int(player)

    def __which_line_to_add(self, column: int) -> int:
        row_index = 0
        while self.board[row_index][column] == 0 and row_index < len(self.board) -1:
            row_index += 1
        return row_index - 1

    def is_column_full(self, column: int) -> bool:
        if all(map(lambda x: 0!=x[column], self.board)):
            return True
        return False

    def __str__(self):
        result = '┏' + "━"*self.TAILLE_GRILLE_X + '┓\n'
        for line in self.board:
            result += '┃'
            for cell in line:
                if cell == 0:
                    result += " "
                elif cell == 1:
                    result += "O"
                elif cell == 2:
                    result += "X"
                else:
                    result += "~"
            result += "┃\n"
        result += '┗' + "━"*self.TAILLE_GRILLE_X + '┛'
        return result


class Users:
    def __init__(self):
        self.__current = 0 # start with 0 but is changed when using __switch

    def __switch(self):
        if self.__current == 1:
            self.__current = 2
        else:
            self.__current = 1

    def current(self):
        self.__switch()
        return self.__current



if __name__ == "__main__":
    my_game = Board()
    users = Users()

    my_game.play(users.current(), 2)
    my_game.play(users.current(), 6)
    my_game.play(users.current(), 3)
    my_game.play(users.current(), 6)
    my_game.play(users.current(), 4)
    my_game.play(users.current(), 6)
    my_game.play(users.current(), 5)
    my_game.play(users.current(), 6)
    print(my_game)
    print(my_game.check_winner(6))


