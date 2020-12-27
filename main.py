import hamming
import addition

# считанную строку перводим в двоичный вид и представляем в виде набора блоков
s = input()
binary_view_of_s = hamming.get_binary_sequence(s)
blocks = addition.binary_string_to_blocks(binary_view_of_s)

# кодируем каждый блок, складываем все кодовые слова в одну бинарную строку и ломаем в ней один бит
encoded_string = ""
for block in blocks:
    encoded_string += addition.code_word_to_binary_string(hamming.get_code_word(block))
encoded_string = hamming.break_one_bit(encoded_string)

# бьём бинарную строку на кодовые слова, вычисляем и исправляем ошибку и восстанавливаем набор блоков
correct_blocks = []
for i in range(0, len(encoded_string), 7):
    code_word = addition.binary_string_to_code_word(encoded_string[i:i + 7])
    error_syndrom = hamming.get_error_syndrom(code_word)
    number_of_incorrect_bit = hamming.find_error(error_syndrom)
    code_word = addition.correct_the_error(code_word, number_of_incorrect_bit)
    correct_block = addition.code_word_to_block(code_word)
    correct_blocks.append(correct_block)

# по набору корректных блоков восстанавливаем строку и выводим её на экран
recovering_s = addition.string_recovery(correct_blocks)
print(recovering_s)



