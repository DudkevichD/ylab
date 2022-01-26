positions_department_list = [
    (2, 5),
    (5, 2),
    (6, 6),
    (8, 3),
    (0, 2)
    ]

positions_post = (0, 2)


def get_distance(position_1, position_2):
    distance = ((position_1[0] - position_2[0]) ** 2 + (position_1[1] - position_2[1]) ** 2) ** 0.5
    return distance


distance = 100
steps = []
all_distance = []


def search_nearest_position(position_1, position_list):
    global distance, steps
    for position in positions_department_list:
        q = get_distance(position_1, position)
        if get_distance(position_1, position) < distance:

            distance = get_distance(position_1, position)
            print(f'{position_1} -> {position}[{distance}]', end=' ')
            steps.append(position)
            all_distance.append(distance)
            position_list.remove(position)
            distance = 100
            if position_list == []:
                return
            else:
                search_nearest_position(position, position_list)


search_nearest_position(positions_post, positions_department_list)

print('=', sum(all_distance))
