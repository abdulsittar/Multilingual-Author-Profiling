import nltk
from nltk.tokenize import RegexpTokenizer

def averageSenLength(text):
  
   sentences = nltk.sent_tokenize(text)
   no_of_sen = len(sentences)
   #print sentences
   #print no_of_sen
   if( no_of_sen == 0):
        no_of_sen = len(text.split('\n'))
   #print text
   #print no_of_sen
   tokenizer = RegexpTokenizer(r'\w+')
   words = tokenizer.tokenize(text)
   no_of_words = len(words)
   #print words
   #print no_of_words
   if no_of_sen != 0:
       return no_of_words/no_of_sen
   else:
       return 0.5
