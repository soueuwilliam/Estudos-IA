import pandas as pd
import numpy as np
# from sklearn.impute import SimpleImputer

class templateCreditaData:
    
    def __init__(self):
        
        self.base = self.getBaseCredit()
        
    def getBaseCredit(self) -> pd.DataFrame:
        
        base = pd.read_csv(fr'C:\Users\campo\Documents\GitHub\Estudos-IA\MlDsPyAZ\data\credit-data.csv')
        return base

