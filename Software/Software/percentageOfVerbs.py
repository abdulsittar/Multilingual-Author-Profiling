import nltk
from nltk.tokenize import RegexpTokenizer

def percentageOfVerbs(text):

   count = 0
   no_of_words =0

   ### calculating no of total words ###   
   tokenizer = RegexpTokenizer(r'\w+')
   words = tokenizer.tokenize(text)
   no_of_words = len(words)  
    
   tokens=nltk.wordpunct_tokenize(text)
   tagged_tokens=nltk.pos_tag(tokens)

   for w in tagged_tokens:
      l=list(w)
      count+=l.count("VB")
      count+=l.count("VBD")
      count+=l.count("VBN")
      count+=l.count("VBG")
      count+=l.count("VBP")
      count+=l.count("VBZ")   
  
   if no_of_words != 0:
          return float(count*100)/no_of_words
   else:
       return 0.5;
    
 
