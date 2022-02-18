from statistics import correlation
import numpy as np
import csv
import plotly.express as px
#fuction to create graph
def plotfigure(path):
    with open(path)as f:
        df=csv.DictReader(f)
        fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
        fig.show()

#function to get a data
def getdatasource(path):
    X=[]
    Y=[]
    with open(path)as f:
        ds=csv.DictReader(f)
        for i in ds:
            X.append(float(i["Coffee in ml"]))
            Y.append(float(i["sleep in hours"]))  
    return {"x":X,"y":Y}

#function to find correlation
def findcorrelation(ds):
    correlation=np.corrcoef(ds["x"],ds["y"])
    print(correlation[0,1])
    
#lets call the function
path="coffee.csv"
ds=getdatasource(path)
findcorrelation(ds)  
plotfigure(path)