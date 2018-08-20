import nltk
import string

def percentageOfPunctuations(text):

   count = 0
   no_of_chars = 0

   p=string.punctuation   

   words = nltk.word_tokenize(text)
 
   #caluculating no of chars
   for word in words:
      no_of_chars+=len(word)

   chars=list(text)


   for c in chars:
       if c in p:
          count+=1
   if no_of_chars != 0:
    return float(count*100)/no_of_chars
   else:
       return 0.5;
