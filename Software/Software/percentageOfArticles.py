import nltk
from nltk.tokenize import RegexpTokenizer


def percentageOfArticles(text):

   count_a   = 0  
   count_and = 0
   count_the = 0

   no_of_words =0
   
   tokenizer = RegexpTokenizer(r'\w+')
   words = tokenizer.tokenize(text)
   no_of_words = len(words)  

   
   #counting articles
   count_a = words.count("a")
   count_an = words.count("an")
   count_the = words.count("the")
    
   count= count_a + count_an + count_the
   if no_of_words != 0:
    return float(count*100)/no_of_words
   else:
       return 0.5;
