def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        is_valid = True
        
        numbers = "0123456789"
        
        for i in pin:
            if i not in numbers:
                is_valid = False
                
        return is_valid
    return False