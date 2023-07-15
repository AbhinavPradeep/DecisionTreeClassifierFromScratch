class Question:
    def __init__(self,Attribute,Condition) -> None:
        self.Attribute = Attribute
        self.Condition = Condition

    def CheckCondition(self,Row:list):
        if self.Attribute == -1:
            self.AssignLabel(Row)
            return
        if Row[self.Attribute] == self.Condition:
            return True
        else:
            return False
        
    def AssignLabel(self,Row:list):
        Row[self.Attribute] = self.Condition

    def __str__(self) -> str:
        return f"Is Row[{self.Attribute}] == {self.Condition}?"
    
    __repr__ = __str__