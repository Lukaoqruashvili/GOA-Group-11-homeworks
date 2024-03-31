def replace_even_indexes(word,replace_char):
    changed_word = ''
    
    for index in range(len(word)):
        if index % 2 == 0:
            changed_word = changed_word + replace_char
        else:
            changed_word = changed_word + word[index]
            
    return changed_word


print(replace_even_indexes("lukaa", "k"))