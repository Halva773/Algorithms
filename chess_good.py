alph = 'ABCDEFGH'
nums = '87654321'


class Chess_Board(object):
    def __init__(self):
        self.field = []
        for i in range(8):
            self.field.append(["* "] * 8)
        self.field[7] = [Rook("white", ["a", 1]), Knight("white", ["b", 1]), Bishop("white", ["c", 1]),
                         Queen("white", ["d", 1]), King("white", ["e", 1]), Bishop("white", ["f", 1]),
                         Knight("white", ["g", 1]), Rook("white", ["h", 1])]
        self.field[6] = [Pawn("white", ["a", 2]), Pawn("white", ["b", 2]), Pawn("white", ["c", 2]),
                         Pawn("white", ["d", 2]), Pawn("white", ["e", 2]), Pawn("white", ["f", 2]),
                         Pawn("white", ["g", 2]), Pawn("white", ["h", 2])]

        self.field[0] = [Rook("black", ["a", 8]), Knight("black", ["b", 8]), Bishop("black", ["c", 8]),
                         Queen("black", ["d", 8]), King("black", ["e", 8]), Bishop("black", ["f", 8]),
                         Knight("black", ["g", 8]), Rook("black", ["h", 8])]
        self.field[1] = [Pawn("black", ["a", 7]), Pawn("black", ["b", 7]), Pawn("black", ["c", 7]),
                         Pawn("black", ["d", 7]), Pawn("black", ["e", 7]), Pawn("black", ["f", 7]),
                         Pawn("black", ["g", 7]), Pawn("black", ["h", 7])]

    def draw(self):
        print('  ', *[a + ' ' for a in alph], '\n')
        for t in range(len(alph)):
            print(nums[t], end='')
            print(' ', *self.field[t])
        print('\n  ', *[a + ' ' for a in alph])

    def draw_hints(self, *args):
        copied = [i.copy() for i in self.field]
        for arg in args[0]:
            if copied[8 - arg[1]][ord(arg[0]) - 97] == "* ":
                copied[8 - arg[1]][ord(arg[0]) - 97] = ". "
            else:
                copied[8 - arg[1]][ord(arg[0]) - 97] = "᛭ "

        print('  ', *[a + ' ' for a in alph], '\n')
        for t in range(len(alph)):
            print(nums[t], end='')
            print(' ', *copied[t])
        print('\n  ', *[a + ' ' for a in alph])


class Figure(object):
    def __init__(self, color, position: list):
        self.color = color
        self.position = position

    def cross_step_by_step_check(self, start_col, start_line, chess_board, possible_positions):
        for i in range(start_col, 0, -1):
            if chess_board.field[start_line][i - 1] == "* ":
                possible_positions.append([chr(i - 1 + 97), 8 - start_line])
            elif chess_board.field[start_line][i - 1].color != self.color:
                possible_positions.append([chr(i - 1 + 97), 8 - start_line])
                break
            else:
                break

        for i in range(7 - start_col, 0, -1):
            if chess_board.field[start_line][-i] == "* ":
                possible_positions.append([chr(8 - i + 97), 8 - start_line])
            elif chess_board.field[start_line][-i].color != self.color:
                possible_positions.append([chr(8 - i + 97), 8 - start_line])
                break
            else:
                break

        for i in range(start_line, 0, -1):
            if chess_board.field[i - 1][start_col] == "* ":
                possible_positions.append([chr(start_col + 97), 9 - i])
            elif chess_board.field[i - 1][start_col].color != self.color:
                possible_positions.append([chr(start_col + 97), 9 - i])
                break
            else:
                break
        for i in range(7 - start_line, 0, -1):
            if chess_board.field[-i][start_col] == "* ":
                possible_positions.append([chr(start_col + 97), abs(i)])
            elif chess_board.field[-i][start_col].color != self.color:
                possible_positions.append([chr(start_col + 97), abs(i)])
                break
            else:
                break

    def diagonal_step_by_step_check(self, start_col, start_line, to_right_bottom, to_left_bottom, to_left_top,
                                    to_right_top, chess_board, possible_positions):
        for i in range(to_right_bottom):
            if chess_board.field[start_line + 1 + i][start_col + 1 + i] == "* ":
                possible_positions.append([chr(start_col + 1 + i + 97), abs(start_line + 1 + i - 8)])
            elif chess_board.field[start_line + 1 + i][start_col + 1 + i].color != self.color:
                possible_positions.append([chr(start_col + 1 + i + 97), abs(start_line + 1 + i - 8)])
                break
            else:
                break

        for i in range(to_left_bottom):
            if chess_board.field[start_line + 1 + i][start_col - 1 - i] == "* ":
                possible_positions.append([chr(start_col - 1 - i + 97), abs(start_line + 1 + i - 8)])
            elif chess_board.field[start_line + 1 + i][start_col - 1 - i].color != self.color:
                possible_positions.append([chr(start_col - 1 - i + 97), abs(start_line + 1 + i - 8)])
                break
            else:
                break

        for i in range(to_left_top):
            if chess_board.field[start_line - 1 - i][start_col - 1 - i] == "* ":
                possible_positions.append([chr(start_col - 1 - i + 97), abs(start_line - 1 - i - 8)])
            elif chess_board.field[start_line - 1 - i][start_col - 1 - i].color != self.color:
                possible_positions.append([chr(start_col - 1 - i + 97), abs(start_line - 1 - i - 8)])
                break
            else:
                break

        for i in range(to_right_top):
            if chess_board.field[start_line - 1 - i][start_col + 1 + i] == "* ":
                possible_positions.append([chr(start_col + 1 + i + 97), abs(start_line - 1 - i - 8)])
            elif chess_board.field[start_line - 1 - i][start_col + 1 + i].color != self.color:

                possible_positions.append([chr(start_col + 1 + i + 97), abs(start_line - 1 - i - 8)])
                break
            else:
                break


