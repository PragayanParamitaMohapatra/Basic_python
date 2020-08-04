def remove_vowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in word:
        if letter in vowels:
            word=word.replace(letter,'')
    return word
w=['car', 'house', 'plant', 'fisherman', 'picnic', 'rodeo']
new_words = [remove_vowel(word) for word in w]
print(new_words)