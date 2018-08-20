import nltk
from nltk.tokenize import RegexpTokenizer

def percentageOfPrepositions(text):

   count = 0
   no_of_words = 0

   #making word tokens

   tokenizer = RegexpTokenizer(r'\w+')
   words = tokenizer.tokenize(text)
   no_of_words = len(words)  

  
   tagged_tokens = nltk.pos_tag(words)
    
   for key,value in tagged_tokens:
     if value == "IN":
        count+=1
        #print key

   #print count
   #print no_of_words
   if no_of_words != 0:
       return float(count*100)/no_of_words
   else:
       return 0.5;