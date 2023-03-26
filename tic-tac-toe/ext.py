""" КрестикИ х НоликИ -> Внешний модуль """
import random
import time


def get_tile_num_by_coords(x, y) -> int:
    app_size = 6
    """ Returns number of tile square by given coords """
    # bg_w, bg_h [64, 113]
    # px_w, px_h [0 1 2] -> 0: [5, 36], [20, 51], 1: [24, 36], [39, 51], 2: [43, 36], [58, 51]
    # px_w, px_h [3 4 5] -> 3: [5, 55], [20, 70], 4: [24, 55], [39, 70], 5: [43, 55], [58, 70]
    # px_w, px_h [6 7 8] -> 6: [5, 74], [20, 89], 7: [24, 74], [39, 89], 8: [43, 74], [58, 89]
    g = {
        0: [[5, 36], [20, 51]], 1: [[24, 36], [39, 51]], 2: [[43, 36], [58, 51]],
        3: [[5, 55], [20, 70]], 4: [[24, 55], [39, 70]], 5: [[43, 55], [58, 70]],
        6: [[5, 74], [20, 89]], 7: [[24, 74], [39, 89]], 8: [[43, 74], [58, 89]]
    }
    row, col = '-', '-'
    if y in range(g[0][0][1] * app_size, (g[0][1][1] + 1) * app_size):
        row = '0'
    elif y in range(g[3][0][1] * app_size, (g[3][1][1] + 1) * app_size):
        row = '1'
    elif y in range(g[6][0][1] * app_size, (g[6][1][1] + 1) * app_size):
        row = '2'

    if x in range(g[0][0][0] * app_size, (g[0][1][0] + 1) * app_size):
        col = '0'
    elif x in range(g[1][0][0] * app_size, (g[1][1][0] + 1) * app_size):
        col = '1'
    elif x in range(g[2][0][0] * app_size, (g[2][1][0] + 1) * app_size):
        col = '2'

    coords_dict = {
        '00': 0, '01': 1, '02': 2,
        '10': 3, '11': 4, '12': 5,
        '20': 6, '21': 7, '22': 8,
    }
    return coords_dict.get(row + col, -1)


def win_conditions(in_list) -> bool:
    """ Check win conditions """
    win_pattern = [
        {0,1,2}, {3,4,5}, {6,7,8},
        {0,3,6}, {1,4,7}, {2,5,8},
        {0,4,8}, {2,4,6}
    ]
    if len(in_list) >= 3:
        for i in win_pattern:
            if i == i.intersection(set(in_list)):
                return True
    return False


def ai_next_move(in_priority_moves_dict) -> int:
    """ AI core """
    # time.sleep(0.1)
    priority_moves = in_priority_moves_dict
    next_move = None
    # 1st use priority
    for key, value in priority_moves.items():
        if priority_moves[key]:
            if len(priority_moves[key]) == 1:
                return priority_moves[key][0]
            else:
                return random.choice(
                    list(
                        set(priority_moves[key]).intersection(priority_moves['4'])
                    ))


def get_occupied_tiles(in_x_list, in_o_list) -> set:
    """ AI part """
    x = set(in_x_list)
    o = set(in_o_list)
    occupied_tiles = x.union(o)
    return occupied_tiles


def get_smart_moves(in_x_list, in_o_list, in_occupied_tiles_set) -> dict:
    """ AI part """
    smart_moves_dict = {
        (0,1,2): [0, 0], (3,4,5): [0, 0], (6,7,8): [0, 0], (0,3,6): [0, 0],
        (1,4,7): [0, 0], (2,5,8): [0, 0], (0,4,8): [0, 0], (2,4,6): [0, 0],
    }
    x = set(in_x_list)
    o = set(in_o_list)
    occupied_tiles = in_occupied_tiles_set
    for num in x:
        for key, val in smart_moves_dict.items():
            if num in key:
                smart_moves_dict[key][0] += 1
    for num in o:
        for key, val in smart_moves_dict.items():
            if num in key:
                smart_moves_dict[key][1] += 1
    return smart_moves_dict


def get_priority_moves(in_x_list, in_o_list, in_smart_moves_dict, in_occupied_tiles_set) -> dict:
    """ AI part """
    smart_moves = in_smart_moves_dict
    priority_moves = {'1': [], '2': [], '3': [], '4': []}
    x = set(in_x_list)
    o = set(in_o_list)
    occupied_tiles = in_occupied_tiles_set
    # Create priority
    # 0 1 2
    # 3 4 5
    # 6 7 8
    # 1st -> occupy 4
    if 4 not in occupied_tiles:
        priority_moves['1'] = [4]
    # 2nd -> finish 'o' available moves when [0, 2]
    for key, value in smart_moves.items():
        if value == [0, 2]:
            priority_moves['2'].append(key[0])
            priority_moves['2'].append(key[1])
            priority_moves['2'].append(key[2])
    # 3rd -> prevent 'x' from available moves when [2, 0]
    for key, value in smart_moves.items():
        if value == [2, 0]:
            priority_moves['3'].append(key[0])
            priority_moves['3'].append(key[1])
            priority_moves['3'].append(key[2])
    # 4th -> collect any free tiles
    for tile_num in range(9):
        if tile_num not in occupied_tiles:
            priority_moves['4'].append(tile_num)
    return priority_moves