class Rook(Figure):
    def __init__(self, color, position: list):
        super().__init__(color, position)

    def __str__(self):
        if self.color == "white":
            return "♖"
        else:
            return "♜"

    def moving(self, chess_board):
        possible_positions = []
        start_col = ord(self.position[0]) - 97
        start_line = abs(self.position[1] - 8)

        self.cross_step_by_step_check(start_col, start_line, chess_board, possible_positions)

        return possible_positions


class Bishop(Figure):
    def __init__(self, color, position: list):
        super().__init__(color, position)

    def __str__(self):
        if self.color == "white":
            return "♗"
        else:
            return "♝"

    def moving(self, chess_board):
        possible_positions = []
        start_col = ord(self.position[0]) - 97
        start_line = abs(self.position[1] - 8)
        to_right_bottom = min(7 - start_col, 7 - start_line)
        to_right_top = min(7 - start_col, start_line)
        to_left_bottom = min(start_col, 7 - start_line)
        to_left_top = min(start_col, start_line)

        self.diagonal_step_by_step_check(start_col, start_line, to_right_bottom, to_left_bottom, to_left_top,
                                         to_right_top, chess_board, possible_positions)

        return possible_positions


class Queen(Figure):
    def __init__(self, color, position: list):
        super().__init__(color, position)

    def __str__(self):
        if self.color == "white":
            return "♕"
        else:
            return "♛"

    def moving(self, chess_board):
        possible_positions = []
        start_col = ord(self.position[0]) - 97
        start_line = abs(self.position[1] - 8)
        to_right_bottom = min(7 - start_col, 7 - start_line)
        to_right_top = min(7 - start_col, start_line)
        to_left_bottom = min(start_col, 7 - start_line)
        to_left_top = min(start_col, start_line)

        self.cross_step_by_step_check(start_col, start_line, chess_board, possible_positions)
        self.diagonal_step_by_step_check(start_col, start_line, to_right_bottom, to_left_bottom, to_left_top,
                                         to_right_top, chess_board, possible_positions)

        return possible_positions


