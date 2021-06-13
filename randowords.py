from random_word import RandomWords 
from PyDictionary import PyDictionary
from random import Random

r = RandomWords()
randy = Random()
dictionary=PyDictionary()

def getWord():
    word = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb,adjective", minLength=3)
    while ((word is None) or (" " in word)):
            word = getWord()
    return word

def checkDef(word):
    defs = dictionary.meaning(word, disable_errors=True) # all of the definitions for the word
    while defs is None:
        word = getWord()
        defs = dictionary.meaning(word, disable_errors=True) # all of the definitions for the word
    return word

def checkParens(definition):
    count = 0
    for i in definition:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
    if count!= 0:
        return definition+")"
    return definition

def generate():
    word = getWord()
    word = checkDef(word)
    defs = dictionary.meaning(word, disable_errors=True)
    if len(defs.keys()) > 1:
        partOfSpeech = randy.choice(list(defs.keys()))
    else:
        partOfSpeech = list(defs.keys())[0]
    definitions = defs.get(partOfSpeech)
    if len(definitions) > 1:
        definition = randy.choice(list(defs.get(partOfSpeech)))
    else: 
        definition = definitions[0]
    definition = checkParens(definition)
    partOfSpeech = partOfSpeech.lower()
    newString = word + "\n" + partOfSpeech + "\n" + definition
    while (len(newString) > 280):
        generate()

    return newString

def main():
    print(generate())

if __name__ == "__main__":
    main()
