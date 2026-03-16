def can_form(word, small):
    for ch in small:
        if small.count(ch) > word.count(ch):
            return False
    return True


word = input("Enter a word: ")

words = ["cat","dog","bag","at","go","do","tab"]

print("Smaller words that can be formed:")

for w in words:
    if can_form(word, w):
        print(w)
