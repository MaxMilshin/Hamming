# функция, исправляющая ошибку по кодовому слову и номеру неправильного бита 
def correct_the_error(code_word, number_of_incorrect_bit):
    if (number_of_incorrect_bit != 0):
        code_word[number_of_incorrect_bit - 1][0] = 1 - code_word[number_of_incorrect_bit - 1][0]
    return code_word 

# переводит строку длины 4 в один блок
def build_one_block(s):
    return [[int(s[0])], [int(s[1])], [int(s[2])], [int(s[3])]]

# представляет бинарную строку и виде набора блоков
def binary_string_to_blocks(s):
    blocks = []
    for i in range(0, len(s), 4):
        blocks.append(build_one_block(s[i:i + 4]))
    return blocks

# по корректному кодовому слову возращает блок
def code_word_to_block(code_word):
    return [code_word[6], code_word[5], code_word[4], code_word[2]]

# переводит набор блоков в одну бинарную строку
def blocks_to_binary_string(blocks):
    binary_s = ""
    for block in blocks:
        for [number] in block:
            binary_s += str(number)
    return binary_s

# по набору блоков востанавливает исходную строку
def string_recovery(blocks):
    recovering_s = ""
    for j in range(0, len(blocks), 2):
        number_of_character = 0
        for i in range(8):
            number_of_character += blocks[j + 1 - i // 4][4 - i % 4 - 1][0] * (2 ** i)
        recovering_s += chr(number_of_character)
    return recovering_s

# переводит кодовое слово в бинарну строку
def code_word_to_binary_string(code_word):
    ans = ""
    for i in range(7):
        ans += str(code_word[i][0])
    return ans

# переводит бинарную строку в кодовое слово
def binary_string_to_code_word(s):
    code_word = []
    for i in range(len(s)):
        code_word.append([int(s[i])])
    return code_word