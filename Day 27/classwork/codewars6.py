def is_palindrome(s):
    reversedword = s[::1]
    if s == reversedword:
        return True
    else:
        return False
