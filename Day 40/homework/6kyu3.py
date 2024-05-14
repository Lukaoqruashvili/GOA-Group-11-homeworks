def name_in_str(text, name):
    for i in text.lower():
        if i == name[0].lower():
            name = name[1:]
            if not name:
                return True
    return False