users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
texts = [
"""Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley.
    The butte is located just north of U.S.
    Highway 30N and the Union Pacific Railroad,
    which traverse the valley.""",

    """At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly.""",

    """The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers.""",
]

username = input("username: ")
password = input("password: ")

if username not in users or users[username] != password:
    print("Unregistered user. Terminating the program.")
    exit()

print(f"Welcome to the app, {username}")
print(f"We have {len(texts)} texts to be analyzed.")

selection = input(f"Enter a number btw. 1 and {len(texts)} to select: ")

if not selection.isdigit():
    print("Invalid input. Terminating the program.")
    exit()

selection = int(selection)

if selection < 1 or selection > len(texts):
    print("Invalid text number. Terminating the program.")
    exit()

text = texts[selection - 1]

words = [word.strip(".,:;!?") for word in text.split()]

word_count = len(words)
titlecase_words = sum(1 for w in words if w.istitle())
uppercase_words = sum(1 for w in words if w.isupper())
lowercase_words = sum(1 for w in words if w.islower())
numbers = [int(w) for w in words if w.isdigit()]

print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_words} titlecase words.")
print(f"There are {uppercase_words} uppercase words.")
print(f"There are {lowercase_words} lowercase words.")
print(f"There are {len(numbers)} numeric strings.")
print(f"The sum of all numbers is {sum(numbers)}.")

lengths = {}
for word in words:
    lengths[len(word)] = lengths.get(len(word), 0) + 1

for length in sorted(lengths):
    print(f"{length}| {'*' * lengths[length]} {lengths[length]}")
