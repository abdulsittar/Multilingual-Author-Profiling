import nltk
from nltk.tokenize import RegexpTokenizer

def percentageOfwords(text):
   
   count=0
  
   sentences = nltk.sent_tokenize(text)
   no_of_sen = len(sentences)

   tokenizer = RegexpTokenizer(r'\w+')
   words = tokenizer.tokenize(text)
   no_of_words = len(words)
   #print no_of_words
   
   for word in words:
       if len(word) >= 6:
          count+=1

   #print count
   if no_of_words != 0:
       return float(count*100)/no_of_words
   else:
       return 0.5;
   
