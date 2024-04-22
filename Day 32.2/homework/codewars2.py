def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    if (len(s) == 0 or len(output) > 140):
        return False
    else:
        return output