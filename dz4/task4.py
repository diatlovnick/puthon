# 4- В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны

with open(file='Text.txt', encoding='utf-8', mode = 'w') as file:
     file.write("Мама сшила м0не штаны и7з бере9зовой кор45ы 893.")

file = open('Text.txt' , "r", encoding='utf-8')

def split_file_lst(file) -> list:    
    data = file.readlines()
    lst = data.split()
    file.close()
    return lst
def delete_word_whith_number(lst: list) -> list:
    new_list = []
    for i in lst:
        is_number = False
        for n in i:
            if n.isdigit():
                is_number = True
                break
        if is_number ==False:
            new_list.append(i)
    return new_list
lst_word_with_number = split_file_lst(file)
res_lst = delete_word_whith_number(lst_word_with_number)
print(res_lst)



# не разобрался как перевести правильно файл в список