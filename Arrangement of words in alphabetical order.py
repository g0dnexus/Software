def sort_text_alphabetically(text):
    words = text.split(' ')
    sorted_words = sorted(words)
    sorted_text = ' '.join(sorted_words)
    
    return sorted_text


input_text = input("Enter text to be sorted / Введите текст для сортировки: ")
sorted_text = sort_text_alphabetically(input_text)


print("Sorted text / Отсортированный текст:")
print(sorted_text)
