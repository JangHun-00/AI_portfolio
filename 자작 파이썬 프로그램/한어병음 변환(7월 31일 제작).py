a = ['a', 'ā', 'á', 'ǎ', 'à']
e = ['e', 'ē', 'é', 'ě', 'è']
i = ['i', 'ī', 'í', 'ǐ', 'ì']
o = ['o', 'ō', 'ó', 'ǒ', 'ò']
u = ['u', 'ū', 'ú', 'ǔ', 'ù']
v = ['ü', 'ǖ', 'ǘ', 'ǚ', 'ǜ']

vowel = ['a', 'e', 'i', 'o', 'u', 'v']

def change(word):
    new_word = word
    
    for i, letter in enumerate(word):
        if letter in vowel:
            gap = len(word) - len(new_word)
            try:
                intonation = int(word[i+1])
            except:
                if letter == 'v':
                    try:
                        new_word = new_word[:i-gap] + 'ü' + new_word[i-gap+1:]
                    except IndexError:
                        new_word = new_word[:i-gap] + 'ü'
                continue

            if intonation > 4:
                print("The letter '{}' has a wrong intonation: {}".format(letter, intonation))
                return 'Error'
            
            lis = eval(letter)
            new_vowel = lis[intonation]

            try:
                new_word = new_word[:i-gap] + new_vowel + new_word[i-gap+2:]
            except IndexError:
                new_word = new_word[:i-gap] + new_vowel
    return new_word

while True:
    change_word = input("Input Hànyǔ Pīnyīn(Quit: Q): ")

    if change_word.upper() == "Q":
        break
    
    change_word = change(change_word)
    print(change_word)