class King(Figure):
    def __init__(self, color, position: list):
        super().__init__(color, position)

    def __str__(self):
        if self.color == "white":
            return "♔"
        else:
            return "♚"

    def moving(self, chess_board):
        possible_positions = []
        possible_positions.append([self.position[0], self.position[1] - 1])
        possible_positions.append([chr(ord(self.position[0]) - 1), self.position[1] - 1])
        possible_positions.append([chr(ord(self.position[0]) + 1), self.position[1] - 1])
        possible_positions.append([self.position[0], self.position[1] + 1])
        possible_positions.append([chr(ord(self.position[0]) - 1), self.position[1] + 1])
        possible_positions.append([chr(ord(self.position[0]) + 1), self.position[1] + 1])
        possible_positions.append([chr(ord(self.position[0]) - 1), self.position[1]])
        possible_positions.append([chr(ord(self.position[0]) + 1), self.position[1]])

        possible_positions = [n for n in possible_positions if n[1] > 0]
        possible_positions = [m for m in possible_positions if (
                chess_board.field[abs(m[1] - 8)][ord(m[0]) - 97] == '* ' or chess_board.field[abs(m[1] - 8)][
            ord(m[0]) - 97].color != self.color)]

        return possible_positions


class Pawn(Figure):
    def __init__(self, color, position: list):
        super().__init__(color, position)

    def __str__(self):
        if self.color == "white":
            return "♙"
        else:
            return "♟"

    def moving(self, chess_board):
        possible_positions = []
        start_col = ord(self.position[0]) - 97
        start_line = abs(self.position[1] - 8)
        if self.color == "white":
            if start_line == 6:
                if chess_board.field[start_line - 1][start_col] == "* ":
                    possible_positions.append([chr(start_col + 97), 8 - start_line + 1])
                    if chess_board.field[start_line - 2][start_col] == "* ":
                        possible_positions.append([chr(start_col + 97), 8 - start_line + 2])
            else:
                if chess_board.field[start_line - 1][start_col] == "* ":
                    possible_positions.append([chr(start_col + 97), 8 - start_line + 1])
            # ниже диагональные ходы
            if start_col != 0 and chess_board.field[start_line - 1][start_col - 1] != "* " and \
                    chess_board.field[start_line - 1][start_col - 1].color == "black":
                possible_positions.append([chr(start_col + 97 - 1), 8 - start_line + 1])
            if start_col != 7 and chess_board.field[start_line - 1][start_col + 1] != "* " and \
                    chess_board.field[start_line - 1][start_col + 1].color == "black":
                possible_positions.append([chr(start_col + 97 + 1), 8 - start_line + 1])

        if self.color == "black":
            if start_line == 1:
                if chess_board.field[start_line + 1][start_col] == "* ":
                    possible_positions.append([chr(start_col + 97), 8 - start_line - 1])
                    if chess_board.field[start_line + 2][start_col] == "* ":
                        possible_positions.append([chr(start_col + 97), 8 - start_line - 2])
            else:
                if chess_board.field[start_line + 1][start_col] == "* ":
                    possible_positions.append([chr(start_col + 97), 8 - start_line - 1])
            # ниже диагональные ходы
            if start_col != 0 and chess_board.field[start_line + 1][start_col - 1] != "* " and \
                    chess_board.field[start_line + 1][start_col - 1].color == "white":
                possible_positions.append([chr(start_col + 97 - 1), 8 - start_line - 1])
            if start_col != 7 and chess_board.field[start_line + 1][start_col + 1] != "* " and \
                    chess_board.field[start_line + 1][start_col + 1].color == "white":
                possible_positions.append([chr(start_col + 97 + 1), 8 - start_line - 1])
        return possible_positions


class Knight(Figure):
    def __init__(self, color, position: list):
        super().__init__(color, position)

    def __str__(self):
        if self.color == "white":
            return "♘"
        else:

            return "♞"

    def moving(self, chess_board):
        possible_positions = []
        for j in [u for u in range(8)]:
            for i in list('abcdefgh'):
                if (abs((ord(self.position[0]) - 97) - (ord(i) - 97)) == 1) and (abs(int(self.position[1]) - j) == 1):
                    if ((int(self.position[1]) - j) > 0):
                        possible_positions.append([i, j - 1])
                    else:
                        possible_positions.append([i, j + 1])

                elif (abs((ord(self.position[0]) - 97) - (ord(i) - 97)) == 2) and (abs(int(self.position[1]) - j) == 0):
                    possible_positions.append([i, j + 1])
                    possible_positions.append([i, j - 1])

        possible_positions = [n for n in possible_positions if n[1] > 0]
        possible_positions = [m for m in possible_positions if (
                chess_board.field[abs(m[1] - 8)][ord(m[0]) - 97] == '* ' or chess_board.field[abs(m[1] - 8)][
            ord(m[0]) - 97].color != self.color)]

        return possible_positions


