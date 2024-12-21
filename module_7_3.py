class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()  # Приводим текст к нижнему регистру
                    # Убираем знаки препинания вручную
                    for char in  [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        content = content.replace(char, "")
                    words = content.split()  # Разбиваем текст на слова
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                position = words.index(word) + 1  # Индекс + 1 для позиции с 1
                result[file_name] = position
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            count = words.count(word)
            if count > 0:
                result[file_name] = count
        return result

# Создаем файл test_file.txt
with open('test_file.txt', 'w', encoding='utf-8') as f:
    f.write("It's a text for task. Найти везде, используйте его для самопроверки. Успехов в решении задачи! text text text.")

# Пример использования
finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего