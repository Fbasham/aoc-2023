with open('data.txt') as f:
    a = f.read().splitlines()


a = '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533'''


def find_minimum_heat_loss(grid):
    rows, cols = len(grid), len(grid[0])

    # Create a 4D array to store the minimum heat loss for each cell, direction, and consecutive count
    dp = [[[[float('inf')] * 4 for _ in range(4)] for _ in range(cols)] for _ in range(rows)]

    # Initialize the starting point for the first direction and consecutive count
    dp[0][0][0][0] = grid[0][0]

    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            for k in range(4):  # Current direction
                for l in range(4):  # Consecutive count
                    # Check the three possible directions (left, up, and diagonal up-left)
                    for d in range(1, 4):
                        ni, nj = i - d if k == 0 else i, j - 1 if k == 0 else j - d
                        if 0 <= ni < rows and 0 <= nj < cols:
                            # Update the minimum heat loss, direction, and consecutive count
                            if l < 3:
                                dp[i][j][(k + 1) % 4][l + 1] = min(dp[i][j][(k + 1) % 4][l + 1], dp[ni][nj][k][l] + grid[i][j])
                            dp[i][j][(k + 1) % 4][0] = min(dp[i][j][(k + 1) % 4][0], dp[ni][nj][k][l] + grid[i][j])

    # The minimum heat loss is at the bottom-right corner for any direction and consecutive count
    result = min(dp[rows - 1][cols - 1][d][l] for d in range(4) for l in range(4))
    
    # Check if the result is finite, return result if so, otherwise return -1
    return result if result != float('inf') else -1

# Example grid
grid = [
    [2, 4, 1, 3, 4, 3, 2, 3, 1, 1, 3, 2, 3],
    [3, 2, 1, 5, 4, 5, 3, 5, 3, 5, 6, 2, 3],
    [3, 2, 5, 5, 2, 4, 5, 6, 5, 4, 2, 5, 4],
    [3, 4, 4, 6, 5, 8, 5, 8, 4, 5, 4, 5, 2],
    [4, 5, 4, 6, 6, 5, 8, 7, 8, 5, 3, 6, 2],
    [1, 4, 3, 8, 5, 9, 8, 7, 9, 8, 4, 5, 4],
    [4, 4, 5, 7, 8, 7, 6, 9, 8, 7, 7, 6, 6],
    [3, 6, 3, 7, 8, 7, 7, 9, 7, 9, 6, 5, 3],
    [4, 6, 5, 4, 9, 6, 7, 9, 8, 8, 7, 8, 7],
    [4, 5, 6, 4, 6, 7, 9, 9, 8, 8, 8, 7, 4],
    [1, 2, 2, 4, 6, 8, 6, 6, 5, 5, 6, 3, 5],
    [2, 5, 4, 6, 5, 4, 8, 8, 8, 7, 7, 5, 3],
    [4, 3, 2, 2, 6, 7, 4, 6, 5, 5, 3, 3, 3]
]

result = find_minimum_heat_loss(grid)
print(result)
