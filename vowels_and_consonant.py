word = input("Enter a word: ")


def print_vowels_and_consonant(letter):
    vow = 0
    con = 0
    for i in range(len(letter)):
        if letter[i] in ['a', 'e', 'o', 'i', 'u']:
            vow += 1
        else:
            con += 1

    print("Count of vowel is: ", vow)
    print("Count of consonant is: ", con)


print_vowels_and_consonant(word)
