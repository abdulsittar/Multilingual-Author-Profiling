import os
import codecs

def writeFile(File,name,lang):

  wekaFile=open(os.path.join(os.path.join("C:/Users/ameer15/python-code/working-function",name),"gender15"+name+".arff"),'a+')

  wekaFile.write("@relation \"gender\" ")
  wekaFile.write("\n")
  if lang == "en":
        wekaFile.write("@attribute percentageOfQuesSen numeric")
	wekaFile.write("\n")
	
	wekaFile.write("@attribute class? {M,F}  ")
	wekaFile.write("\n")
	wekaFile.write("\n")
	wekaFile.write("@data")
	wekaFile.write("\n")

 
  
	f=open(os.path.join("C:/Users/ameer15/python-code/working-function",File+".txt"),'r')
	text=f.read()
	lines=text.split()

	for line in lines:
		w=line.split(',')
		#for i in range(0,29):
			#wekaFile.write(str(w[i]))
			#wekaFile.write(",")
		wekaFile.write(str(w[0]))
		wekaFile.write(",") 
		wekaFile.write("?")
		#wekaFile.write(str(w[29]))
		wekaFile.write("\n")                 
  
	wekaFile.close()
	f.close()

	
  elif lang == "it":
	wekaFile.write("@attribute percentageOfFullStops numeric ") 
	wekaFile.write("\n")
	wekaFile.write("@attribute class? {M,F}  ")
	wekaFile.write("\n")
	wekaFile.write("\n")
	wekaFile.write("@data")
	wekaFile.write("\n")

 
  
	f=open(os.path.join("C:/Users/ameer15/python-code/working-function",File+".txt"),'r')
	text=f.read()
	lines=text.split()

	for line in lines:
		w=line.split(',')
		#for i in range(0,29):
			#wekaFile.write(str(w[i]))
			#wekaFile.write(",")
    
		wekaFile.write(str(w[24]))
		wekaFile.write(",") 
		#wekaFile.write(str(w[29]))
		wekaFile.write("?")
		wekaFile.write("\n")                 
  
	wekaFile.close()
	f.close()

  elif lang == "nl":
        wekaFile.write("@attribute percentageOfQuesSen numeric")
	wekaFile.write("\n")
	wekaFile.write("@attribute class? {M,F}  ")
	wekaFile.write("\n")
	wekaFile.write("\n")
	wekaFile.write("@data")
	wekaFile.write("\n")

 
  
	f=open(os.path.join("C:/Users/ameer15/python-code/working-function",File+".txt"),'r')
	text=f.read()
	lines=text.split()

	for line in lines:
		w=line.split(',')
		#for i in range(0,29):
			#wekaFile.write(str(w[i]))
			#wekaFile.write(",")
		wekaFile.write(str(w[0]))
		wekaFile.write(",")
		wekaFile.write("?")
		#wekaFile.write(str(w[29]))
		wekaFile.write("\n")                 
  
	wekaFile.close()
	f.close()

      
  elif lang == "es":
        wekaFile.write("@attribute percentageOfQuesSen numeric")
	wekaFile.write("\n")
	wekaFile.write("@attribute class? {M,F}  ")
	wekaFile.write("\n")
	wekaFile.write("\n")
	wekaFile.write("@data")
	wekaFile.write("\n")

 
  
	f=open(os.path.join("C:/Users/ameer15/python-code/working-function",File+".txt"),'r')
	text=f.read()
	lines=text.split()

	for line in lines:
		w=line.split(',')
		#for i in range(0,29):
			#wekaFile.write(str(w[i]))
			#wekaFile.write(",")
		wekaFile.write(str(w[0]))
		wekaFile.write(",")
		wekaFile.write("?")
		#wekaFile.write(str(w[29])
		wekaFile.write("\n")                 
  
	wekaFile.close()
	f.close()