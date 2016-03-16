
# Fun but slow way of tackeling the problem.
def is_word_ordered(word, rev=False):
    return all(x[0] == x[1] for x in zip(word if not rev else reversed(word), sorted(word)))

if __name__ == "__main__":
    words = ["almost", "cereal", "billowy", "biopsy", "chinos", "defaced", "chintz", "sponged", "bijoux", "abhors", "fiddle", "begins", "chimps", "wronged"]
    for word in words:
        if is_word_ordered(word):
            print(word, "IS ORDERED")
        elif is_word_ordered(word, True):
            print(word, "IS REVERSED")
        else:
            print(word, "UNORDERED")

