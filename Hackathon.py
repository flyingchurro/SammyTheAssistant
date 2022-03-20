import nltk
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from gtts import gTTS

   
note = input("Enter Text Here: ")
   

stopWords = set(stopwords.words("english"))
words = word_tokenize(note)
   

   
freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1
   

lines = sent_tokenize(note)
sentenceValue = dict()
   
for sentence in lines:
    for work, freq in freqTable.items():
        if work in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq
   
   
   
sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]
   

   
average = int(sumValues / len(sentenceValue))

summary = ''
for sentence in lines:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        summary += " " + sentence
print(summary)

myText = summary

#declare a variable for the language you want the tts to speak in
language = 'en'

#variable
output = gTTS(text=myText, lang=language, slow=False)

output.save("output.mp3")

os.system("start output.mp3")
