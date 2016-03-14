from string import ascii_lowercase

def only_contains(letters):
    return lambda x: all(c in letters for c in x.strip())

def get_wordset(characters):
    has_letters = only_contains(characters)

    with open("/usr/share/dict/words") as f:
        return [word.strip() for word in f if has_letters(word)]

if __name__ == "__main__":
    working = ["abcd", "qwer", "hjklo", "edcf", "bnik", "poil", "vybu"]
    for keys in working:
        words = get_wordset(keys)
        print(keys, max(words, key=len))
