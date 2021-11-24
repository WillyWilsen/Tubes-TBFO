import pandas as pd
from copy import copy

class Pandaren:
    
    def __init__(self, csvfile):
        self.df = pd.read_csv(csvfile)
    
    def show(self):
        print(self.df)
    
    def drop(self,col):
        self.df.drop(columns=col)
    
    def getDF(self):
        return self.df
    
    def getDuplicateDF(self):
        return copy(self.df)
    

instance = Pandaren("namafile.csv","paraminiharusnyagadatapigapapakarenabukansyntaxerror")

instance2 = instance.getDF()

instance3 = instance.getDuplicateDF()

illegal = ["col1", "col2", "col3"]
for illegal_col in illegal:
    instance.drop(illegal_col)

if instance2.columns == instance.columns:
    print("See, i told you it would refer to the same df")

if instance3.columns != instance.columns:
    print("See, the one using copy() didnt get changed, the columns still all there")