import os
import percentageOfQuesSen as q
import percentageOfShortSen as s
import percentageOfLongSen as l
import averageSenLength as a
import avgWordLength as aw
import percentageOfWordsWithSixAndMoreLetters as sixW
import percentageOfWordsWithTwoAndThreeLetters as t
import percentageOfSemicolons as sc
import percentageOfPunctuations as pu
import percentageOfPronouns as pro
import percentageOfPrepositions as prp
import percentageOfCoordinatingConjunction as cc
import percentageOfComma as comma
import percentageOfArticles as art
import percentageOfWordsWithOneSyllable as syll1
import percentageOfWordsWithThreePlusSyllable as syll3
import averageSyllablePerWord as Asyll
import percentageOfAdj as adj
import percentageOfAdverb as adv
import percentageOfCapital as C
import percentageOfColons as colon
import percentageOfDet as det
import percentageOfDigits as digits
import percentageOfFullStops as fstops
import percentageOfInterjections as int
import percentageOfModal as modal
import percentageOfNouns as noun
import percentageOfPersonalPronouns as Perpro
import percentageOfVerbs as verb

from datetime import datetime


def writeFile(text,fileName, folderPath, genderClass, ageClass):
  
      ##creating file for writing features##
      wekaFile = open(os.path.join(folderPath,fileName + ".txt"),'a+')
      #wekaFile.write("@data")
      #wekaFile.write("\n")
      ## note starting time for feature extraction##
      #print "starting features extraction at:"+datetime.now().strftime('%H:%M:%S')
      ###extracting features from text###
      percentageOfQue =q.percentageOfQueSen(text)
#      percentageOfShort =s.percentageOfShortSen(text)
#      percentageOfLong =l.percentageOfLongSen(text)
#      averageLength =a.averageSenLength(text)
#      averageWord = aw.avgWordLength(text)
#      percentageOfSixWords = sixW.percentageOfwords(text)
#      percentageOfTwoThreeWords = t.percentageOfwords(text)
#      percentageOfSemicolons = sc.percentageOfSemiColons(text)
#      percentageOfPunctuations = pu.percentageOfPunctuations(text)
      #percentageOfPronouns = pro.percentageOfPronouns(text)
      #percentageOfPrepositions = prp.percentageOfPrepositions(text)
      #percentageOfCoordinatingConjunction = cc.percentageOfCC(text)
#      percentageOfComma = comma.percentageOfComma(text)
      #percentageOfArticles = art.percentageOfArticles(text)
      #percentageOfWordsWithOneSyllable=syll1.percentageOfOneSyllable(text)
      #percentageOfWordsWithThreePlusSyllable = syll3.percentageOfSyllable(text)
      #averageSyllablePerWord = Asyll.averageSyllable(text)
      #percentageOfAdj = adj.percentageOfAdj(text)
      #percentageOfAdverb = adv.percentageOfAdverb(text)
#      percentageOfCapital = C.percentageOfCapitalLetters(text)
#      percentageOfColons = colon.percentageOfColons(text)
      #percentageOfDet = det.percentageOfDet(text)
#      percentageOfDigits = digits.percentageOfDigits(text)
#      percentageOfFullStops = fstops.percentageOfFullStops(text)
      #percentageOfInterjections = int.percentageOfInterjections(text)
      #percentageOfModal= modal.percentageOfModal(text)
      #percentageOfNouns=noun.percentageOfNouns(text)
      #percentageOfPersonalPronouns= Perpro.percentageOfPronouns(text)
      #percentageOfVerbs=verb.percentageOfVerbs(text)

      ## note finishing time for feature extraction##
      #print "finishing  features extraction at:"+datetime.now().strftime('%H:%M:%S')
      ##writing attributes in file##

      wekaFile.write(str.format("{0:<5.3f}",percentageOfQue))
      wekaFile.write(",")
#      wekaFile.write(str.format("{0:<5.3f}",percentageOfShort))
#      wekaFile.write(",")
#      wekaFile.write(str.format("{0:<5.3f}",percentageOfLong))
#      wekaFile.write(",")
#      wekaFile.write(str.format("{0:<5.3f}",averageLength))
#      wekaFile.write(",")
#      wekaFile.write(str.format("{0:<5.3f}",averageWord))
#      wekaFile.write(",")
#      wekaFile.write(str.format("{0:<5.3f}",percentageOfSixWords))
#      wekaFile.write(",")
#      wekaFile.write(str.format("{0:<5.3f}",percentageOfTwoThreeWords))
#      wekaFile.write(",")
#      wekaFile.write(str.format("{0:<5.3f}",percentageOfSemicolons))
#      wekaFile.write(",")
#      wekaFile.write(str.format("{0:<5.3f}",percentageOfPunctuations))
#      wekaFile.write(",")
      #wekaFile.write(str.format("{0:<5.3f}",percentageOfPronouns))
      #wekaFile.write(",")
      #wekaFile.write(str.format("{0:<5.3f}",percentageOfPrepositions))
      #wekaFile.write(",")
      #wekaFile.write(str.format("{0:<5.3f}",percentageOfCoordinatingConjunction))
      #wekaFile.write(",")
#      wekaFile.write(str.format("{0:<5.3f}",percentageOfComma))
#      wekaFile.write(",")
      #wekaFile.write(str.format("{0:<5.3f}",percentageOfArticles))
      #wekaFile.write(",")
      #wekaFile.write(str.format("{0:<5.3f}",percentageOfWordsWithOneSyllable))
      #wekaFile.write(",")
      #wekaFile.write(str.format("{0:<5.3f}",percentageOfWordsWithThreePlusSyllable))
      #wekaFile.write(",")
      #wekaFile.write(str.format("{0:<5.3f}",averageSyllablePerWord))
      #wekaFile.write(",")
      #wekaFile.write(str.format("{0:<5.3f}",percentageOfAdj))
      #wekaFile.write(",")
      #wekaFile.write(str.format("{0:<5.3f}",percentageOfAdverb))
      #wekaFile.write(",")
#      wekaFile.write(str.format("{0:<5.3f}",percentageOfCapital))
#      wekaFile.write(",")
#      wekaFile.write(str.format("{0:<5.3f}",percentageOfColons))
#      wekaFile.write(",")
      #wekaFile.write(str.format("{0:<5.3f}",percentageOfDet))
      #wekaFile.write(",")
#      wekaFile.write(str.format("{0:<5.3f}",percentageOfDigits))
#      wekaFile.write(",")
#      wekaFile.write(str.format("{0:<5.3f}",percentageOfFullStops))
#      wekaFile.write(",")
      #wekaFile.write(str.format("{0:<5.3f}",percentageOfInterjections))
      #wekaFile.write(",")
      #wekaFile.write(str.format("{0:<5.3f}",percentageOfModal))
      #wekaFile.write(",")
      #wekaFile.write(str.format("{0:<5.3f}",percentageOfNouns))
      #wekaFile.write(",")
      #wekaFile.write(str.format("{0:<5.3f}", percentageOfPersonalPronouns))
      #wekaFile.write(",")
      #wekaFile.write(str.format("{0:<5.3f}",percentageOfVerbs))
      #wekaFile.write(",")
      if genderClass != "":
          wekaFile.write(genderClass)
          wekaFile.write(",")
      if ageClass != "":
          wekaFile.write(ageClass)
          wekaFile.write(",")
      wekaFile.write("\n")
      wekaFile.close()                                                                                                                                      
