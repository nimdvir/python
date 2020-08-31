import re

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if (word[0] in vowels):
        count += 1
    for index in range(1, len(word)):
        if ((word[index] in vowels) and (word[index - 1] not in vowels)):
            count += 1
            if (word.endswith("e")):
                count -= 1
    if (count == 0):
        count += 1
    return count

def count_syllables(word):
    return len(
        re.findall('(?!e$)[aeiouy]+', word, re.I) +
        re.findall('^[^aeiouy]*e$', word, re.I)
    )

word = input("Please enter a word: ")
print("There are " + str(syllable_count(word)) + " syllables in '" + word + "'")
print("Second option! There are " + str(count_syllables(word)) + " syllables in '" + word + "'")



