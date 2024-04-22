def camel_case(str):
    res_list = []
    
    str = str.split(" ")
    
    for word in str:
        res_list.append(word.capitalize())
        
    return "".join(res_list)