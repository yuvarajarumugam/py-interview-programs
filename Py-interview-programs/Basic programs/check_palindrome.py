def palindrome(string: str):
    end = -1
    for i in range(len(string)):
        if string[i].lower() != string[end].lower():
            return False
        end += -1
    return True

print(palindrome('Madam'))