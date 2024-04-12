def reverse_words(text):
    words_list = text.split(" ")
    reversed_words = []
    
    for word in words_list:
        reversed_words.append(word[::-1])
    
    
    return " ".join(reversed_words)