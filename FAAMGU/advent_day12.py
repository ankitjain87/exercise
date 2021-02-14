from collections import defaultdict


direction_map = {
    'E': 0, 'S': 1, 'W': 2, 'N': 3,
    0 : 'E', 1: 'S', 2: 'W', 3: 'N' 
}

instructions = []
with open("/Users/jankit/Downloads/input.txt") as f:
    for i in f.readlines():
        line = i.strip()
        # print(line, type(line))
        ins, val = line[:1], int(line[1:])
        if ins in direction_map:
            ins = direction_map[ins]
        instructions.append((ins, val))


current_direction = 0
directions = ['E', 'S', 'W', 'N']
distance = defaultdict(int)

def update_direction(d, deg, current_direction):
    move = deg//90 + 4
    next_move = None
    # print(d, current_direction, move)
    if d == 'L':
        next_move = (current_direction - move) % 4
    else:
        next_move = (current_direction + move) % 4
    print(d, current_direction, move, next_move)
    return next_move


for d, val in instructions:
    if d == "F":
        distance[current_direction] += val
    elif d in ["L", "R"]:
        current_direction = update_direction(d, val, current_direction)
    else:
        distance[d] += val

print(current_direction, distance)
