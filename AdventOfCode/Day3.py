def main():
    filename = (
        "/Users/arthur/Documents/GitHub/LeetcodeAdventure/AdventOfCode/day3input.txt"
    )
    with open(filename, "r") as file_object:
        # Read the file into a 2D grid (list of lists)
        grid = [list(line.strip()) for line in file_object]

    sum_of_parts = 0
    checked_positions = set()

    # Function to check adjacent cells for symbols
    def has_adjacent_symbol(row, col):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                adj_row, adj_col = row + dy, col + dx
                if 0 <= adj_row < len(grid) and 0 <= adj_col < len(grid[adj_row]):
                    if (
                        not grid[adj_row][adj_col].isdigit()
                        and grid[adj_row][adj_col] != "."
                    ):
                        return True
        return False

    # Iterate over each cell in the grid
    for row in range(len(grid)):
        col = 0
        while col < len(grid[row]):
            if grid[row][col].isdigit():
                start_col = col
                # Find the full number
                while col < len(grid[row]) and grid[row][col].isdigit():
                    col += 1
                number = int("".join(grid[row][start_col:col]))

                # Check if any part of the number is adjacent to a symbol
                if any(has_adjacent_symbol(row, c) for c in range(start_col, col)):
                    if (row, start_col, col) not in checked_positions:
                        sum_of_parts += number
                        checked_positions.add((row, start_col, col))
            else:
                col += 1

    print(sum_of_parts)


def main_modified_to_find_gears():
    filename = (
        "/Users/arthur/Documents/GitHub/LeetcodeAdventure/AdventOfCode/day3input.txt"
    )

    with open(filename, "r") as file_object:
        # Read the file into a 2D grid (list of lists)
        grid = [list(line.strip()) for line in file_object]

    sum_of_parts = 0

    # Function to extract the full number starting from a given position
    def extract_full_number(row, col):
        # Trace back to the start of the number
        original_col = col
        while col > 0 and grid[row][col - 1].isdigit():
            col -= 1

        start_col = col
        while col < len(grid[row]) and grid[row][col].isdigit():
            col += 1

        return int("".join(grid[row][start_col:col])), (row, start_col, col - 1)

    # Function to find and return two entire numbers adjacent to '*'
    def find_adjacent_numbers(row, col):
        adjacent_numbers = []
        checked_local_positions = set()

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                adj_row, adj_col = row + dy, col + dx
                if 0 <= adj_row < len(grid) and 0 <= adj_col < len(grid[adj_row]):
                    if (
                        grid[adj_row][adj_col].isdigit()
                        and (adj_row, adj_col) not in checked_local_positions
                    ):
                        number, pos = extract_full_number(adj_row, adj_col)
                        if pos not in checked_local_positions:
                            adjacent_numbers.append(number)
                            checked_local_positions.add(pos)
                            if len(adjacent_numbers) == 2:
                                return adjacent_numbers

        return []  # Return empty list if not exactly two numbers found

    # Iterate over each cell in the grid
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "*":
                adjacent_numbers = find_adjacent_numbers(row, col)
                print(adjacent_numbers)
                if len(adjacent_numbers) == 2:
                    product_of_adjacent = adjacent_numbers[0] * adjacent_numbers[1]
                    sum_of_parts += product_of_adjacent

    print(sum_of_parts)


if __name__ == "__main__":
    main_modified_to_find_gears()
