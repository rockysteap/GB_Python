""" КрестикИ х НоликИ -> Основной модуль """
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from ext import *

# Main theme colors -> bg: #a8605d, bg outline: #654053, txt: #d1a67e

app_size = 6
# 64x113 - main_bg (x6 384x678)
app_w = 64 * app_size
app_h = 113 * app_size

# 16x16 - tile
tile_w = 16 * app_size
tile_h = 16 * app_size

# 26x5 - turn info
turn_info_size = 5
turn_info_w = 26 * turn_info_size
turn_info_h = 5 * turn_info_size

# 27x5 - mode info
mode_info_size = 4
mode_info_w = 27 * mode_info_size
mode_info_h = 5 * mode_info_size

# 25x7 - btn
menu_btn_size = 4
menu_btn_w = 25 * menu_btn_size
menu_btn_h = 7 * menu_btn_size

game_button_size = 3
game_btn_w = 25 * game_button_size
game_btn_h = 7 * game_button_size
restart_btn_w = 40 * game_button_size
restart_btn_h = 7 * game_button_size

# 35x11 - win_info
win_info_size = 8
win_info_w = 35 * win_info_size
win_info_h = 11 * win_info_size

# Create app window
root = Tk()
root.title('КрестикИ x НоликИ')
root.iconbitmap('./images/favicon.ico')
root.geometry("384x678+800+300")
root.resizable(width=False, height=False)


def load_images():
    """ Resize images using pillow lib """
    # Assets from https://m1k3-dev.itch.io/tic-tac-toe-asset-pack
    image_list = []
    # Paths
    p_bg = ['./images/bg_menu.gif', './images/bg_game.gif']
    p_btn_menu = ['./images/btn_menu_play.png', './images/btn_menu_quit.png', './images/year.gif']
    p_btn_game = ['./images/btn_game_pvp.png', './images/btn_game_vsai.png', './images/btn_game_restart.png']
    p_tile = ['./images/tile_x.gif', './images/tile_o.gif', './images/tile_sq.gif']
    p_turn_info = ['./images/info_turn_x.gif', './images/info_turn_o.gif']
    p_mode_info = ['./images/btn_game_pvp.png', './images/btn_game_vsai.png']
    win = ['./images/win_x.gif', './images/win_o.gif', './images/win_draw.gif']
    for path in p_bg:
        image_list.append(ImageTk.PhotoImage(Image.open(path).resize((app_w, app_h))))
    for path in p_btn_menu:
        image_list.append(ImageTk.PhotoImage(Image.open(path).resize((menu_btn_w, menu_btn_h))))
    for path in p_btn_game:
        if 'restart' in path:
            image_list.append(ImageTk.PhotoImage(Image.open(path).resize((restart_btn_w, restart_btn_h))))
        else:
            image_list.append(ImageTk.PhotoImage(Image.open(path).resize((game_btn_w, game_btn_h))))
    for path in p_tile:
        image_list.append(ImageTk.PhotoImage(Image.open(path).resize((tile_w, tile_h))))
    for path in p_turn_info:
        image_list.append(ImageTk.PhotoImage(Image.open(path).resize((turn_info_w, turn_info_h))))
    for path in p_mode_info:
        image_list.append(ImageTk.PhotoImage(Image.open(path).resize((mode_info_w, mode_info_h))))
    for path in win:
        image_list.append(ImageTk.PhotoImage(Image.open(path).resize((win_info_w, win_info_h))))
    return image_list


# Parse image list to global vars
i_menu = load_images()[0]
i_bg = load_images()[1]
i_btn_play = load_images()[2]
i_btn_quit = load_images()[3]
i_year = load_images()[4]
i_btn_pvp = load_images()[5]
i_btn_vsai = load_images()[6]
i_btn_restart = load_images()[7]
i_x = load_images()[8]
i_o = load_images()[9]
i_tile = load_images()[10]
i_info_turn_x = load_images()[11]
i_info_turn_o = load_images()[12]
i_info_pvp = load_images()[13]
i_info_vsai = load_images()[14]
i_win_x = load_images()[15]
i_win_o = load_images()[16]
i_win_no_moves = load_images()[17]
# End of images parse


