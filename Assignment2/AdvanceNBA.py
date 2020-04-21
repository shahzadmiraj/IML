NoOfClass=1
NoOfFeatures=3

IndexOfclass=3
NamesOfClasses=[]
NoOfSamples=3
featureValueInputs=[]
table=[]





def inputUserNumber(x):
    while True:
        num = input("\n Please enter a number feature "+x+"= ")
        try:
            float(num)
            return float(num)

        except ValueError:
            print ("please enter number only ivalid number is not allow")



def Display(likelihoods,headTranspose,ClassName):
    likelihoodsCount=len(likelihoods)
    ProbilityOFClasses=[]
    SumOFLikeliHood=sum(likelihoods)
    MaxClass=ClassName[0]
    MaxValue=0
    for l in range(likelihoodsCount):
        ProbilityOFClasses.append(likelihoods[l]/SumOFLikeliHood)
        #print ("Probility of class",ClassName[l],"=",ProbilityOFClasses[l],"with percentage is ",int(ProbilityOFClasses[l]*100))
        if(ProbilityOFClasses[l]>MaxValue):
            MaxValue=ProbilityOFClasses[l]
            MaxClass=ClassName[l]

    #print ("Maximum probiblity of class =",MaxClass,"with percentage is",int(MaxValue*100))
    return MaxClass

#NaiveBaseAlgo
def NaiveBaseAlgo(featureValueInputs,table,headTranspose):
    likelihoods=[]

    NoOfFeatures = headTranspose.shape[0] - 1  # get no of feature from count rows
    IndexOfclass = NoOfFeatures  # index of last row which is our class
    NamesOfClasses = headTranspose.loc[NoOfFeatures,].unique()
    for c in NamesOfClasses:
        likelihoods.append(findLikelihood(c,featureValueInputs,table))
    return Display(likelihoods,headTranspose,NamesOfClasses)

def ProOfClass(C,table):
    count=0
    result=1.0
    ClassRow=len(table)-1
    SampleCol=len(table[0])
    for s in range(SampleCol):
        if(table[ClassRow][s]==C):
            count+=1
    #result=count//SampleCol
    result = count
    if(result==0):
        result=1.0
    return float(result)


def proInputGivenClass(feature,Valuefeature,C,table):
    #p(X|C)
   count=0
   result=1.2
   sampleCount=len(table[0])
   ClassRow=len(table)-1
   for s in range(sampleCount):
       if((table[feature][s]==Valuefeature)&(table[ClassRow][s]==C)):
           count+=1

   result=count/ProOfClass(C,table)
   if(result==0):
       result=1
   return result


def findLikelihood(C,featureValueInputs,table):
    #P(x/C)=P(x=?/C)P(x=?/C)P(x=?/C)*P(C)     constant C
    likeliHood=1.0
    sampleCol=len(table[0])
    for feature in range(len(table)-1):    #p(X|C) Variant X
        likeliHood*=proInputGivenClass(feature,featureValueInputs[feature],C,table)

    likeliHood*=ProOfClass(C,table)/sampleCol  # P(x/C)=P(x=?/C)P(x=?/C)P(x=?/C)*P(C)
    return likeliHood

import numpy as np
import  pandas as pd
import random
dataOrignal=pd.read_csv('../dataset/breast-cancer.csv',header=None)




transpose=dataOrignal     #transpose
headDataOrignal=dataOrignal.head()
headTranspose=transpose






NoOfFeatures=headTranspose.shape[0]-1  #get no of feature from count rows
IndexOfclass=NoOfFeatures # index of last row which is our class
NamesOfClasses=headTranspose.loc[NoOfFeatures,].unique()
NoOfClass=len(NamesOfClasses)
NoOfSamples=headTranspose.shape[1]





# value=NamesOfClasses
# for f in range(NoOfFeatures):
#     featureValueInputs.append(inputUserNumber(str(f+1)))

training=headTranspose
Testing=training


def GetFeatureValuesInputs(Testing,FeatureValuesInputs):
    table = np.array(Testing)
    totalColumn=len(table[0])
    for featureValue in range(totalColumn-1):
        FeatureValuesInputs.append(random.choice(table[:, featureValue]))

def TrainingDatasetPercentage(Testing):
    BestClass=Testing.loc[0,Testing.shape[1]-1]
    countDeleteRows=Testing.shape[0]-int(Testing.shape[0]*90/100)
    for i in range(countDeleteRows):
        totalrows=Testing.shape[0]
        row=int(random.random() * totalrows)
        Testing = Testing.drop(row)
        FeatureValuesInputs = []
        GetFeatureValuesInputs(Testing,FeatureValuesInputs)
        Testing=Testing.T
        table=np.array(Testing)
        BestClass=NaiveBaseAlgo(FeatureValuesInputs,table,Testing)
        Testing = Testing.T
        FeatureValuesInputs.append(BestClass)
        print "input features and best class",FeatureValuesInputs
        a_series = pd.Series(FeatureValuesInputs, index=Testing.columns)
        Testing = Testing.append(a_series, ignore_index=True)
        print Testing


TrainingDatasetPercentage(Testing)


