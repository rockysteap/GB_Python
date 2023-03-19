def is_ru_alphabet(word):
    ru_alphabet = {'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
                   'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'}
    for letter in word.lower():
        if letter not in ru_alphabet:
            return False
    return True


def ru_score(word):
    ru_dict = {('А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'): 1,
               ('Д', 'К', 'Л', 'М', 'П', 'У'): 2,
               ('Б', 'Г', 'Ё', 'Ь', 'Я'): 3,
               ('Й', 'Ы'): 4,
               ('Ж', 'З', 'Х', 'Ц', 'Ч'): 5,
               ('Ш', 'Э', 'Ю'): 8,
               ('Ф', 'Щ', 'Ъ'): 10}
    score = 0
    for key, value in ru_dict.items():
        for letter in word.upper():
            if letter in key:
                score += value
    return score


def is_en_alphabet(word):
    en_alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    for letter in word.lower():
        if letter not in en_alphabet:
            return False
    return True


def en_score(word):
    en_dict = {('A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'): 1,
               ('D', 'G'): 2,
               ('B', 'C', 'M', 'P'): 3,
               ('F', 'H', 'V', 'W', 'Y'): 4,
               ('K', ): 5,
               ('J', 'X'): 8,
               ('Q', 'Z'): 10}
    score = 0
    for key, value in en_dict.items():
        for letter in word.upper():
            if letter in key:
                score += value
    return score