def render_menu():
    """ Initial menu """
    menu_bg = Label(root, image=i_menu)
    menu_bg.place(x=0, y=0, relwidth=1, relheight=1)

    # Play button
    mm_btn_play = Button(root, image=i_btn_play, bg='#d1a67e', activebackground='#a8605d',
                         command=mm_btn_play_func)
    mm_btn_play.place(x=(app_w / 2 - menu_btn_w / 2), y=(app_h / 2 - menu_btn_h / 2))
    # Quit button
    mm_btn_quit = Button(root, image=i_btn_quit, bg='#d1a67e', activebackground='#a8605d',
                         command=mm_btn_quit_func)
    mm_btn_quit.place(x=(app_w / 2 - menu_btn_w / 2), y=(app_h / 2 + menu_btn_h))
    # Year button
    mm_btn_year = Button(root, image=i_year, bg='#d1a67e', highlightthickness=0, bd=0, activebackground='#a8605d',
                         command=mm_btn_year_func)
    mm_btn_year.place(x=(app_w / 2 - menu_btn_w / 2), y=(app_h / 2 + menu_btn_h * 10.3))

    out_render_menu_var_list = [menu_bg, mm_btn_play, mm_btn_quit]
    return out_render_menu_var_list


def mm_btn_play_func():
    """ Play button command """
    game_is_running()


def mm_btn_quit_func():
    """ Quit button command """
    response = messagebox.askyesno('КрестикИ х НоликИ', 'Желаете выйти?')
    if response:
        app_destroy()


def mm_btn_year_func():
    messagebox.showinfo('Secret button',
                        'Congratulations!'
                        '\nYou\'ve found a secret button!\n'
                        '\nThanks for playing!\n'
                        '\nIt was fun to try Tkinter library for the first time'
                        '\nBest regards, ilia.')


def rendered_item_destroy(in_list):
    """ Destroys gfx objects """
    for item in in_list:
        item.destroy()


def app_destroy():
    """ Kills main app window """
    root.destroy()


def render_game_bg():
    """ Game window """
    game_bg = Label(root, image=i_bg)
    game_bg.place(x=0, y=0, relwidth=1, relheight=1)


def render_game_btn_pvp(in_state):
    """ Show PVP button """
    game_btn_pvp = Button(root, image=i_btn_pvp, bg='#d1a67e', activebackground='#654053',
                          command=game_btn_pvp_func, state=in_state)
    game_btn_pvp.place(x=(app_w / 100 * 3), y=(app_h / 100 * 94.5))


def game_btn_pvp_func():
    """ PVP button command """
    global game_mode, x_list, o_list
    destroy_game_tile([i for i in range(9)])
    x_list.clear()
    o_list.clear()
    change_turn('pvp')
    return game_mode


def render_game_btn_vsai(in_state):
    """ Show VSAI button"""
    game_btn_vsai = Button(root, image=i_btn_vsai, bg='#d1a67e', activebackground='#654053',
                           command=game_btn_vsai_func, state=in_state)
    game_btn_vsai.place(x=(app_w / 100 * 76), y=(app_h / 100 * 94.5))


def game_btn_vsai_func():
    """ VSAI button command """
    global game_mode, x_list, o_list
    destroy_game_tile([i for i in range(9)])
    x_list.clear()
    o_list.clear()
    change_turn('ai')
    return game_mode


def render_game_btn_restart(in_state):
    """ Show RESTART button """
    game_btn_restart = Button(root, image=i_btn_restart, bg='#d1a67e', activebackground='#654053',
                              command=game_btn_restart_func, state=in_state)
    game_btn_restart.place(x=(app_w / 2 - restart_btn_w / 2), y=(app_h / 100 * 92))


def game_btn_restart_func():
    """ Restart button command """
    global whose_turn, x_list, o_list
    destroy_game_tile([i for i in range(9)])
    x_list.clear()
    o_list.clear()
    whose_turn = 'x'
    show_info()


def render_game_tile(in_tiles_list, in_image):
    """ Show tiles by given list """
    global rendered_tiles
    tile_grid = {
        0: [5, 36], 1: [24, 36], 2: [43, 36],
        3: [5, 55], 4: [24, 55], 5: [43, 55],
        6: [5, 74], 7: [24, 74], 8: [43, 74],
    }
    x, y = 0, 1
    for i in in_tiles_list:
        game_tile = Label(root, image=in_image, borderwidth=0)
        game_tile.place(x=tile_grid[i][x] * app_size, y=tile_grid[i][y] * app_size)
        rendered_tiles[i] = game_tile
    return rendered_tiles


def destroy_game_tile(in_tiles_list):
    """ Destroy tiles by given list  """
    global rendered_tiles
    for i in in_tiles_list:
        if i in rendered_tiles:
            rendered_tiles[i].destroy()
            del rendered_tiles[i]
    return rendered_tiles


