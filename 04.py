class Warehouse:
    def __init__ (self, grid):
        self.grid = grid

    def get_adjacent_points(self, row, col):

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        R = len(self.grid)
        C = len(self.grid[0])

        for dr, dc in directions:
            new_r, new_c = row + dr, col + dc

            if 0 <= new_r < R and 0 <= new_c < C:
                yield (new_r, new_c)


    def count_adjacent_rolls(self, row, col):
        count = 0
        for r, c in self.get_adjacent_points(row, col):
            if grid[r][c] == "@":
                count += 1
        return count

    def get_less_than_n_adjacent(self, n: int):
        less_than_n = [
            (row, col)
            for row in range(len(self.grid))
            for col in range(len(self.grid[0]))
            if self.grid[row][col] == "@" and self.count_adjacent_rolls(row, col) < n
        ]

        return less_than_n

    def count_less_than_n_adjacent(self, n: int) -> int:
        return len(self.get_less_than_n_adjacent(n))
    
    def count_remove_until_unable(self, n:int) -> int:
        remove_count = 0
        while True:
            to_remove = self.get_less_than_n_adjacent(n)

            if not to_remove:
                break

            for row, col in to_remove:
                self.grid[row][col] = "x"

            remove_count += len(to_remove)

        return remove_count


if __name__ == "__main__":
    with open("inputs/04.txt") as f:
        grid = [[c for c in l.strip("\n")] for l in f.readlines()]
    
    warehouse = Warehouse(grid)
    print(len(grid), len(grid[0]))
    print("Part 01:")
    print(warehouse.count_less_than_n_adjacent(4))
    print("Part 02:")
    print(warehouse.count_remove_until_unable(4))
