#Using Dictionaries to Translate Words in Python
## Here a dict is used as a Database

EtoF = {'bread': 'du pain', 'meat': 'du vin',\
'eats': 'mange', 'drinks': 'bois',\
'likes': 'aime', 1: 'un',\
'6.00':'6.00'}

#newStr ='John eats bread'
def wordTranslator(key, dictionary):
    if key in dictionary:
        return dictionary[key]
    else:
        return key


#####################REAL TRANSLATOR FUNCTION
def realTranslate(sentence):
    msg ="Does not Suggest Violence: "
    numberFound = 0
    translator =''
    key =''
    for c in sentence:
        if c!=' ':
            key = key + c
        else:
            translator = translator + ' ' + wordTranslator(key, EtoF)
            key = '' ##Set the key again to empty
            numberFound+=1
    if(numberFound>0):
        return msg + "\n" + translator[1:] + ' ' + wordTranslator(key, EtoF)
    else:
        return "Does not Suggest Violence: " + "\n" + translator[1:] + ' ' + wordTranslator(key, EtoF)

#Supply word to translate here
masterTranslator = realTranslate('John eats bread and meat')
print (masterTranslator)





























