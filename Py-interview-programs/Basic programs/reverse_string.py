string = 'yuvaraj'

print(string[::-1])

def reverse_string(string: str):
    reversed_string = ''
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    return reversed_string

print(reverse_string(string))

