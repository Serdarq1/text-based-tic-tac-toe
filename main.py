import csv

game_over = False

player1 = "X"
player2 = "O"

with open("./scoreboard.csv", newline="") as f:
    rows = list(csv.reader(f))
player1_wins, player2_wins = map(int, rows[0])

player = player1

grid = list("123456789")
chosen_grids = []

# Each tuple defines a win if all cells in tuple contain players mark.
winning_combos = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)

def print_grid():
    print("\n", " | ".join(grid[:3]))
    print("---+---+---")
    print("", " | ".join(grid[3:6]))
    print("---+---+---")
    print("", " | ".join(grid[6:]))

start_game = input('Press 1 to play the game. Press 2 to see the scores: ')
while int(start_game) != 1:
    if start_game == '2':
        print(f"Player 1: {player1_wins} \n Player 2: {player2_wins}")
    start_game = input('Press 1 to play the game. Press 2 to see the scores: ')


def play_game(player, game_over):
    """Starts and plays the game."""
    while not game_over:
        grid_num = input("Enter a grid number: ")
        
        try:
            grid_num_to_int = int(grid_num) - 1
        except Exception as e:
            print("Please enter a number.")
            continue

        if grid_num_to_int < 0 or grid_num_to_int > 9:
            print("The grid number should be between 1 and 9.")

        elif grid[grid_num_to_int] not in chosen_grids:
            grid[grid_num_to_int] = player
            if player == player1:
                player = player2
            else:
                player = player1
            chosen_grids.append(grid[grid_num_to_int])
            print_grid()
        else:
            print("You can't overwrite a grid.")

        if has_winner(grid, player1_wins, player2_wins):
            game_over = True
        elif is_board_full(grid):
            print("It's a draw")
            game_over = True


def has_winner(grid, player1_wins, player2_wins):
    x_indexes = [i for i, val in enumerate(grid) if val == 'X']
    y_indexes = [i for i, val in enumerate(grid) if val == 'O']
     
    for combo in winning_combos:
        if all(i in x_indexes for i in combo):
            player1_wins += 1
            rows[0] = [str(player1_wins), str(player2_wins)]
            with open("./scoreboard.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(rows)
            print("Player 1 wins!")
            return True
        elif all(i in y_indexes for i in combo):
            player2_wins += 2
            rows[0] = [str(player1_wins), str(player2_wins)]
            with open("./scoreboard.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(rows)
            print("Player 2 wins!")
            return True
        
def is_board_full(grid):
    return all(cell in {'X', 'O'} for cell in grid)
        
     
print('Welcome to Tic Tac Toe! ')
print_grid()
play_game(player, game_over)
