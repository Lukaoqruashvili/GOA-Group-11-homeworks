def reverse_words(text):
    splitword = text.split(' ')
    
    reverse = [word[::-1] for word in splitword]
    
    result= ' '.join(reverse)
    
    return result