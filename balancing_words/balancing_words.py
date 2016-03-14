from string import ascii_lowercase

def weight(text):

    weight = 0

    text = text.strip()

    if not text:
        return weight


    for x in range(len(text)):
        weight += (ascii_lowercase.index(text.lower()[x]) + 1) * (x + 1)

    return weight

def get_sides(pivot, text):
    return text[:pivot], text[pivot+1:]

def get_pivot_point(text):
    for x in range(len(text)):
        sides = get_sides(x, text)
        if weight(sides[0]) == weight(sides[1]):
            return x
    return -1

def show_info(text):
    pivot = get_pivot_point(text)
    if pivot == -1:
        print(text, "is not balanced")
    else:
        sides = get_sides(pivot, text)

        print(sides[0], text[pivot], sides[1], "-", weight(sides[1]))


if __name__ == "__main__":
    text = "stead"
    show_info(text)
#    with open("/usr/share/dict/words") as f:
#        for word in f:
#            show_info(word)
