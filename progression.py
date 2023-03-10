# функція для знаходження суми членів арифметичної прогресії з відомим першим членом, різницею та кількістю членів.
def arith_seq_sum(first_term, diff, num_terms):
    last_term = first_term + (num_terms - 1) * diff  # знаходимо останній член
    seq_sum = (num_terms / 2) * (first_term + last_term)  # знаходимо суму прогресії
    return seq_sum


# функція, яка знаходить номер члена арифметичної прогресії з відомим цим членом, першим членом та різницею.
def arith_seq_term_num(term, first_term, diff):
    term_num = (term - first_term) / diff + 1  # знаходимо номер члена прогресії
    if term_num.is_integer():  # перевіряємо, чи є номер цілим числом
        return int(term_num)
    else:
        return None  # якщо номер не є цілим, повертаємо None


seq_sum = arith_seq_sum(13, 6, arith_seq_term_num(97, 13, 6))
print(seq_sum)
