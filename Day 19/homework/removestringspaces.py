def no_space(x):
    result = ""
    
    for char in x:
        if char != " ":
            result = result + char
    
    return result

print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))