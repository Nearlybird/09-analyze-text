# Remember to reach out for help after your own due diligence

def analyze_text(text):
    #Create all the letters
    alf = "abcdefghijklmnopqrstuvwxyz"
    letters = 0
    e = "e"
    es = 0
    text = text.lower()
    for i in range(len(text)):
        if alf.find(text[i]) >= 0:
            letters += 1
        else:
            letters = letters
        if e.find(text[i]) >= 0:
            es += 1
        else:
            es = es
    percent = (es/letters)*100
    percent = '{0:.2f}'.format(percent)
    print("The text contains", letters, "alphabetic characters, of which", es,"(",percent,"""%) are ‘e’.""")
  

analyze_text("blueberries")

        #define number of letters in WORD
        #define number of Es in WORD
