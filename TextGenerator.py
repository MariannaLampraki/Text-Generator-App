import glob


# Read text
def myStrip(word):
    return word.strip(',.?!\n"-();').lower()


def insertToWords(text):
    for line in text:
        line = line
        for word in line.split(" "):
            newword = myStrip(word)
            if newword not in words.keys():
                words[newword] = 1
            else:
                words[newword] += 1


files = []
for filename in glob.glob("*.txt"):
    files.append(filename)
words = {}  # a dictionary holding each word and how many times it is displayed in the text

try:  # you can change the file paths if you want
    count = 0
    for file in files:
        with open(file, "r") as text:
            insertToWords(text)
    words.pop("")  # for some reason there was an element with the key "" and I had no idea how to get rid of it
    print("Files read: " + str(len(files)))
    count = 0
    for value in words.values():
        count += value
    print("Total words read: " + str(count))
    print("Unique words read: " + str(len(words)))
    num = 0
    rarestwords = []
    while num not in words.values():
        num += 1
    x = 5
    for word, value in words.items():
        if x == 0:
            break
        if value == num:
            rarestwords.append(word)
            x -= 1
    print("5 rarest words: " + str(rarestwords))

    # Analyzing user input
    userin = input("Give me a word: ").lower()
    while userin != "q":
        if userin not in words.keys():
            print("I don't know this word :(")
        else:
            print(words.get(userin))
        userin = input("Give me another word: ").lower()

except FileNotFoundError:
    print('File not found')
