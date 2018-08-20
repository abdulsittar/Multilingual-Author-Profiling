import nltk
from nltk import word_tokenize

def percentageOfQueSen(text):

   count=0
   str='?'
   
   #no of sentences
   sentences = nltk.sent_tokenize(text)
   no_of_sen = len(sentences)
 
   for sen in sentences:
     if sen.find(str) !=-1:
        count+=1
    
   #print count
   #print no_of_sen
   
   if no_of_sen != 0:
       return (count*100)/no_of_sen
   else:
       return 0.5;
