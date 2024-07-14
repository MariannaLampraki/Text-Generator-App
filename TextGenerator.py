import glob


# Read text
def myStrip(word):
    return word.strip(',.?!\n"-();').lower()


def insertToWords(text):
    for line in text:
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

    # Graphing
    graph = {}  # Empty dictionary with words and following words

    def add_vector_to_graph(v1, v2, w):
        if v1 not in graph:
            graph[v1] = {}
        if v2 in graph[v1]:
            graph[v1][v2] += w
        else:
            graph[v1][v2] = w


    processed_words = {myStrip(word) for word in words}

    for file in files:
        with open(file, "r") as text:
            for line in text:
                items = line.split()
                processed_items = [myStrip(item) for item in items]
                for i in range(len(processed_items)-1):
                    if processed_items[i] in processed_words:
                        next_word = processed_items[i+1]
                        if next_word != "" and next_word != "â€“":
                            add_vector_to_graph(processed_items[i], next_word, 1)

    formatted_graph = {k: [item for sublist in [[key, val] for key, val in v.items()] for item in sublist] for k, v in
                       graph.items()}
    # Analyzing user input
    userin = input("Give me a word: ").lower()
    while userin != "q":
        if userin not in words.keys():
            print("I don't know this word :(")
        else:
            print(words.get(userin))
            possible_words = formatted_graph.get(userin)
            try:
                for i in range(0, 20, 2):
                    print(userin + " " + possible_words[i])
            except IndexError:
                print("No more following words")
        userin = input("Give me another word: ").lower()

except FileNotFoundError:
    print('File not found')
