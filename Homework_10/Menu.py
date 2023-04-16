
class Menu:
    pointer = ' -> '
    file_last_saved: str = '-'
    file_last_opened: str = '-'
    state = None
    lang: int = 0  # current language

    def __init__(self, menu_data_module_and_dict, menu_link_module_and_dict, file_info):
        """ Expected source structure """
        # dataset: dict = { 'GroupName1': [ {'col': 1, 'label': [label_in_lang1, label_in_lang2]   },
        #                                   {'row': 1, ItemName1: [label_in_lang1, label_in_lang2] },
        #                                   {'row': 2, ItemName2: [label_in_lang1, label_in_lang2] },
        #                                   ]
        #                   'GroupName2': [ {}, ... ]
        #                   }
        # self.data[key] <- GroupName
        # self.data[key][index] <- number of dict to access
        # self.data[key][index][key] <- inner dict value or list of values
        # self.data[key][index][key][index] <- inner dict value inside list of values
        self.data: dict = menu_data_module_and_dict
        self.links: dict = menu_link_module_and_dict
        self.info: dict = file_info
        self.menu_dict: dict = dict()  # dict with 2d list with items
        self.gr_by_col: dict = dict()  # how many groups via switching share one column
        self.lang_count: int = 0  # number of languages source file provided
        self.title_max_len: dict = dict()  # longest label in each column

        # Prepare menu_dict for easier item access and get shared columns -> dict:
        #                                           {0: ['GroupName1'], 1: ['GroupName1', 'GroupName2']}
        for key, value in self.data.items():
            self.menu_dict[key] = []
            for item in value:
                for key2, value2 in item.items():
                    if isinstance(value2, list):
                        self.menu_dict[key].append(value2)
                        if self.lang_count == 0:
                            self.lang_count = len(value2)  # detect number of languages from first menu titles
                    elif key2 == 'col':
                        self.gr_by_col[key] = value2 - 1  # -1 to get col indices

        # Get the longest title in group by language, e.g. for 2 lang -> {'GroupName1': [11, 14], ...}
        for i in range(self.lang_count):
            for key, value in self.menu_dict.items():
                temp_max_len = 0
                if key not in self.title_max_len:
                    self.title_max_len[key] = [i for i in range(self.lang_count)]
                for item in value:
                    if len(item[i]) > temp_max_len:
                        temp_max_len = len(item[i])
                self.title_max_len[key][i] = temp_max_len

    def set_lang(self, language: int) -> None:
        self.lang = language

    def __setstate__(self, state: str):
        self.state = state

    def __getstate__(self):
        if not self.state:  # if set was not used prior get
            self.state = list(self.data)[0]  # set to 'GroupName1' as an initial state
        return self.state

    def set_last_opened(self, file: str) -> None:
        self.file_last_opened = file

    def set_last_saved(self, file: str) -> None:
        self.file_last_saved = file

    def draw(self) -> None:
        """ Chained view (info passed from links dict):
            states      ->  (shown menus)
            columns     ->        I          II         III
            GroupName1  ->  (GroupName1)
            GroupName2  ->  (GroupName1, GroupName2)
            GroupName3  ->  (GroupName1, GroupName3)
            GroupName4  ->  (GroupName1, GroupName2, GroupName4) """
        state_level = self.gr_by_col[self.state]
        menu_path = self.links[self.state]
        item_len_list = []
        info = f'{1 + len(self.pointer) + 1}   {" " * len(menu_path)}'
        info_line_len = len(info)
        item_count_list = []
        next_col_place = dict()
        left_shift = 1
        middle_gap = 3
        for each in menu_path:
            item_len_list.append(self.title_max_len[each][self.lang])
            info_line_len += self.title_max_len[each][self.lang]
            item_count_list.append(len(self.menu_dict[each]))
        file_info = f" {self.info['last_opened'][self.lang]} {self.file_last_opened}    " \
                    f"{self.info['last_saved'][self.lang]} {self.file_last_saved}"
        if len(file_info) > info_line_len:
            info_line_len = len(file_info)
        print(file_info)
        print("-" * info_line_len)
        col_gap, col, row = 0, 0, 0
        row_step_counter = len(item_count_list)
        while set(item_count_list) != { 0 }:
            for counter, menu in enumerate(menu_path):
                if state_level == counter and row == 0:
                    print(f'{" " * col_gap}{self.pointer}', end='')
                elif state_level == counter:
                    print(' ' * len(self.pointer), end='')
                else:
                    print(' ', end='')
                col_gap = middle_gap
                if col >= len(item_len_list):
                    col = 0
                if col not in next_col_place:
                    next_col_place[col] = next_col_place.get(col,
                                                             (left_shift + col_gap + len(self.pointer) + item_len_list[
                                                                 col]))
                try:
                    my_format = "{:{align}{fill}}"
                    print(my_format.format(self.menu_dict[menu][row][self.lang], align='<', fill=12), end='')
                except IndexError:
                    print('', end='')
                col += 1
                row_step_counter -= 1
                if row_step_counter == 0:
                    print()
                    row += 1
                    row_step_counter = len(item_count_list)
                item_count_list[counter] -= 1 if item_count_list[counter] > 0 else 0
        print("-" * info_line_len)