class RK(Figure):
    def __init__(self, color, position: list):
        super().__init__(color, position)

    def __str__(self):
        if self.color == "white":
            return "☆"
        else:
            return "★"

    def moving(self, chess_board):
        possible_positions = []
        start_col = ord(self.position[0]) - 97
        start_line = abs(self.position[1] - 8)

        for j in [u for u in range(8)]:
            for i in list('abcdefgh'):
                if (abs((ord(self.position[0]) - 97) - (ord(i) - 97)) == 1) and (abs(int(self.position[1]) - j) == 1):
                    if ((int(self.position[1]) - j) > 0):
                        possible_positions.append([i, j - 1])
                    else:
                        possible_positions.append([i, j + 1])

                elif (abs((ord(self.position[0]) - 97) - (ord(i) - 97)) == 2) and (abs(int(self.position[1]) - j) == 0):
                    possible_positions.append([i, j + 1])
                    possible_positions.append([i, j - 1])

        possible_positions = [n for n in possible_positions if n[1] > 0]
        possible_positions = [m for m in possible_positions if (
                chess_board.field[abs(m[1] - 8)][ord(m[0]) - 97] == '* ' or chess_board.field[abs(m[1] - 8)][
            ord(m[0]) - 97].color != self.color)]

        self.cross_step_by_step_check(start_col, start_line, chess_board, possible_positions)

        return possible_positions


class BK(Figure):
    def __init__(self, color, position: list):
        super().__init__(color, position)

    def __str__(self):
        if self.color == "white":
            return "✧ "
        else:
            return "✦ "

    def moving(self, chess_board):
        possible_positions = []
        start_col = ord(self.position[0]) - 97
        start_line = abs(self.position[1] - 8)
        to_right_bottom = min(7 - start_col, 7 - start_line)
        to_right_top = min(7 - start_col, start_line)
        to_left_bottom = min(start_col, 7 - start_line)
        to_left_top = min(start_col, start_line)

        for j in [u for u in range(8)]:
            for i in list('abcdefgh'):
                if (abs((ord(self.position[0]) - 97) - (ord(i) - 97)) == 1) and (abs(int(self.position[1]) - j) == 1):
                    if ((int(self.position[1]) - j) > 0):
                        possible_positions.append([i, j - 1])
                    else:
                        possible_positions.append([i, j + 1])

                elif (abs((ord(self.position[0]) - 97) - (ord(i) - 97)) == 2) and (abs(int(self.position[1]) - j) == 0):
                    possible_positions.append([i, j + 1])
                    possible_positions.append([i, j - 1])

        possible_positions = [n for n in possible_positions if n[1] > 0]
        possible_positions = [m for m in possible_positions if (
                chess_board.field[abs(m[1] - 8)][ord(m[0]) - 97] == '* ' or chess_board.field[abs(m[1] - 8)][
            ord(m[0]) - 97].color != self.color)]

        self.diagonal_step_by_step_check(start_col, start_line, to_right_bottom, to_left_bottom, to_left_top,
                                         to_right_top, chess_board, possible_positions)

        return possible_positions


class B3(Figure):
    def __init__(self, color, position: list):
        super().__init__(color, position)

    def __str__(self):
        if self.color == "white":
            return "◇"
        else:
            return "◆"

    def moving(self, chess_board):
        possible_positions = []
        start_col = ord(self.position[0]) - 97
        start_line = abs(self.position[1] - 8)
        to_right_bottom = min(min(7 - start_col, 7 - start_line), 3)
        to_right_top = min(min(7 - start_col, start_line), 3)
        to_left_bottom = min(min(start_col, 7 - start_line), 3)
        to_left_top = min(min(start_col, start_line), 3)

        self.diagonal_step_by_step_check(start_col, start_line, to_right_bottom, to_left_bottom, to_left_top,
                                         to_right_top, chess_board, possible_positions)

        return possible_positions


