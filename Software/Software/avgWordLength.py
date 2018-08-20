import nltk
from nltk.tokenize import RegexpTokenizer

def avgWordLength(text):
  
   #caluculating no of words
   tokenizer = RegexpTokenizer(r'\w+')
   words = tokenizer.tokenize(text)
   no_of_words = len(words)
   #print words
   #print no_of_words

   
   #caluculating no of chars
   no_of_chars=0
   for word in words:
    no_of_chars+=len(word)

 
  # print no_of_chars
   if no_of_words != 0:
        return float(no_of_chars)/no_of_words
   else:
        return 0.5

