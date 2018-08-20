import nltk
from nltk.tokenize import RegexpTokenizer
from textstat.textstat import textstat

def percentageOfOneSyllable(text):

   count = 0
   no_of_words =0
   
   tokenizer = RegexpTokenizer(r'\w+')
   words = tokenizer.tokenize(text)
   no_of_words = len(words)  

   
   for word in words:
      if(textstat.syllable_count(word)==1):
          count+=1
   
   if no_of_words != 0:
              return float(count*100)/no_of_words
   else:
       return 0.5;
