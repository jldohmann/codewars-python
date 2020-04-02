def duplicate_encode(word):
    """
    Takes a string and counts the number of times a character appears.
    If a character appears only once, it is replaced with "(".
    If a character appears more than once, it is replaced with ")".
    """
    new_word = word.casefold()
    lst = []
    new_lst = []
    
    for char in new_word:
       counts = new_word.count(char)
       lst.append(counts)
    
    for int in lst:
       if int > 1:
          new_lst.append(")")
       else:
          new_lst.append("(")
          
    final = ''.join(new_lst)
    return final
