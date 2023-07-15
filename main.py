from Node import Node
from DecisionTreeClassifier import DecisionTreeClassifier

Table = [["Yellow", "3", "Apple"],
         ["Green", "3", "Apple"],
         ["Red", "1", "Grape"],
         ["Red", "1", "Grape"],
         ["Yellow", "3", "Lemon"],
         ]

Classifier = DecisionTreeClassifier()

Tree = Classifier.BuildTree(Table)

def printTree(node:Node, level=0):
    if node != None:
        printTree(node.LeftNode, level + 1)
        print(' ' * 4 * level + '-> ' + f"{node}")
        printTree(node.RightNode, level + 1)

#print(CalculateImpurity(["L1","L1","L2","L3","L3"]))

#print(CalculateGain(["L1","L1","L2","L3","L3"],["L3"],["L1","L1","L2","L3"]))

printTree(Tree)