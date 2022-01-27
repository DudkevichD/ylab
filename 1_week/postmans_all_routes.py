import itertools

positions_department_list = [
    (2, 5),
    (5, 2),
    (6, 6),
    (8, 3),
    ]

positions_post = (0, 2)
variants_path_list = list(itertools.permutations(positions_department_list, 4))
variants_path_dict = {}


def get_distance(position_1, position_2):
    distance = ((position_1[0] - position_2[0]) ** 2 + (position_1[1] - position_2[1]) ** 2) ** 0.5
    return distance


for variant in variants_path_list:
    variant = list(variant)
    variant.insert(0, positions_post)
    variant.append(positions_post)
    total_distance = 0
    path = ''

    for position in range(len(variant) - 1):
        distance = get_distance(variant[position], variant[position + 1])
        total_distance += distance
        path += f'{variant[position]} -> {variant[position + 1]}[{distance}] '
    variants_path_dict[total_distance] = path

variants_path_dict = dict(sorted(variants_path_dict.items(), key=lambda total_distance: float(total_distance[0])))

for total_distance, path in variants_path_dict.items():
    print(f'{path}= {total_distance}')
    break
