import collections


def find_most_common_word(file_path):
    word_counts = collections.Counter()

    with open(file_path, "r") as file:
        content = file.read()
        content = content.replace(",", "").replace(".", "")  # Удаление разделителей
        words = content.lower().split()

        word_counts.update(words)

    most_common_word, word_count = word_counts.most_common(1)[0]

    return most_common_word, word_count


# Пример использования
file_path = "file.txt"
word, word_count = find_most_common_word(file_path)
print("word =", word)
print("word_count =", word_count)
