import nltk
from nltk.tokenize import RegexpTokenizer

def percentageOfPronouns(text):

   count = 0
   no_of_words = 0

   #making word tokens

   tokenizer = RegexpTokenizer(r'\w+')
   words = tokenizer.tokenize(text)
   no_of_words = len(words)  

  
   tagged_tokens = nltk.pos_tag(words)
    
   for w in tagged_tokens:
      l=list(w)
      count+=l.count("PRP")
      count+=l.count("PRP$")
     
   if no_of_words != 0:
          return float(count*100)/no_of_words
   else:
       return 0.5;
