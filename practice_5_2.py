def words_ending_with_ya(sentence):
    #Разделение предложения на слова
    words = sentence.split()
    #Создание списка слов, заканчивающихся на "я":
    #word for word in words - генератор списка
    result = [word for word in words if word.endswith('я')]
    return result

# Пример использования
sentence = "Это простая строка, которая содержит слова, заканчивающиеся на букву я."
words = words_ending_with_ya(sentence)
print(words)
