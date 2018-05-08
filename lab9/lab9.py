class Automat():

    def __init__(self, board, alive, iterations):
        self.board_width = board['w']
        self.board_height = board['h']
        self.alive_height = alive['w']
        self.alive_width = alive['h']
        self.iterations = iterations

        active_cells = []

        for x in range(self.alive_width):
            for y in range(self.alive_height):
                active_cells.append((x,y))

        board = [[False] * self.board_width for row in range(self.board_height)]

        for cell in active_cells:
            board[cell[1] + y][cell[0] + x] = True

        self.board=board

    def print_board(self):
        output = ''

        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if self.board[y][x]: output += ' 1'
                else: output += ' 0'
            output += '\n'

        print(output)


    def evolve(self):
        for generation in range(self.iterations):
            new_board = [[False] * self.board_width for row in range(self.board_height)]

            for y, row in enumerate(self.board):
                for x, cell in enumerate(row):
                    neighbours = self.get_neighbours(x, y)
                    previous_state = self.board[y][x]
                    should_live = neighbours == 3 or (neighbours == 2 and previous_state == True)
                    new_board[y][x] = should_live

            self.board = new_board
            self.print_board()

    def get_neighbours(self, x, y):

        self.iterations = 0

        for hor in [-1, 0, 1]:
            for ver in [-1, 0, 1]:
                if not hor == ver == 0 and (0 <= x + hor < self.board_width and 0 <= y + ver < self.board_height):
                    self.iterations += self.board[(y + ver) % self.board_height][(x + hor) % self.board_width]

        return self.iterations




board = { 'w': 10, 'h':10 }
alive = { 'w': 3, 'h':5 }

g = Automat(board, alive, 3)
g.print_board()
g.evolve()

class Vector3D():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, second_vector):
        if isinstance(second_vector, Vector3D):
            self.x += second_vector.x
            self.y += second_vector.y
            self.z += second_vector.z
            return self.get_str()
        else: raise ValueError("Needed another vector to add")

    def __sub__(self, second_vector):
        if isinstance(second_vector, Vector3D):
            self.x -= second_vector.x
            self.y -= second_vector.y
            self.z -= second_vector.z
            return self.get_str()
        else: raise ValueError("Needed another vector to substract")

    def __mul__(self, mul_by):
        if isinstance(mul_by, Vector3D):
            self.x *= mul_by.x
            self.y *= mul_by.y
            self.z *= mul_by.z
            return self.get_str()

        elif isinstance(mul_by, int):
            self.x *= mul_by
            self.y *= mul_by
            self.z *= mul_by
            return self.get_str()
        else: raise ValueError("Needed another vector or int to multiply")

    def __eq__(self, second_vector):
        if isinstance(second_vector, Vector3D):
            if self.x == second_vector.x and self.x == second_vector.x and self.x == second_vector.x:
                return "Vectors are equal"
            else: return "Vectors are not equal"
        else: raise ValueError("Needed another vector to compare")

    def __len__(self):
        return 3

    def __str__(self):
        return self.get_str()

    def get_str(self):
        return "Vector: [" + str(self.x) + ", " + str(self.y) + ", " +  str(self.z) + "]"

v1 = Vector3D(1, 2, 3)
v2 = Vector3D(1, 2, 3)
v3 = Vector3D(4, 5, 6)

print(str(v1))
print(str(v2))
print(str(v3))

print(len(v1))

print(v1 == v2)
print(v1 == v3)

print(v1 - v2)
print(v1 + v2)
print(v1 + v2)


print(v1 * 10)
print(v1 * v2)
