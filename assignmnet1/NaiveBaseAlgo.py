NoOfClass=3
NoOfFeatures=3

featureValueInputs=[2,2,3]
#table=[[2,4,1,2,4,2,1,2,2,3,3,1,2,4,2],[3,1,3,4,2,1,2,3,2,3,2,2,1,3,2],[2,4,2,3,4,3,4,3,4,3,1,1,4,4,4],[0,1,0,0,1,2,0,1,0,2,0,1,0,2,0]]
table=[]

def readfile():
    fin = open('../dataset/dataset1.txt','r')
    table=[]
    for line in fin.readlines():
        table.append( [ int (x) for x in line.split(',') ] )
    return table



def inputUserNumber(x):
    while True:
        num = input("\n Please enter a number "+x)
        try:
            int(num)
            return int(num)
        except ValueError:
            print ("please enter number only ivalid number is not allow")



def Display(likelihoods):
    likelihoodsCount=len(likelihoods)
    ClassName=['A','B','C']
    ProbilityOFClasses=[0.1,0.1,0.1]
    SumOFLikeliHood=sum(likelihoods)
    MaxClass="A"
    MaxValue=0
    for l in range(likelihoodsCount):
        ProbilityOFClasses[l]=likelihoods[l]/SumOFLikeliHood
        print ("Probility of class",ClassName[l],"=",ProbilityOFClasses[l],"with percentage is ",int(ProbilityOFClasses[l]*100))
        if(ProbilityOFClasses[l]>MaxValue):
            MaxValue=ProbilityOFClasses[l]
            MaxClass=ClassName[l]

    print ("Maximum probiblity of class =",MaxClass,"with percentage is",int(MaxValue*100))

#NaiveBaseAlgo
def NaiveBaseAlgo(featureValueInputs,table):
    likelihoods=[0.1,0,0]

    for c in range(NoOfClass):
        likelihoods[c]=findLikelihood(c,featureValueInputs,table)
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


table=readfile()
value=['X','Y','Z']
for r in range(len(value)):
    featureValueInputs[r]=inputUserNumber(value[r])
NaiveBaseAlgo(featureValueInputs,table)