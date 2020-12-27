import matrix
import random

H = [[0, 0, 0, 1, 1, 1, 1],
     [0, 1, 1, 0, 0, 1, 1],
     [1, 0, 1, 0, 1, 0, 1]]

G = [[1, 0, 1, 1],
     [1, 1, 0, 1],
     [0, 0, 0, 1],
     [1, 1, 1, 0],
     [0, 0, 1, 0],
     [0, 1, 0, 0], 
     [1, 0, 0, 0]]

# по блоку возращает кодовое слово 
def get_code_word(p):
	return matrix.multiply(G, p)

# по кодовому слову возращает столбец контрольных сумм
def get_error_syndrom(code_word):
	return matrix.multiply(H, code_word)

# по столбцу контрольных сумм возращает номер неправильного бита в кодовом слове
def find_error(error_syndrom):
	return error_syndrom[0][0] * 4 + error_syndrom[1][0] * 2 + error_syndrom[2][0]

# случайным образом ломает один бит в бинарной строке
def break_one_bit(s):
	num = random.randint(0, len(s) - 1)
	return s[0:num] + str(1 - int(s[num])) + s[num + 1:]

# переводит обычную строку в бинарную(каждому символу соответсвует 8 бит - двоичный номер в таблице ASCII) 
def get_binary_sequence(s):
	sequence = ""
	for elem in s:
		number = ord(elem)
		binary_view_of_number = ""
		for i in range(8):
			binary_view_of_number += str(number % 2);
			number //= 2
		sequence += binary_view_of_number[::-1]
	return sequence