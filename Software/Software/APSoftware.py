import os
import extractingFeatures15 as g
from xml.dom import minidom
import ageArrf15 as age
import genderArrf15 as gender
import xml.etree.cElementTree as ET
import codecs
import sys,getopt
import csv
from weka.core.converters import Loader

fname = "EF.txt"
Path = ""
testinginputPath = ""
trainedModelName = ""

def main(argv):
    global input
    global outputModel
    global inputModel
    global outputPrediction
    global isTest
    global my_list
    
    input = " ";
    outputModel = " ";
    inputModel = " ";
    outputPrediction = " ";
    counter = 0
    isTest = 0
    my_list = []
    
    try:
        opts, args = getopt.getopt(argv,"hi:o:m:",["ifile=","ofile=","mfile="])
        print len(opts);
    except getopt.GetoptError:
        sys.exit(2)
    if len(opts) == 3:
        isTest = 1
    else:
        isTest = 0

    for opt, arg in opts:
        print arg;
        if len(opts) == 3:
            if opt=="-i":
                input=arg
            elif opt=="-o":
                outputPrediction=arg
            elif opt=="-m":
                inputModel=arg
        else:
            if opt=="-i":
                input=arg
            elif opt=="-o":
                outputModel=arg

    if isTest == 0:
        import weka.core.jvm as jvm
        jvm.start();
        excractFeatures()
    
    if isTest == 1:
        import weka.core.jvm as jvm
        jvm.start();
        excractFeatures();
        jvm.stop()
        sys.exit();

     
def generateARRFs():
     name = "Train"
     if isTest == 0:
          f= "TrainingExtractedFeature"
          name = "Train"
          age.writeFile(f,name,outputModel, "yes");
          gender.writeFile(f,name,outputModel, "yes");
          createTrainedModel();
     
     if isTest == 1:
          f= "TestingExtractedFeature"
          name = "Test"
          age.writeFile(f,name,inputModel, "");
          gender.writeFile(f,name,inputModel, "")
          predictionFromModel();
     
def excractFeatures():
    i=0
    fileName = ""
    genderClass = ""
    ageClass = ""
    if isTest == 0:
         featureFileName = "TrainingExtractedFeature"
         truthFilePath = os.path.join(input,"Truth.csv")
         with open(truthFilePath) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if i != 0:
                    fileName = row[0]
                    genderClass = row[1]
                    ageClass = row[2]
                    f=open(os.path.join(input,fileName+".txt"), "r")
                    text=f.read().decode('utf8','ignore')
                    print fileName
                    #print text
                    g.writeFile(text,featureFileName, outputModel, genderClass, ageClass)
                i=i+1;
            generateARRFs()
    
    else:
         featureFileName = "TestingExtractedFeature"
         folderList=os.listdir(input)
         for file in folderList:
            if not "Store" in file:
                f=open(os.path.join(input,file),"r")
                text=f.read().decode('utf8','ignore')
                print file
                labels=file.split('.')
                my_list.append(str(labels[0]))
                g.writeFile(text,featureFileName, inputModel, "", "")
         generateARRFs()



