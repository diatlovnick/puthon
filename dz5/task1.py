#1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
#'абвгдейка - это передача' = >" - это передача"

text_str = str("абвгдейка - это передача")
text_lst = text_str.split()
res_lst = []
#word_delete = str('абв')
def delete_word(text_lst: list, word_delete: str):
    for i in range(len(text_lst)):
        test_word = text_lst[i].count(word_delete)
        if test_word == 0:
            res_lst.append(text_lst[i])

    return res_lst
res = delete_word(text_lst,'абв')
print(res)
    

