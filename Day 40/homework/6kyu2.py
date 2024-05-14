def is_pangram(st):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in st.lower():
            return False
    return True