def predictionFromModel():
    import weka.core.serialization as serialization
    from weka.classifiers import Classifier
    from weka.classifiers import Evaluation
    
    predictionsPath = outputPrediction
    models_dir = inputModel
    modelsList=os.listdir(inputModel)
    data_dir = input
    folderList=os.listdir(inputModel)
    i=0
    loader=Loader(classname="weka.core.converters.ArffLoader")
    from weka.core.classes import Random
    from weka.core.dataset import Instances
    
    data = loader.load_file(os.path.join(inputModel, "genderTest.arff"))
    data.class_is_last()
    modelName = "GenderModel.model"
    objects = serialization.read_all(os.path.join(inputModel,modelName))
    trainedModel = Classifier(jobject=objects[0])
    genderFile = open(os.path.join(outputPrediction,'Gender_Predictions.csv'), 'w')
    with genderFile:
        j=-1;
        fieldnames = ['Test_Author_Profile_Id','Gender']
        writer = csv.DictWriter(genderFile, fieldnames=fieldnames)
        writer.writeheader()
        for index, inst in enumerate(data):
            j=j+1;
            pred = trainedModel.classify_instance(inst)
            dist = trainedModel.distribution_for_instance(inst)
            print(str(index+1) + ": label index=" + str(pred) + ", class distribution=" + str(dist))
            if(str(pred) == '0.0'):
                writer.writerow({'Test_Author_Profile_Id' : my_list[j], 'Gender' :'male'})
            if(str(pred) == '1.0'):
                writer.writerow({'Test_Author_Profile_Id' : my_list[j], 'Gender' :'female'})
    
    data = loader.load_file(os.path.join(inputModel, "ageTest.arff"))
    data.class_is_last()
    modelName = "AgeModel.model"
    objects = serialization.read_all(os.path.join(inputModel,modelName))
    trainedModel = Classifier(jobject=objects[0])
    ageFile = open(os.path.join(outputPrediction,'Age_Predictions.csv'), 'w')

    with ageFile:
        j=-1;
        fieldnames = ['Test_Author_Profile_Id','Age']
        writer = csv.DictWriter(ageFile, fieldnames=fieldnames)
        writer.writeheader()
        for index, inst in enumerate(data):
            j=j+1;
            pred = trainedModel.classify_instance(inst)
            dist = trainedModel.distribution_for_instance(inst)
            print(str(index+1) + ": label index=" + str(pred) + ", class distribution=" + str(dist))
            if(str(pred) == '0.0'):
                writer.writerow({'Test_Author_Profile_Id' : my_list[j], 'Age' :'15-19'})
            if(str(pred) == '1.0'):
                writer.writerow({'Test_Author_Profile_Id' : my_list[j], 'Age' :'20-24'})
            if(str(pred) == '2.0'):
                writer.writerow({'Test_Author_Profile_Id' : my_list[j], 'Age' :'25-xx'})
    os._exit(0)

def createTrainedModel():
    from weka.core.converters import Loader
    folderList=os.listdir(outputModel)
    i=0
    classi = ""
    loader=Loader(classname="weka.core.converters.ArffLoader")
    data = loader.load_file(os.path.join(outputModel, "genderTrain.arff"))
    data.class_is_last()
    from weka.classifiers import Classifier
    classi = "weka.classifiers.bayes.NaiveBayes"
    cls = Classifier(classname=classi)
    from weka.attribute_selection import ASSearch, ASEvaluation, AttributeSelection
    search = ASSearch(classname="weka.attributeSelection.Ranker",options=["-1.7976931348623157E308","-1"])
        #evaluator = ASEvaluation(classname="weka.attributeSelection.ChiSquaredAttributeEval")
        #attsel = AttributeSelection()
        #attsel.search(search)
        #attsel.evaluator(evaluator)
        #attsel.select_attributes(data)
    cls.build_classifier(data)
    import weka.core.serialization as serialization
    from weka.core.dataset import Instances
    serialization.write_all(os.path.join(outputModel,"GenderModel"+".model"),[cls,Instances.template_instances(data)])
    from weka.classifiers import Evaluation
    from weka.core.classes import Random
    evl= Evaluation(data)
    evl.crossvalidate_model(cls, data, 10, Random(1))
    print "Gender model predictions"
    print cls
    #print(evl.percent_correct)
    print(evl.summary())
    print(evl.class_details())
    
    data = loader.load_file(os.path.join(outputModel, "ageTrain.arff"))
    data.class_is_last()
    classi = "weka.classifiers.bayes.NaiveBayes"
    cls = Classifier(classname=classi)
    from weka.attribute_selection import ASSearch, ASEvaluation, AttributeSelection
    search = ASSearch(classname="weka.attributeSelection.Ranker",options=["-1.7976931348623157E308","-1"])
    #evaluator = ASEvaluation(classname="weka.attributeSelection.ChiSquaredAttributeEval")
    #attsel = AttributeSelection()
    #attsel.search(search)
    #attsel.evaluator(evaluator)
    #attsel.select_attributes(data)
    #classi = "weka.classifiers.trees.J48"
    #classi = "weka.classifiers.functions.Logistic"
    #classi = "weka.classifiers.trees.RandomForest"
    #classi = "weka.classifiers.bayes.NaiveBayes"
    #classi = "weka.classifiers.functions.SMOreg"
    cls.build_classifier(data)
    print "Age model predictions"
    print cls
    import weka.core.serialization as serialization
    from weka.core.dataset import Instances
    serialization.write_all(os.path.join(outputModel,"AgeModel"+".model"),[cls,Instances.template_instances(data)])
    evl= Evaluation(data)
    evl.crossvalidate_model(cls, data, 10, Random(1))
    
    #print(evl.percent_correct)
    print(evl.summary())
    print(evl.class_details())
    os._exit(0)


main(sys.argv[1:])
