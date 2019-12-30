a = ['a', 'ā', 'á', 'ǎ', 'à']; e = ['e', 'ē', 'é', 'ě', 'è']
i = ['i', 'ī', 'í', 'ǐ', 'ì']; o = ['o', 'ō', 'ó', 'ǒ', 'ò']
u = ['u', 'ū', 'ú', 'ǔ', 'ù']; v = ['ü', 'ǖ', 'ǘ', 'ǚ', 'ǜ']
vowel = ['a', 'e', 'i', 'o', 'u', 'v']

def change(word):
    new_word = list(word)
    delete_index = []
    for z, letter in enumerate(new_word):
        try:
            intonation = int(letter)
        except:
            continue
        else:
            delete_index.append(z)
            tmp_letter = eval(new_word[z-1])
            new_word[z-1] = tmp_letter[intonation]

    count = 0
    for k in delete_index:
        del new_word[k-count]
        count += 1

    new_word = "".join(new_word)
    return new_word

while True:
    change_word = input("Input Hànyǔ Pīnyīn(Quit: Q): ")

    if change_word.upper() == "Q":
        break
    
    change_word = change(change_word)
    print(change_word)

