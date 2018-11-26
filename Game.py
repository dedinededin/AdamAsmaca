from collections import OrderedDict


def gen(alphabet, words):
    wholeWords = str(''.join(words))
    dict = {}
    for n in wholeWords:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1

    freqList = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    print(freqList)
    for freq in freqList:
        if freq[0] in alphabet:
            return freq[0]


wordList = [line.rstrip('\n') for line in open('kelime-listesi.txt', encoding="utf-8")]
alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"

wordLength = int(input("Kelimen kaç harfli?"))
wordList = list(filter(lambda a: len(a) == wordLength, wordList))
theWord = "_" * wordLength
usedChars = ""
counter = 1;

while len(wordList) > 1:
    char = gen(alphabet, wordList)
    usedChars = usedChars + char
    isCharInWord = input("{}.Deneme : Kelimende {} harfi var mı? e/h".format(counter, char))
    counter = counter + 1
    if isCharInWord == "e":
        whereIsIt = input("Kelimenin neresinde (1,{})".format(wordLength))
        indexes = whereIsIt.split(" ")
        for index in indexes:
            index = int(index) - 1
            theWord = theWord[:index] + char + theWord[index + 1:]
            wordList = list(filter(lambda a: a[index] == char, wordList))

        for index in range(0, wordLength):
            if theWord[index] == "_":
                wordList = list(filter(lambda a: a[index] != char, wordList))

        print(theWord)
        print(wordList)
        wholeWords = str(''.join(wordList))
        alphabet = "".join(OrderedDict.fromkeys(wholeWords))

    if isCharInWord == "h":
        wordList = list(filter(lambda a: char not in a, wordList))
    # print(wordList)

    for ch in usedChars:
        try:
            alphabet = alphabet[:alphabet.index(ch)] + alphabet[alphabet.index(ch) + 1:]
        except:
            pass

print("Seçtiğin kelime: " + wordList[0])
