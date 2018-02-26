import pandas as pd 

def quarter_volume():
    data=pd.read_csv('apple.csv',header=0)
    #head=0: using the first row as column names
    data.index=pd.to_datetime(data.Date)
    data=data.Volume
    data=data.resample('Q')
    data=data.sum()
    data=data.sort_values()
    result=data[-2]
    return result


    return second_volume
