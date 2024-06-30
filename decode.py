def decryption(cin):
    listt = []
    i = 0
    while i < len(cin):
        # Take every 4th character (actual encoded character)
        listt.append(ord(cin[i]) - 12)
        i += 4  # Skip the random word (3 characters) + 1 actual character
    
    decoder = ""
    for val in listt:
        decoder += chr(val)
    
    return str(decoder)
