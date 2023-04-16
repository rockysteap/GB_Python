# print(x := 1)

data = {'main': [
                {'col': 1, 'label': ['(M)ain menu', '(Г)лавное меню']},
                {'row': 1, 'item_1': ['(F)ile', '(Ф)айл']},
                {'row': 2, 'item_2': ['(B)ook', '(К)нига']},
                {'row': 3, 'item_3': ['E(x)it', '(В)ыход']},
                {'row': 4, 'item_4': ['Change to:', 'Сменить на:']},
                {'row': 5, 'item_5': ['(R)u', '(А)нгл']},
        ],
        'file': [
                {'col': 2, 'label': ['File menu', 'Работа с файлами']},
                {'row': 1,  'item_1': ['(O)pen - read from file', '(О)ткрыть - считать из файла']},
                {'row': 2,  'item_2': ['(S)ave - write to file', '(С)охранить - записать в файл']},
        ],
        'book': [
                {'col': 2, 'label': ['Book menu', 'Работа с книгой']},
                {'row': 1,  'item_1': ['(N)ew - make new entry', '(С)оздать - новая запись']},
                {'row': 2,  'item_2': ['F(I)nd - search for entry', '(Н)айти - поиск записи']},
                {'row': 3,  'item_3': ['(S)how - show book content', '(П)оказать - вывести всё']},
                {'row': 4,  'item_4': ['(E)dit - change existing entry', '(И)зменить - откорректировать запись']},
                {'row': 5,  'item_5': ['(D)elete - remove existing entry', '(У)далить - стереть запись']},
        ]}


# print(menu['main'])
# print(menu['main'][0])
# print(menu['main'][0]['label'])
# print(menu['main'][0]['label'][0])
# print(list(menu))

# for key in data:
#     print(key)

lang_count = 0
gr_by_row = dict()
i_max_len = dict()
for key, value in data.items():
    # print(key)
    # print(data[key][0]['col'])
    # print(len(data[key][0]['label']))
    # print(len(data[key]))
    # print(data[key][2])
    # print(gr_by_row[data[key][0]['col']])

    if len(data[key][0]['label']) > lang_count:
        lang_count = len(data[key][0]['label'])

    # { 1: ['main'], 2: ['file', 'book'] }
    gr_by_row[data[key][0]['col']] = gr_by_row.get(data[key][0]['col'])
    if not gr_by_row[data[key][0]['col']]:
        gr_by_row[data[key][0]['col']] = []
    gr_by_row[data[key][0]['col']].append(key)

    for i in range(lang_count):
        i_max_len[data[key][0]['col']] = i_max_len.get(data[key][0]['col'])
        if not i_max_len[data[key][0]['col']]:
            i_max_len[data[key][0]['col']] = []

    # for item in value:
    #     for member in item.values():
    #         if isinstance(member, list) and len(member[0]) > max:



        # i_max_len[data[key][0]['col']].append(key)

        # for i in range

    # for value in data[key][0]:
    #     print(data[key])

# print(i_max_len)

d = {'a': 1, 'b': 2}
temp_val = d['a']

print(temp_val)
