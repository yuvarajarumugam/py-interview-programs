s1 = 'abc'
s2 = 'cab'

def anagram(s1: str, s2: str):
    return sorted(s1) == sorted(s2)

print(anagram(s1, s2))