class Game(object):
    def __init__(self, chess_board):
        self.chess_board = chess_board
        self.to_move = "white"
        self.checkmate = False
        self.zero_shashek = False

    def turn(self, to_move):
        self.chess_board.draw()

        coords = input("Введите координаты фигуры, которую хотите выбрать ").split(" ")
        col = ord(coords[0]) - 97
        line = abs(int(coords[1]) - 8)
        selected_figure = self.chess_board.field[line][col]

        while self.chess_board.field[line][col] == "* " or selected_figure.color != to_move:
            coords = input(f"В этой клетке нет фигуры цвета {to_move}, выберите клетку с фигурой этого цвета ").split(
                " ")
            col = ord(coords[0]) - 97
            line = abs(int(coords[1]) - 8)
            selected_figure = self.chess_board.field[line][col]

        while len(selected_figure.moving(self.chess_board)) == 0:
            coords = input("Эта фигура не может ходить, выберите другую ").split(" ")
            col = ord(coords[0]) - 97
            line = abs(int(coords[1]) - 8)
            selected_figure = self.chess_board.field[line][col]

        print()
        print(f"Эту фигуру можно переместить на одну из этих клеток - {selected_figure.moving(self.chess_board)}")
        print()

        self.chess_board.draw_hints(selected_figure.moving(self.chess_board))

        new_coords = input("Введите координаты куда вы хотите переместить фигуру ").split(" ")
        new_col = ord(new_coords[0]) - 97
        new_line = abs(int(new_coords[1]) - 8)
        print()

        while [chr(new_col + 97), 8 - new_line] not in selected_figure.moving(self.chess_board):
            new_coords = input("На эти координаты сходить нельзя, введите другие ").split(" ")
            new_col = ord(new_coords[0]) - 97
            new_line = abs(int(new_coords[1]) - 8)

        if isinstance(selected_figure, Pawn) and (new_line == 0 or new_line == 7):
            print("ферзь = Queen, ладья = Rook, слон = Bishop, конь = Knight")
            choice = input("Ваша пешка дошла до последней горизонтали, выберите фигуру для превращения ")
            while choice not in ["Queen", "Rook", "Bishop", "Knight"]:
                choice = input("Напишите название фигуры для превращения корректно ")
            selected_figure = eval(choice)(to_move, [new_coords[0], int(new_coords[1])])

        global can_be_en_passant
        global target
        can_be_en_passant = False
        target = [0, 0]
        if isinstance(selected_figure, Pawn) and abs(line - new_line) == 2:
            can_be_en_passant = True
            target = [new_line, new_col]

        if isinstance(selected_figure, Pawn) and abs(line - new_line) == 1 and abs(col - new_col) == 1 and \
                self.chess_board.field[new_line][new_col] == "* ":
            self.chess_board.field[line][new_col] = "* "

        if isinstance(selected_figure, Shahska) and abs(line - new_line) == 2 and abs(col - new_col) == 2:
            if line > new_line and col > new_col:
                self.chess_board.field[line - 1][col - 1] = "* "
            if line > new_line and col < new_col:
                self.chess_board.field[line - 1][col + 1] = "* "
            if line < new_line and col > new_col:
                self.chess_board.field[line + 1][col - 1] = "* "
            if line < new_line and col < new_col:
                self.chess_board.field[line + 1][col + 1] = "* "

        self.chess_board.field[line][col] = "* "
        self.chess_board.field[new_line][new_col] = selected_figure
        selected_figure.position = [new_coords[0], int(new_coords[1])]
        self.to_move = "black" if self.to_move == "white" else "white"

        number_of_kings = sum([isinstance(square, King) for line in self.chess_board.field for square in line])
        if number_of_kings == 1:
            self.checkmate = True
            self.chess_board.draw()
            print(f"Игра окончена! Победили - {to_move}")

        if set([square.color for line in self.chess_board.field for square in line if square != "* "]) == 1:
            self.zero_shashek = True
            self.chess_board.draw()
            print(f"Игра окончена! Победили - {to_move}")
        return


board1 = Chess_Board()
play = Game(board1)

while not play.checkmate:
    play.turn(play.to_move)