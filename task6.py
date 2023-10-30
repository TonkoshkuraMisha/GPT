def first_repeated_word(repeated_words):
    '''Находит первый дубль в строке'''
    repeated_words = repeated_words.split(" ")
    added_words = []
    for word in repeated_words:
        if repeated_words.count(word) >= 2:
            added_words.append(word)
    if len(added_words) > 0:
        return added_words[0]
    else:
        return None


print(first_repeated_word("ab ca bc ca ab bc"))
