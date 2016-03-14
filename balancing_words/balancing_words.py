import string

def get_side_weight(side, indexes):
    alphabet = string.ascii_lowercase
    return sum((alphabet.index(side[x]) + 1) * (indexes[x] + 1) for x in range(len(side)))

def get_weights(word, pivot):

    left = word[:pivot]
    right = word[pivot+1:]

    return get_side_weight(left, list(reversed(range(len(left))))), get_side_weight(right, list(range(len(right))))

def get_pivot(word):
    for pivot in range(len(word)):
        weights = get_weights(word, pivot)
        if weights[0] != weights[1]:
            continue
        return pivot
    return -1

if __name__ == "__main__":
    words = ["stead", "CONSUBSTANTIATION", "wrongheaded", "unintelligibility"]
    for word in words:
        pivot = get_pivot(word.lower())
        if pivot == -1:
            print(word, "has no pivot")
        else:
            print(word[:pivot], word[pivot], word[pivot:], "-", pivot)
