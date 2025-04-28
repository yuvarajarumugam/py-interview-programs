def vowels_consonants(string: str):
    vowels = ['a', 'e', 'i', 'o', 'u']

    vowels_count = 0
    consonants_count = 0

    for i in string:
        if i in vowels:
            vowels_count += 1
        else:
            consonants_count += 1

    return f"Vowels count is {vowels_count} and Consonants count is {consonants_count}"

print(vowels_consonants("aeiou"))