def change_turn(in_mode='current'):
    """ Change game mode and turns
        Call AI move           """
    global game_mode, whose_turn
    if in_mode == 'current' and game_mode == 'ai':
        if whose_turn == 'x':
            check_win('x')
            get_ai_move()
            show_info()
        elif whose_turn == 'o':
            whose_turn = 'x'
            show_info()
    elif in_mode == 'current' and game_mode == 'pvp':
        whose_turn = 'o' if whose_turn == 'x' else 'x'
    elif in_mode == 'pvp':
        if game_mode == 'ai':
            game_mode = 'pvp'
        whose_turn = 'x'
        show_info()
    elif in_mode == 'ai':
        if game_mode == 'pvp':
            game_mode = 'ai'
        whose_turn = 'x'
        show_info()
    return game_mode, whose_turn


def show_info():
    """ Show info messages """
    global game_mode, whose_turn, info_messages
    for message in info_messages:
        message.destroy()
    message = Label(root, image=i_info_pvp if game_mode == 'pvp' else i_info_vsai, borderwidth=0)
    message.place(x=(app_w / 2 - mode_info_w / 2), y=4 * app_size)
    message = Label(root, image=i_info_turn_x if whose_turn == 'x' else i_info_turn_o, borderwidth=0)
    message.place(x=(app_w / 2 - turn_info_w / 2), y=23 * app_size)
    return info_messages


def check_win(player):
    """ Check if win conditions are met or no free moves left """
    global x_list, o_list
    free_tiles = 9 - len(get_occupied_tiles(x_list, o_list))
    if player == 'x':
        if win_conditions(x_list):
            game_stop('x')
    elif player == 'o':
        if win_conditions(o_list):
            game_stop('o')
    if free_tiles == 0:
        if win_conditions(x_list):
            game_stop('x')
        elif win_conditions(o_list):
            game_stop('o')
        game_stop('no_moves')


def game_stop(player):
    """ Stop mouse binder and show winner """
    global play_paused
    render_game_btn_pvp('disabled')
    render_game_btn_vsai('disabled')
    render_game_btn_restart('disabled')
    if player == 'x':
        game_btn_pvp = Button(root, image=i_win_x, bg='#d1a67e', activebackground='#654053',
                              command=game_stop_btn_func)
        game_btn_pvp.place(x=(app_w / 2 - win_info_w / 2), y=(app_h / 100 * 40))
    elif player == 'o':
        game_btn_pvp = Button(root, image=i_win_o, bg='#d1a67e', activebackground='#654053',
                              command=game_stop_btn_func)
        game_btn_pvp.place(x=(app_w / 2 - win_info_w / 2), y=(app_h / 100 * 40))
    elif player == 'no_moves':
        game_btn_pvp = Button(root, image=i_win_no_moves, bg='#d1a67e', activebackground='#654053',
                              command=game_stop_btn_func)
        game_btn_pvp.place(x=(app_w / 2 - win_info_w / 2), y=(app_h / 100 * 40))
    play_paused = 'on'


def game_stop_btn_func():
    """ Game stop info - button command """
    global x_list, o_list, whose_turn
    x_list.clear()
    o_list.clear()
    whose_turn = 'x'
    game_is_running()


def on_mouse_click(event):
    """ Global event command """
    global x_list, o_list, game_mode, play_paused
    if play_paused != 'on':
        tile_num = get_tile_num_by_coords(event.x, event.y)
        if tile_num in range(0, 9):
            if whose_turn == 'x':
                render_game_tile([tile_num], i_x)
                x_list.append(tile_num)
                if len(x_list) >= 3:
                    check_win('x')
                change_turn()
            elif whose_turn == 'o' and game_mode == 'pvp':
                render_game_tile([tile_num], i_o)
                o_list.append(tile_num)
                if len(o_list) >= 3:
                    check_win('o')
                change_turn()
    show_info()


def get_ai_move():
    global x_list, o_list, play_paused
    occupied_tiles = get_occupied_tiles(x_list, o_list)
    smart_moves = get_smart_moves(x_list, o_list, occupied_tiles)
    priority_moves = get_priority_moves(x_list, o_list, smart_moves, occupied_tiles)
    tile = ai_next_move(priority_moves)
    if tile is not None and play_paused != 'on':
        o_list.append(tile)
        render_game_tile([tile], i_o)
    check_win('o')


def game_is_running():
    """ Main function called from Play button """
    global rendered_tiles, game_mode, play_paused
    rendered_item_destroy(render_menu_var_list)
    render_game_bg()
    render_game_btn_pvp('active')
    render_game_btn_vsai('active')
    render_game_btn_restart('active')
    show_info()
    root.bind('<Button-1>', on_mouse_click)
    play_paused = 'off'


# Global vars on start
game_mode = 'pvp'  # -> 1: hotseat ('pvp')  -> 2: vs ai ('ai')
whose_turn = 'x'
play_paused = 'off'
id_click = None
x_list = list()
o_list = list()
rendered_tiles = dict()
info_messages = list()

# Game start
render_menu_var_list = render_menu()

# Main infinity loop
root.mainloop()
