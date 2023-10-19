import random

# Fungsi untuk membuat papan permainan dengan lebar yang diinputkan
def create_board(width):
    return [['.' for _ in range(width)] for _ in range(width)]

# Fungsi untuk menghasilkan posisi acak untuk bidak dan goal
def generate_positions(board):
    positions = set()
    while True:
        x = random.randint(0, len(board) - 1)
        y = random.randint(0, len(board) - 1)
        if (x, y) not in positions:
            positions.add((x, y))
        if len(positions) == 1:
            break
    return positions

# Fungsi untuk mencetak papan permainan
def print_board(board, current_pos, goal_pos):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (row, col) == current_pos:
                print('A', end=' ')
            elif (row, col) == goal_pos:
                print('O', end=' ')
            else:
                print(board[row][col], end=' ')
        print()

# Fungsi untuk mengecek apakah pemain menang atau kalah
def is_game_won(current_pos, goal_pos):
    return current_pos == goal_pos

# Fungsi utama untuk memainkan permainan
def play_game(width):
    board = create_board(width)
    goal_position = generate_positions(board).pop()
    current_position = random.choice(list(generate_positions(board)))

    print("Selamat datang di permainan!")
    print("Tujuan permainan adalah mencapai goal (O). Anda memiliki 3 langkah.")

    moves = 0

    while moves < 3:
        print_board(board, current_position, goal_position)
        direction = input("Pilih arah (w/a/s/d) atau ketik 'keluar' untuk berhenti: ").lower()
        
        if direction == 'keluar':
            print("Terima kasih telah bermain!")
            return  # Kembali dari permainan

        if direction not in ['w', 'a', 's', 'd']:
            print("Arah tidak valid.")
            continue

        if direction == 'w':
            new_position = (current_position[0] - 1, current_position[1])
        elif direction == 'a':
            new_position = (current_position[0], current_position[1] - 1)
        elif direction == 's':
            new_position = (current_position[0] + 1, current_position[1])
        elif direction == 'd':
            new_position = (current_position[0], current_position[1] + 1)

        if 0 <= new_position[0] < width and 0 <= new_position[1] < width:
            current_position = new_position
            moves += 1

            if is_game_won(current_position, goal_position):
                print("Selamat! Anda menang!")
                return
    else:
        print("Maaf, Anda kalah!")

# Fungsi untuk memainkan permainan lagi atau keluar
def main():
    while True:
        board_width = input("Masukkan lebar papan permainan atau ketik 'keluar' untuk berhenti: ")
        if board_width == 'keluar':
            print("Terima kasih telah bermain!")
            break
        try:
            board_width = int(board_width)
            play_game(board_width)
            play_again = input("Main lagi? (ya/tidak): ").lower()
            if play_again != 'ya':
                break
        except ValueError:
            print("Masukan tidak valid. Masukkan angka sebagai lebar papan.")

if __name__ == "__main__":
    main()
