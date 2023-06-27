# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
import string

text = "Переме́нный ток - электрический ток," \
       " который с течением времени изменяется по величине, обычно и по направлению в электрической цепи." \
       " Хотя переменный ток часто переводят на английский как alternating current, эти термины не эквивалентны." \
       "Переменный ток (англ. Аlternating Сurrent) - электрический ток," \
       " который с течением времени изменяется по величине и направлению (или только по величине или направлению)." \
       " Основные характеристики переменного тока это: форма сигнала," \
       " амплитудные и временные характеристики силы тока и напряжения." \
       "Магнитное поле всегда возникает вокруг движущихся электрических зарядов," \
       " или при взаимодействии тел, обладающих магнитным моментом." \
       " Поскольку современные электрические сети используют в основном переменный электрический ток," \
       " то магнитное поле изменяет своё значение и направление периодически."

result = {}
text = text.translate(str.maketrans('', '', string.punctuation)).split()

for i in text:
    if i.lower() in result.keys():
        result[i.lower()] += 1
    else:
        result[i.lower()] = 1

result = sorted(result.items(), key=lambda item: item[1], reverse=True)
print(result[:10])