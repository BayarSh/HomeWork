def single_root_words(root_word, *other_words): # Объявляем функцию single_root_words и напишем в ней параметры root_word и *other_words
    same_words = [] # Создаём внутри функции пустой список same_words, который пополнится нужными словами.

    # Приводим root_word к нижнему регистру для сравнения
    root_word_lower = root_word.lower()

    for word in other_words:    # При помощи цикла for перебираем предполагаемо подходящие слова
        # Приводим текущее слово к нижнему регистру для сравнения
        word_lower = word.lower()

        # Проверяем, содержится ли одно слово в другом
        if (root_word_lower in word_lower) or (word_lower in root_word_lower):
            same_words.append(word)

    return same_words

# Примеры вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)  # ['richiest', 'orichalcum', 'richies']
print(result2)  # ['Able', 'Disable']