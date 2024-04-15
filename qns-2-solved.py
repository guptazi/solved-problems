import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    bonus=employees['salary'].values*2
    employees['bonus']=bonus
    return employees
    
