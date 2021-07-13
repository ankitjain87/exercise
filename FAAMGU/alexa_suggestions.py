customer_location = (0,0)

def find_resturants(all_locations, nearest_restaurant):
    distance_map = {}
    for i, v in enumerate(all_locations):
        dist = v[0]^2 + v[1]^2
        if dist not in distance_map:
            distance_map[dist] = [i]
        else:
            distance_map[dist].append(i)

    output = []
    print(distance_map)
    keys = list(distance_map.keys())
    for key in sorted(keys):
        for point in distance_map[key]:
            if nearest_restaurant == 0:
                return output
            output.append(all_locations[point])
            nearest_restaurant -= 1

    return output

print(find_resturants([[1,2],[3,4],[1,-1]], 2))