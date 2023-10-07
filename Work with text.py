def remove_punctuation(text):
    result = ""
    for c in text:
        if c.isalnum():
            result += c
    return result


def remove_extra_spaces(text):
    result = ""
    is_space = False
    for c in text:
        if not c.isspace():
            result += c
            is_space = False
        else:
            if not is_space:
                result += ' '
                is_space = True
    return result.strip()


def to_upper(text):
    return text.upper()


def to_lower(text):
    return text.lower()


def count_words(text):
    count = 0
    in_word = False
    for c in text:
        if c.isalpha():
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False
    return count


def count_sentences(text):
    count = 0
    for c in text:
        if c in ('.', '!', '?'):
            count += 1
    return count


def invert_text(text):
    return text[::-1]


def invert_words(text):
    words = text.split()
    inverted_words = [word[::-1] for word in words]
    return ' '.join(inverted_words)


def remove_numbers(text):
    result = ""
    for c in text:
        if not c.isdigit():
            result += c
    return result


def replace_numbers(text):
    numbers = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    result = ""
    for c in text:
        if c.isdigit():
            index = int(c)
            if 0 <= index <= 9:
                result += numbers[index]
        else:
            result += c
    return result


def count_characters(text):
    return len(text)


text = input("Введите текст: ")

print("Количество символов:", count_characters(text))
print("Количество предложений:", count_sentences(text))
print("Количество слов:", count_words(text))
print("Текст без чисел:", remove_numbers(text))
print("Текст без символов пунктуации:", remove_punctuation(text))
print("Текст без лишних пробелов:", remove_extra_spaces(text))
print("Текст в нижнем регистре:", to_lower(text))
print("Текст в верхнем регистре:", to_upper(text))
print("Инвертированный текст:", invert_text(text))
print("Текст с инвертированными словами:", invert_words(text))
print("Текст с числами замененными на слова:", replace_numbers(text))
