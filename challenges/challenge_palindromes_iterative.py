def is_palindrome_iterative(word):
    comparision_word = word[::-1]
    if len(word) == 1:
        return True
    if word is None or word == "":
        return False
    if word == comparision_word:
        return True
    else:
        return False
