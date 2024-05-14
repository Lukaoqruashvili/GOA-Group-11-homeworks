def tocamel_case(text):
    if text == "":
        return ""
    text = text.replace("-", "")
    words = text.split("_")
    final_str = ""
    if text[0].isupper():
        for i in words:
            final_str += i.capitalize()
    else:
        final_str = words[0]
        for index in range(1,len(words)):
            final_str += words[index].capitalize()




    return final_str