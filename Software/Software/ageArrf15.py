import os
import codecs

def writeFile(file, name, folder, classVar):

  wekaFile=open(os.path.join(folder,"age"+name+".arff"),'a+')

  wekaFile.write("@relation \"age\" ")
  wekaFile.write("\n")
  wekaFile.write("@attribute percentageOfQuesSen numeric")
  wekaFile.write("\n")
#  wekaFile.write("@attribute percentageOfShortSen numeric")
#  wekaFile.write("\n")
#  wekaFile.write("@attribute percentageOfLongSen numeric ")
#  wekaFile.write("\n")
#  wekaFile.write("@attribute averageSenLength numeric ")
#  wekaFile.write("\n")
#  wekaFile.write("@attribute avgWordLength numeric ")
#  wekaFile.write("\n")
#  wekaFile.write("@attribute percentageOfWordsWithSixAndMoreLetters    numeric ")
#  wekaFile.write("\n")
#  wekaFile.write("@attribute percentageOfWordsWithTwoAndThreeLetters   numeric ")
#  wekaFile.write("\n")
#  wekaFile.write("@attribute percentageOfSemicolons   numeric ")
#  wekaFile.write("\n")
#  wekaFile.write("@attribute percentageOfPunctuations  numeric ")
#  wekaFile.write("\n")
  #wekaFile.write("@attribute percentageOfPronouns  numeric ")
  #wekaFile.write("\n")
  #wekaFile.write("@attribute percentageOfPrepositions  numeric ")
  #wekaFile.write("\n")
  #wekaFile.write("@attribute percentageOfCoordinatingConjunction  numeric ")
  #wekaFile.write("\n")
#  wekaFile.write("@attribute percentageOfComma numeric ")
#  wekaFile.write("\n")
  #wekaFile.write("@attribute percentageOfArticles numeric ")
  #wekaFile.write("\n")
  #wekaFile.write("@attribute percentageOfWordsWithOneSyllables numeric ")
  #wekaFile.write("\n")
  #wekaFile.write("@attribute percentageOfWordsWithThreePlusSyllable numeric ")
  #wekaFile.write("\n")
  #wekaFile.write("@attribute averageSyllablePerWords numeric ")
  #wekaFile.write("\n")
  #wekaFile.write("@attribute percentageOfAdj numeric ")
  #wekaFile.write("\n")
  #wekaFile.write("@attribute percentageOfAdverb numeric ")
  #wekaFile.write("\n")
#  wekaFile.write("@attribute percentageOfCapital numeric ")
#  wekaFile.write("\n")
#  wekaFile.write("@attribute percentageOfColons numeric ")
#  wekaFile.write("\n")
  #wekaFile.write("@attribute percentageOfDet numeric ")
  #wekaFile.write("\n")
#  wekaFile.write("@attribute percentageOfDigits numeric ")
#  wekaFile.write("\n")
#  wekaFile.write("@attribute percentageOfFullStops numeric ")
#  wekaFile.write("\n")
  #wekaFile.write("@attribute percentageOfInterjections numeric ")
  #wekaFile.write("\n")
  #wekaFile.write("@attribute percentageOfModal numeric ")
  #wekaFile.write("\n")
  #wekaFile.write("@attribute percentageOfNouns numeric ")
  #wekaFile.write("\n")
  #wekaFile.write("@attribute percentageOfPersonalPronouns numeric ")
  #wekaFile.write("\n")
  #wekaFile.write("@attribute percentageOfVerbs numeric ")
  #wekaFile.write("\n")
  wekaFile.write("@attribute class {\"15-19\", \"20-24\", \"25-xx\"}")
  wekaFile.write("\n")
  wekaFile.write("@data")
  wekaFile.write("\n")

  f=open(os.path.join(folder,file+".txt"),'r')
  text=f.read()
  lines=text.split()

  for line in lines:
     w=line.split(',')
     for i in range(0,1):
       wekaFile.write(str(w[i]))
       wekaFile.write(",")
     
     if classVar == "":
        wekaFile.write("?");
        wekaFile.write("\n");
     else:
        wekaFile.write('"' + str(w[2]) + '"');
        wekaFile.write("\n");
  wekaFile.close();
  f.close();
  
  
           
  
	
  
  





      
