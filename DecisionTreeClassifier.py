import numpy as np
from Node import Node
from Question import Question
from operator import itemgetter
import collections

class DecisionTreeClassifier:

    #Massive bottleneck, fixed with collections.Counter
    def CalculateImpurity(self,Labels: list):
        UniqueLabels = []
        UniqueLabels = collections.Counter(Labels)
        UniqueLabels = list(UniqueLabels.items())
        # for Label in Labels:
        #     if (Label, Labels.count(Label)) not in UniqueLabels:
        #         UniqueLabels.append((Label, Labels.count(Label)))
        Impurity = 1-(sum([(j/(len(Labels)))**2 for i, j in UniqueLabels]))
        print(Impurity)
        return Impurity


    def CalculateAverageImpurity(self,Labels1, Labels2):
        AverageImpurity = abs(((len(Labels1)/(len(Labels1)+len(Labels2)))*self.CalculateImpurity(
            Labels1))+((len(Labels2)/(len(Labels1)+len(Labels2)))*self.CalculateImpurity(Labels2)))
        return AverageImpurity


    def CalculateGain(self,Parent, Labels1, Labels2):
        InformationGain = abs(self.CalculateImpurity(
            Parent)-self.CalculateAverageImpurity(Labels1, Labels2))
        return InformationGain

    def GenerateProbability(self,Labels:list):
        LabelsAndProbability = []
        for Label in Labels:
            if (Label, Labels.count(Label)) not in LabelsAndProbability:
                LabelsAndProbability.append((Label, (Labels.count(Label))/len(Labels)))
        return LabelsAndProbability

    def BuildTree(self,DataTable: list[list]) -> Node:
        HeadNode = Node()
        Attributes = []
        for x in DataTable:
            for i, j in enumerate(x[0:-1]):
                if (i, j) not in Attributes:
                    Attributes.append((i, j))
        Questions = [Question(i, j) for (i, j) in Attributes]
        Labels = [x[-1] for x in DataTable]
        CurrentNode = HeadNode
        #print(Labels)
        # while CalculateImpurity(Labels) != 0 or len(Questions) != 0:
        QuestionEffectiveness = []
        for Q in Questions:
            TrueLabels = []
            TrueIndices = []
            FalseLabels = []
            FalseIndices = []
            i=0
            for Row in DataTable:
                if Q.CheckCondition(Row) == True:
                    TrueLabels.append(Row[-1])
                    TrueIndices.append(i)
                else:
                    FalseLabels.append(Row[-1])
                    FalseIndices.append(i)
                i+=1
            Gain = self.CalculateGain(Labels, TrueLabels, FalseLabels)
            QuestionEffectiveness.append((Q, Gain, TrueLabels, FalseLabels, TrueIndices, FalseIndices))
        #print(QuestionEffectiveness)
        if max(QuestionEffectiveness, key=itemgetter(1))[1] == 0:
            FinalQuestion = Question(-1,self.GenerateProbability(Labels))
            return Node(FinalQuestion)
        BestQuestion = max(QuestionEffectiveness, key=itemgetter(1))
        #print(BestQuestion)
        print(BestQuestion[0])
        CurrentNode.Question = BestQuestion[0]
        TrueLabels = BestQuestion[2]
        FalseLabels = BestQuestion[3]
        #True goes right
        if self.CalculateImpurity(TrueLabels) == 0:
            FinalQuestion = Question(-1,TrueLabels[0])
            HeadNode.RightNode = Node(FinalQuestion)
        else:
            #print(TrueLabels)
            TrueRows = [DataTable[i] for i in BestQuestion[4]]
            HeadNode.RightNode = self.BuildTree(TrueRows)
        #False goes left
        if self.CalculateImpurity(FalseLabels) == 0:
            FinalQuestion = Question(-1,FalseLabels[0])
            HeadNode.LeftNode = Node(FinalQuestion)
        else:
            #print(FalseLabels)
            FalseRows = [DataTable[i] for i in BestQuestion[5]]
            HeadNode.LeftNode = self.BuildTree(FalseRows)
        return HeadNode