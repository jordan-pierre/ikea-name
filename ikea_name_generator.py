import random

def gen_ikea_name(original_name):
    name = original_name[::-1].lower()
    vowels = {'a': ['å', 'ä'], 'e': ['ë'], 'i': ['ï'], 'o': ['ö', 'ø'], 'u': ['ü']}
    first_vowel, index = first_str_occurance(name, vowels.keys())

    if first_vowel is not None:
        name = name[:index] + random.choice(vowels[first_vowel]) + name[index + 1:]
    
    return name.capitalize()


def first_str_occurance(string, chars):
    for index, char in enumerate(string):
        if char in chars:
            return char, index
    else:
        return (None, 0)


for i in range(10):
    print(gen_ikea_name('u'))
