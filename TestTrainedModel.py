from Node import Node
from DecisionTreeClassifier import DecisionTreeClassifier
from Question import Question
import pickle
import csv
import collections

with open('ShroomTree.pkl', 'rb') as f:
    Tree = pickle.load(f)
f.close()

with open('testdata.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

FormattedData = []
for Row in data:
    Row.append(Row.pop(0))
    Row.pop(4)
    FormattedData.append(Row)

# for row in FormattedData:
#     print(row)

with open('testdata.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

LabelsRemoved=[]
for Row in data:
    Row.append(Row.pop(0))
    Row.pop(4)
    Row[-1]=None
    LabelsRemoved.append(Row)

# for row in LabelsRemoved:
#     print(row)

def printTree(node:Node, level=0):
    if node != None:
        printTree(node.LeftNode, level + 1)
        print(' ' * 4 * level + '-> ' + f"{node}")
        printTree(node.RightNode, level + 1)

def AssignLabels(TableOFData : list[list],Tree: Node):
    for Row in TableOFData:
        CurrentNode = Tree
        Labelled = False
        while Labelled == False:
            Result = CurrentNode.Question.CheckCondition(Row)
            if Result == None:
                Labelled = True
            elif Result == True:
                CurrentNode = CurrentNode.RightNode
            elif Result == False:
                CurrentNode = CurrentNode.LeftNode

printTree(Tree)

AssignLabels(LabelsRemoved,Tree)

# for row in LabelsRemoved:
#     print(row)

def CheckLabels(Data,DataLabelsRemoved):
    BoolList =[]
    for i,j in enumerate(Data):
        BoolList.append(j == DataLabelsRemoved[i])
    FreqList = collections.Counter(BoolList)
    FreqList = list(FreqList.items())
    print(FreqList)
    print(f"{(FreqList[0][1]/(FreqList[1][1]+FreqList[0][1]))*100}%")
    

CheckLabels(FormattedData,LabelsRemoved)