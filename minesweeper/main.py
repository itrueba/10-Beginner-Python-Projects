import random
# Creamos un objeto para que represente un tablero

class Board:
    # Inicializacion de la clase 
    def __init__(self, dim_size, num_boms):
        # Definimos las dimensiones del tablero y el numero de bombas
        self.dim_size = dim_size
        self.num_bombs = num_boms

        # Creamos el tablero
        self.board = self.make_new_board()        

        # Conjunto para registrar todas las casillas ya excavadas
        self.dug = set() # Si excavamos en la 0,0 - self.dug = {(0,0)}

    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        
        bombs_planted = 0

        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == "*":
                continue

            board[row][col] = "*"
            bombs_planted +=1

        return board

# Jugar al juego
def play(dim_size = 10, num_bombs = 10):
    # Paso 1: Crear el tablero y colocar las bombas

    # Paso 2: Enseñar el tablero y preguntar al jugador que elija casilla 

    # Paso 3a: Si la casilla contiene una bomba, el juego termina
    
    # Paso 3b: So la casilla no es una bomba, hacer recursividad hasta que este pegado a una

    # Paso 4: Repetir los pasos 2 - 3a - 3b hasta que no queden bombas. El jugador ha ganado

    
    pass