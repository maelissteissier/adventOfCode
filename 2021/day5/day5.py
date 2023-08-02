file = open('input.in', 'r')
lines_newline = file.readlines()
lines = [line.strip() for line in lines_newline]


def get_point_id(point_dict):
    return 'x' + str(point_dict['x']) + 'y' + str(point_dict['y'])


def add_point_covered(new_point, overlap):
    if overlap == 449:
        i = 9
    elif overlap > 449:
        i = 10
    new_overlap = False
    new_point_id = get_point_id(new_point)
    point_covered = points_covered.get(new_point_id)
    if point_covered is None:
        points_covered[new_point_id] = 1
    else:
        # need to count overlap only once
        new_overlap = True if point_covered == 1 else False
        points_covered[new_point_id] = point_covered + 1
    if overlap == 449 and new_overlap:
        i = 10
    return new_overlap

def count_overlap(points):
    count = 0
    for point in points:
        if points[point] > 1:
            count += 1
    return count


vectors = [[point.split(',') for point in line.split(' -> ')] for line in lines]
vectors_dict = [{'a': {'x': int(vec[0][0]), 'y':int(vec[0][1])}, 'b':{'x': int(vec[1][0]), 'y':int(vec[1][1])}, 'h': True if int(vec[0][1]) == int(vec[1][1]) else False, 'v': True if int(vec[0][0]) == int(vec[1][0]) else False} for vec in vectors]

# DEFI 1
# points_covered = {}
# overlap_points_count = 0
#
# for vec in vectors_dict:
#     # Add first point to covered points. (only if horizontal or vertical for 1st challenge)
#     # Return true if a new overlap has occured (for keeping count of overlaps)
#     if (vec['v'] or vec['h']) and add_point_covered(vec['a'], overlap_points_count):
#         overlap_points_count += 1
#     if vec['v']:
#         # calculate every points from a to b
#         y_a = vec['a']['y']
#         y_b = vec['b']['y']
#         vec_direction = y_a - y_b
#         while y_a != y_b:
#             y_a = y_a + 1 if vec_direction < 0 else y_a - 1
#             new_point = {'x': vec['a']['x'], 'y': y_a}
#             if add_point_covered(new_point, overlap_points_count):
#                 overlap_points_count += 1
#     elif vec['h']:
#         x_a = vec['a']['x']
#         x_b = vec['b']['x']
#         vec_direction = x_a - x_b
#         while x_a != x_b:
#             x_a = x_a + 1 if vec_direction < 0 else x_a - 1
#             new_point = {'x': x_a, 'y': vec['a']['y']}
#             if add_point_covered(new_point, overlap_points_count):
#                 overlap_points_count += 1
#
# print(overlap_points_count)


def count_overlap(points):
    count = 0
    for point in points:
        if points[point] > 1:
            count += 1



# DEFI 2

points_covered = {}
overlap_points_count = 0

for vec in vectors_dict:
    # Add first point to covered points.
    # Return true if a new overlap has occured (for keeping count of overlaps)
    if add_point_covered(vec['a'], overlap_points_count):
        overlap_points_count += 1
    if vec['v']:
        # calculate every points from a to b
        y_a = vec['a']['y']
        y_b = vec['b']['y']
        vec_direction = y_a - y_b
        while y_a != y_b:
            y_a = y_a + 1 if vec_direction < 0 else y_a - 1
            new_point = {'x': vec['a']['x'], 'y': y_a}
            if add_point_covered(new_point, overlap_points_count):
                overlap_points_count += 1
    elif vec['h']:
        x_a = vec['a']['x']
        x_b = vec['b']['x']
        vec_direction = x_a - x_b
        while x_a != x_b:
            x_a = x_a + 1 if vec_direction < 0 else x_a - 1
            new_point = {'x': x_a, 'y': vec['a']['y']}
            if add_point_covered(new_point, overlap_points_count):
                overlap_points_count += 1
    else:
        x_a = vec['a']['x']
        x_b = vec['b']['x']
        y_a = vec['a']['y']
        y_b = vec['b']['y']
        y_direction = y_a - y_b
        x_direction = x_a - x_b
        while x_a != x_b and y_a != y_b:
            y_a = y_a + 1 if y_direction < 0 else y_a - 1
            x_a = x_a + 1 if x_direction < 0 else x_a - 1
            new_point = {'x': x_a, 'y': y_a}
            if add_point_covered(new_point, overlap_points_count):
                overlap_points_count += 1


print(overlap_points_count)