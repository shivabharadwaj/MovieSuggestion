import numpy as np
from scipy import linalg
data1=np.genfromtxt('Big Data.csv',delimiter=',',dtype=None)
names=np.genfromtxt('u.item',delimiter='|',dtype=None)


##Create Array
def createArray(input, numMovies):
    w = input[:, 1].max()
    numUsers = w
    output = np.zeros((numMovies * numUsers, 3))
    temparr = np.zeros((numMovies * numUsers,3))
    x = input[:, 0]
    list = []
    for i in range(len(x)):
        if x[i] not in list:
            list.append(x[i])
    k=0
    total=0
    j=0
    new=0
    list0=[]
    list1=[]
    list2=[]
    for i in range (numMovies):
        for k in range (numUsers):
            if j+1>len(input):
                while k<numUsers:
                    temparr[k][1] = k + 1
                    temparr[k][2] = 0
                    temparr[k][0] = list[i]
                    list0.append(temparr[k][0])
                    list1.append(temparr[k][1])
                    list2.append(temparr[k][2])
                    k=k+1
                break
            if input[j][1]==k+1 and j<=len(input):
               temparr[k][1]=input[j][1]
               temparr[k][0]=list[i]
               temparr[k][2]=input[j][2]
               list0.append(temparr[k][0])
               list1.append(temparr[k][1])
               list2.append(temparr[k][2])
               j=j+1
            else:
               temparr[k][1]=k+1
               temparr[k][2]=0
               temparr[k][0]=list[i]
               list0.append(temparr[k][0])
               list1.append(temparr[k][1])
               list2.append(temparr[k][2])
    for i in range (len(list1)):
        output[i][0]=list0[i]
        output[i][1]=list1[i]
        output[i][2]=list2[i]
    return(output)

data = createArray(data1, 1682)



#Takes in User Movie as input and returns list of movies from most to least similar

lenData=len(data)
lenNames=len(names)
numReviewers=int(lenData/lenNames)




mystring=str(input('Enter movie here that you like: '))
inputName = bytes(mystring, 'utf-8')
q=len(inputName)
i=0
x=0
for i in range (lenNames):
    if names[i][1][0:q]==inputName:
        x=i
        break


while x==0 and mystring!="Toy Story":
    mystring = str(input('Maybe incorrect spelling or not in data set. Try Again: '))
    inputName = bytes(mystring, 'utf-8')
    q=len(inputName)
    i=0
    x=0
    for i in range (lenNames):
        if names[i][1][0:q]==inputName:
            x=i
            break
movieNum=names[i][0]
movieNum2=x





#Find StartPt of Movie
startPt=0
for i in range (lenData):
    if data[i][0]== movieNum:
        startPt=i
        break
newNumList = []
newNameList=[]


#Find list of similarities (in numbers)
for i in range (-x,lenNames-x):
    sum=0
    for j in range (numReviewers):
        #if j+startPt+numReviewers*i>=len(data):
         #   break
        sum = ((data[j + startPt][2] - data[j + startPt + (numReviewers * i)][2]) ** 2) + sum
    newNumList.append(sum**.5)
    newNameList.append(names[movieNum2+i][1])
    if (len(newNameList) == lenNames):
        break


#Deleting unnecessary information
del newNumList[x]
del newNameList[x]

#Creating ordered Final Lists
final=[]
for i in range (len(newNumList)):
    final.append(np.int(newNumList[i]))

order1=[]
order2=[]

for i in range (len(newNumList)):
    m=min(newNumList)
    y= newNumList.index(m)
    order1.append(newNumList[y])
    order2.append(newNameList[y])
    del newNumList[y]
    del newNameList[y]

#Print Solution
print("You might also like:")
for i in range (10):
    print(order2[i])

