with open("PythonSummary.txt", "r") as file:
    fileText = []
    fileText = file.read()
    for char in '-.,!\n':
        newText = fileText.replace(char, ' ')
    final = newText.lower()
    wordList = final.split()
    print("Enter a word: ")
    word = input()
    wordFreq = []
    #for word in wordList:
    #    wordFreq.append(wordList.count(word))
    print(wordList.count(word))