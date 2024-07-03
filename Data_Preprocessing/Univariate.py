class Univariate():
    
    def quanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            if(dataset[columnName].dtype=='O'):
                qual.append(columnName)
            else:
                quan.append(columnName)
        return quan,qual
    def FreqTable(columnName,dataset):
        FreqTable=pd.DataFrame(columns=["Unique_Values","Frequency","Relative_freq","Cumsum"])
        FreqTable["Unique_Values"]=dataset[columnName].value_counts().index
        FreqTable["Frequency"]=dataset[columnName].value_counts().values
        FreqTable["Relative_freq"]=FreqTable["Frequency"]/103
        FreqTable["Cumsum"]=FreqTable["Relative_freq"].cumsum()
        return FreqTable
    
    def Univaraite(dataset,quan):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","Q4:99%","Q5:100%","IQR","1.5Rule","Lesser","Greater","Min","Max"],columns=quan)
    for ColumnName in quan:
        descriptive[ColumnName]["Mean"]=dataset[ColumnName].mean()
        descriptive[ColumnName]["Median"]=dataset[ColumnName].median()
        descriptive[ColumnName]["Mode"]=dataset[ColumnName].mode()[0]
        descriptive[ColumnName]["Q1:25%"]=dataset.describe()[ColumnName]["25%"]
        descriptive[ColumnName]["Q2:50%"]=dataset.describe()[ColumnName]["50%"]
        descriptive[ColumnName]["Q3:75%"]=dataset.describe()[ColumnName]["75%"]
        descriptive[ColumnName]["Q4:99%"]=np.percentile(dataset[ColumnName],99)
        descriptive[ColumnName]["Q5:100%"]=dataset.describe()[ColumnName]["max"]
        descriptive[ColumnName]["IQR"]= descriptive[ColumnName]["Q3:75%"]-descriptive[ColumnName]["Q1:25%"]
        descriptive[ColumnName]["1.5Rule"]=1.5*descriptive[ColumnName]["IQR"]
        descriptive[ColumnName]["Lesser"]=descriptive[ColumnName]["Q1:25%"]-descriptive[ColumnName]["1.5Rule"]
        descriptive[ColumnName]["Greater"]=descriptive[ColumnName]["Q3:75%"]+descriptive[ColumnName]["1.5Rule"]
        descriptive[ColumnName]["Min"]=dataset[ColumnName].min()
        descriptive[ColumnName]["Max"]=dataset[ColumnName].max()
    return descriptive

    def Outlier_columnNames():
        Lesser = []
        Greater = []
        for ColumnName in quan:
            if descriptive[ColumnName]["Min"] < descriptive[ColumnName]["Lesser"]:
                Lesser.append(ColumnName)
            if descriptive[ColumnName]["Max"] > descriptive[ColumnName]["Greater"]:
                Greater.append(ColumnName)           
                
    def Replacing_Outliers():
        for columnName in Lesser:
            dataset[columnName][dataset[columnName]<descriptive[columnName]["Lesser"]]=descriptive[columnName]["Lesser"]
        for columnName in Greater:
            dataset[columnName][dataset[columnName]>descriptive[columnName]["Greater"]]=descriptive[columnName]["Greater"]
