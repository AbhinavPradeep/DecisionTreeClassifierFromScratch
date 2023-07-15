class Node:
    def __init__(self,Question=None,LeftNode=None,RightNode=None) -> None:
        self.Question = Question
        self.LeftNode = LeftNode
        self.RightNode = RightNode

    def __str__(self) -> str:
        return str(self.Question)
    
    __repr__ = __str__