def find_vowels(input_string):
    vowels = "aeiouAEIOU"
    found_vowels = ""

    for char in input_string:
        if char in vowels:
            found_vowels += char

    return found_vowels


string = input("Enter a string: ")
vowels = find_vowels(string)

if vowels:
    print("Vowels in", string, "are", vowels)
else:
    print("No vowels found in", string)

