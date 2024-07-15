def sliding_tile_puzzle():
    # Initialize the puzzle grid (0 represents the empty space)
    puzzle = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def display_puzzle():
        for row in puzzle:
            print(" ".join(str(tile) for tile in row))
        print()

    def get_empty_position():
        for i in range(3):
            for j in range(3):
                if puzzle[i][j] == 0:
                    return i, j

    def move_tile(direction):
        empty_i, empty_j = get_empty_position()
        if direction == "left" and empty_j < 2:
            puzzle[empty_i][empty_j], puzzle[empty_i][empty_j + 1] = puzzle[empty_i][empty_j + 1], puzzle[empty_i][empty_j]
        # Implement other directions (up, down, right) similarly

    # Shuffle the puzzle (you can customize this step)
    # ...

    print("Welcome to the Sliding Tile Puzzle!")
    display_puzzle()

    while True:
        move = input("Enter direction (left/right/up/down): ")
        move_tile(move)
        display_puzzle()

        # Check if the puzzle is solved (ascending order)
        if all(puzzle[i][j] == i * 3 + j + 1 for i in range(3) for j in range(3)):
            print("Congratulations! The door unlocks.")
            break

# Call the function
sliding_tile_puzzle()
