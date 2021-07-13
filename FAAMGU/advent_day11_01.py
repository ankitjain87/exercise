# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.

# grid = [['L', '.', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L'],
#  ['L', 'L', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L'],
#  ['L', '.', 'L', '.', 'L', '.', '.', 'L', '.', '.'],
#  ['L', 'L', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L'],
#  ['L', '.', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L'],
#  ['L', '.', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L'],
#  ['.', '.', 'L', '.', 'L', '.', '.', '.', '.', '.'],
#  ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
#  ['L', '.', 'L', 'L', 'L', 'L', 'L', 'L', '.', 'L'],
#  ['L', '.', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L']]

grid = []
with open("/Users/jankit/Downloads/input.txt") as f:
    for i in f.readlines():
        line = list(i.strip())
        grid.append(line)


neighbours = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
m, n = len(grid), len(grid[0])
need_to_update = [1]

def get_adjacent_counts(i, j, state):
    count = 0
    adjacent = 0
    for item in neighbours:
        ni, nj = i + item[0], j + item[1]
        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] != '.':
            if grid[ni][nj] == state:
                count += 1
            adjacent += 1

    return count, adjacent


def update_grid(update_points, state):
    for x, y in update_points:
        grid[x][y] = state


while len(need_to_update) > 0:
    # print(grid)
    need_to_update = []
    # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "#":
                count, adjacent = get_adjacent_counts(i, j, "#")
                if count >= 4:
                    need_to_update.append((i, j))

    print("===50===")
    if need_to_update:
        update_grid(need_to_update, "L")
        need_to_update = []

    print("===55===")
    # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "L":
                count, adjacent = get_adjacent_counts(i, j, "L")
                # print(i, j, count, adjacent)
                if count == adjacent:
                    need_to_update.append((i, j))

    if need_to_update:
        update_grid(need_to_update, "#")


print(grid)

final_count = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == "#":
            final_count += 1

print(final_count)
