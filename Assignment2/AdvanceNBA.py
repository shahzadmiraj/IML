NoOfClass=1
NoOfFeatures=3

IndexOfclass=3
NamesOfClasses=[]
NoOfSamples=3
featureValueInputs=[]
table=[]


def stringIsnumber(string):
    try:
        val = int(string)
        return True
    except ValueError:
        return False


def CheckTwoStringNumber(stringlist):
    if stringIsnumber(stringlist[0]) and stringIsnumber(stringlist[1]):
        return True
    else:
        return False

def splitFunction(string):
    stringlist=string.split("-")
    if len(stringlist)==2:
        if CheckTwoStringNumber(stringlist):
            return True
    return False



def inputUserNumber(x):
    while True:
        num = input("\n Please enter a number feature "+x+"= ")
        try:
            float(num)
            return float(num)

        except ValueError:
            print ("please enter number only ivalid number is not allow")



def Display(likelihoods):
    likelihoodsCount=len(likelihoods)
    ClassName=NamesOfClasses
    ProbilityOFClasses=[]
    SumOFLikeliHood=sum(likelihoods)
    MaxClass=NamesOfClasses[0]
    MaxValue=0
    for l in range(likelihoodsCount):
        ProbilityOFClasses.append(likelihoods[l]/SumOFLikeliHood)
        print ("Probility of class",ClassName[l],"=",ProbilityOFClasses[l],"with percentage is ",int(ProbilityOFClasses[l]*100))
        if(ProbilityOFClasses[l]>MaxValue):
            MaxValue=ProbilityOFClasses[l]
            MaxClass=ClassName[l]

    print ("Maximum probiblity of class =",MaxClass,"with percentage is",int(MaxValue*100))

#NaiveBaseAlgo
def NaiveBaseAlgo(featureValueInputs,table):
    likelihoods=[]

    for c in NamesOfClasses:
        likelihoods.append(findLikelihood(c,featureValueInputs,table))
    Display(likelihoods)

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
dataOrignal=pd.read_csv('../dataset/breast-cancer.csv',header=None)


def TraverserTableForRanges(dataOrignal):
    dataOrignal=dataOrignal.head()
    for KeyRow, ValueColumns in dataOrignal.iteritems():
        for keyColumn,EachColumValue in ValueColumns.iteritems():
            if(dataOrignal.dtypes[keyColumn]=="object"):
                if splitFunction(EachColumValue):
                    NumberList=map(int, EachColumValue.split('-'))
                    startNumber=NumberList[0]
                    EndingNumber=NumberList[1]
                    for number in range(startNumber,EndingNumber+1):
                        CopyRow=dataOrignal.loc[KeyRow,]
                        print CopyRow


TraverserTableForRanges(dataOrignal)

# transpose=dataOrignal.T       #transpose
# headDataOrignal=dataOrignal.head()
# headTranspose=transpose.head()
#
#
#
#
#
#
# NoOfFeatures=headTranspose.shape[0]-1  #get no of feature from count rows
# IndexOfclass=NoOfFeatures # index of last row which is our class
# NamesOfClasses=headTranspose.loc[NoOfFeatures,].unique()
# NoOfClass=len(NamesOfClasses)
# NoOfSamples=headTranspose.shape[1]
#
#
# value=NamesOfClasses
# for f in range(NoOfFeatures):
#     featureValueInputs.append(inputUserNumber(str(f+1)))



# featureValueInputs=[2.3, 2.3, 3.3, 23.0]
# table=np.array(headTranspose)
# NaiveBaseAlgo(featureValueInputs,table)