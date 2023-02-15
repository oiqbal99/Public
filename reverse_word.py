def	reverse_word(word):	
    rev = ""
    w_len = len(word)
    for i in range(0, w_len):
        rev = rev + word[w_len-1-i]
        
    return rev
