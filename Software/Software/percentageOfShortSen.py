import nltk
from nltk.tokenize import RegexpTokenizer

def percentageOfShortSen(text):
   
   count=0
  
   sentences = nltk.sent_tokenize(text)
   no_of_sen = len(sentences)
   
   #print no_of_sen

   for sen in sentences:
    tokenizer= RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(text)
    if len(words) < 8:
        count+=1

   #print count
   if no_of_sen != 0:
       return float(count*100)/no_of_sen
   else:
       return 0.5;

   
